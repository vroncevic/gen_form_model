# -*- coding: UTF-8 -*-
# gen_form_model.py
# Copyright (C) 2018 Vladimir Roncevic <elektron.ronca@gmail.com>
#
# gen_form_model is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# gen_form_model is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program. If not, see <http://www.gnu.org/licenses/>.
#

import sys
from os import getcwd

try:
    from pathlib import Path

    from ats_utilities.cfg_base import CfgBase
    from form.gen_form import GenForm
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.console_io.error import error_message
    from ats_utilities.console_io.success import success_message
except ImportError as e:
    msg = "\n{0}\n{1}\n".format(__file__, e)
    sys.exit(msg)  # Force close python ATS ###################################

__author__ = "Vladimir Roncevic"
__copyright__ = "Copyright 2018, Free software to use and distributed it."
__credits__ = ["Vladimir Roncevic"]
__license__ = "GNU General Public License (GPL)"
__version__ = "1.0.0"
__maintainer__ = "Vladimir Roncevic"
__email__ = "elektron.ronca@gmail.com"
__status__ = "Updated"


class GenFormModel(CfgBase, GenForm):
    """
        Define class GenFormModel with attribute(s) and method(s).
        Load a settings, create an interface and run operation(s).
        It defines:
            attribute:
                __CLASS_SLOTS__ - Setting class slots
                VERBOSE - Console text indicator for current process-phase
                __CONFIG - Configuration file path
                __OPS -  Tool options (list)
            method:
                __init__ - Initial constructor
                process - Process and run tool option
    """

    __CLASS_SLOTS__ = (
        'VERBOSE', '__CONFIG', '__OPS'  # Read-Only
    )
    VERBOSE = 'GENERATE_FORM_MODEL'
    __CONFIG = '/../conf/gen_form_model.cfg'
    __OPS = ['-g', '--gen', '-h', '--version']

    def __init__(self, verbose=False):
        """
            Loading configuration and setting argument options.
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
        """
        cls = GenFormModel
        verbose_message(cls.VERBOSE, verbose, 'Initial configuration')
        module_dir = Path(__file__).resolve().parent
        base_config_file = "{0}{1}".format(module_dir, cls.__CONFIG)
        CfgBase.__init__(self, base_config_file, verbose=verbose)
        tool_status = self.get_tool_status(verbose=verbose)
        if tool_status:
            self.add_new_option(
                cls.__OPS[0], cls.__OPS[1], dest='mod',
                help='generate form model'
            )
            GenForm.__init__(self, verbose=verbose)

    def process(self, verbose=False):
        """
            Process and run operation.
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :return: True (success) | False
            :rtype: <bool>
        """
        cls, status = GenFormModel, False
        tool_status = self.get_tool_status(verbose=verbose)
        if tool_status:
            self.show_base_info(verbose=verbose)
            num_of_args = len(sys.argv)
            if num_of_args > 1:
                op = sys.argv[1]
                if op not in cls.__OPS:
                    sys.argv = []
                    sys.argv.append('-h')
            else:
                sys.argv.append('-h')
            opts, args = self.parse_args(sys.argv)
            num_of_args, current_dir = len(args), getcwd()
            form_file = "{0}/{1}{2}".format(current_dir, opts.mod, '.py')
            form_file_exist = Path(form_file).exists()
            if num_of_args == 1 and opts.mod and not form_file_exist:
                message = "{0} {1} [{2}]".format(
                    "[{0}]".format(self.get_ats_name(verbose=verbose)),
                    'Generating module', form_file
                )
                print(message)
                gen_form_status = self.gen_form(
                    "{0}".format(opts.mod), verbose=verbose
                )
                if gen_form_status:
                    success_message(
                        self.get_ats_name(verbose=verbose), 'Done\n'
                    )
                    status = True
                else:
                    error_message(
                        self.get_ats_name(verbose=verbose),
                        'Failed to process and run option'
                    )
            else:
                error_message(
                    self.get_ats_name(verbose=verbose), form_file,
                    'already exist in current directory'
                )
        else:
            error_message('gen_form_model', 'Tool is not operational')
        return True if status else False
