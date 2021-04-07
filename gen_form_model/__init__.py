# -*- coding: UTF-8 -*-

'''
 Module
     gen_form_model.py
 Copyright
     Copyright (C) 2017 Vladimir Roncevic <elektron.ronca@gmail.com>
     gen_form_model is free software: you can redistribute it and/or modify it
     under the terms of the GNU General Public License as published by the
     Free Software Foundation, either version 3 of the License, or
     (at your option) any later version.
     gen_form_model is distributed in the hope that it will be useful, but
     WITHOUT ANY WARRANTY; without even the implied warranty of
     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
     See the GNU General Public License for more details.
     You should have received a copy of the GNU General Public License along
     with this program. If not, see <http://www.gnu.org/licenses/>.
 Info
     Defined class GenFormModel with attribute(s) and method(s).
     Load a base info, create an CLI interface and run operation(s).
'''

import sys
from os import getcwd

try:
    from pathlib import Path
    from gen_form_model.pro import GenForm
    from ats_utilities.cli.cfg_cli import CfgCLI
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.console_io.error import error_message
    from ats_utilities.console_io.success import success_message
except ImportError as ats_error_message:
    MESSAGE = '\n{0}\n{1}\n'.format(__file__, ats_error_message)
    sys.exit(MESSAGE)  # Force close python ATS ##############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, https://vroncevic.github.io/gen_form_model'
__credits__ = ['Vladimir Roncevic']
__license__ = 'https://github.com/vroncevic/gen_form_model/blob/master/LICENSE'
__version__ = '1.2.1'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class GenFormModel(CfgCLI):
    '''
        Defined class GenFormModel with attribute(s) and method(s).
        Load a base info, create an CLI interface and run operation(s).
        It defines:

            :attributes:
                | __slots__ - Setting class slots.
                | VERBOSE - Console text indicator for current process-phase.
                | __CONFIG - Configuration file path.
                | __OPS -  Tool options (list).
            :methods:
                | __init__ - Initial constructor.
                | process - Process and run tool option.
                | __str__ - Dunder method for GenFormModel.
    '''

    __slots__ = ('VERBOSE', '__CONFIG', '__OPS')
    VERBOSE = 'GEN_FORM_MODEL'
    __CONFIG = '/conf/gen_form_model.cfg'
    __OPS = ['-g', '--gen', '-v']

    def __init__(self, verbose=False):
        '''
            Loading configuration and setting argument options.

            :param verbose: Enable/disable verbose option.
            :type verbose: <bool>
            :exceptions: None
        '''
        verbose_message(GenFormModel.VERBOSE, verbose, 'init tool info')
        current_dir = Path(__file__).resolve().parent
        base_info = '{0}{1}'.format(current_dir, GenFormModel.__CONFIG)
        CfgCLI.__init__(self, base_info, verbose=verbose)
        if self.tool_operational:
            self.add_new_option(
                GenFormModel.__OPS[0], GenFormModel.__OPS[1], dest='mod',
                help='generate form model'
            )
            self.add_new_option(
                GenFormModel.__OPS[2], action='store_true', default=False,
                help='activate verbose mode for generation'
            )

    def process(self, verbose=False):
        '''
            Process and run operation.

            :param verbose: Enable/disable verbose option.
            :type verbose: <bool>
            :return: True (success) | False.
            :rtype: <bool>
            :exceptions: None
        '''
        status = False
        if self.tool_operational:
            num_of_args_sys = len(sys.argv)
            if num_of_args_sys > 1:
                operation = sys.argv[1]
                if operation not in GenFormModel.__OPS:
                    sys.argv = []
                    sys.argv.append('-h')
            else:
                sys.argv.append('-h')
            opts, args = self.parse_args(sys.argv)
            verbose_message(GenFormModel.VERBOSE, verbose, args)
            current_dir = Path(__file__).resolve().parent
            form_file = '{0}/{1}{2}'.format(current_dir, opts.mod, '.py')
            form_file_exist = Path(form_file).exists()
            if not form_file_exist:
                if num_of_args_sys >= 1 and bool(opts.mod):
                    print(
                        '{0} {1} [{2}]'.format(
                            '[{0}]'.format(GenFormModel.VERBOSE.lower()),
                            'generating form', opts.mod
                        )
                    )
                    generator = GenForm(verbose=opts.v or verbose)
                    status = generator.gen_form(
                        '{0}'.format(opts.mod), verbose=opts.v or verbose
                    )
                    if status:
                        success_message(GenFormModel.VERBOSE, 'done\n')
                    else:
                        error_message(
                            GenFormModel.VERBOSE, 'generation failed'
                        )
                else:
                    error_message(
                        GenFormModel.VERBOSE, 'provide form name'
                    )
            else:
                error_message(
                    GenFormModel.VERBOSE, 'form already exists'
                )
        else:
            error_message(
                GenFormModel.VERBOSE, 'tool is not operational'
            )
        return True if status else False

    def __str__(self):
        '''
            Dunder method for GenFormModel.

            :return: Object in a human-readable format.
            :rtype: <str>
            :exceptions: None
        '''
        return '{0} ({1})'.format(
            self.__class__.__name__, CfgCLI.__str__(self)
        )
