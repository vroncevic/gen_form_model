# -*- coding: UTF-8 -*-

'''
 Module
     read_template.py
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
     Defined class ReadTemplate with attribute(s) and method(s).
     Created API for read a template file and return in string format.
'''

import sys
from os.path import exists

try:
    from pathlib import Path
    from ats_utilities.checker import ATSChecker
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.console_io.error import error_message
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_bad_call_error import ATSBadCallError
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


class ReadTemplate(object):
    '''
        Defined class ReadTemplate with attribute(s) and method(s).
        Created API for read a template file and return in string format.
        It defines:

            :attributes:
                | __slots__ - Setting class slots.
                | VERBOSE - Console text indicator for current process-phase.
                | __TEMPLATE_DIR - Prefix path to templates.
                | __template - Absolute template file path.
            :methods:
                | __init__ - Initial constructor.
                | get_template - Getter for template object.
                | read - Read a template and return a string representation.
                | __str__ - Dunder method for ReadTemplate.
    '''

    __slots__ = ('VERBOSE', '__TEMPLATE_DIR', '__template')
    VERBOSE = 'GEN_FORM_MODEL::PRO::READ_TEMPLATE'
    __TEMPLATE_DIR = '/../conf/template/'

    def __init__(self, verbose=False):
        '''
            Initial constructor.

            :param verbose: Enable/disable verbose option.
            :type verbose: <bool>
            :exceptions: None
        '''
        verbose_message(ReadTemplate.VERBOSE, verbose, 'init template')
        self.__template = '{0}{1}'.format(
            Path(__file__).resolve().parent, ReadTemplate.__TEMPLATE_DIR
        )

    def get_template(self):
        '''
            Getter for template object.

            :return: Template object.
            :rtype: <str>
            :exceptions: None
        '''
        return self.__template

    def read(self, form_template, verbose=False):
        '''
            Read a template and return a string representation.

            :param form_template: Form template file.
            :type form_template: <str>
            :param verbose: Enable/disable verbose option.
            :type verbose: <bool>
            :return: Form content | None.
            :rtype: <str> | <NoneType>
            :exception: ATSTypeError | ATSBadCallError
        '''
        checker, error, status = ATSChecker(), None, False
        error, status = checker.check_params([
            ('str:form_template', form_template)
        ])
        if status == ATSChecker.TYPE_ERROR:
            raise ATSTypeError(error)
        if status == ATSChecker.VALUE_ERROR:
            raise ATSBadCallError(error)
        template_file, form_content = '{0}{1}'.format(
            self.__template, form_template
        ), None
        verbose_message(
            ReadTemplate.VERBOSE, verbose, 'loading template', template_file
        )
        if bool(template_file) and exists(template_file):
            with open(template_file, 'r') as form_file:
                form_content = form_file.read()
        else:
            error_message(
                ReadTemplate.VERBOSE, 'check file {0}'.format(template_file)
            )
        return form_content

    def __str__(self):
        '''
            Dunder method for ReadTemplate.

            :return: Object in a human-readable format.
            :rtype: <str>
            :exceptions: None
        '''
        return '{0} ({1})'.format(
            self.__class__.__name__, str(self.__template)
        )
