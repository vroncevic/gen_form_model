# -*- coding: UTF-8 -*-
# write_template.py
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
from inspect import stack
from datetime import date
from os import getcwd, chmod
from string import Template

try:
    from form.form_selector import FormSelector
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.console_io.error import error_message
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_bad_call_error import ATSBadCallError
except ImportError as e:
    msg = "\n{0}\n{1}\n".format(__file__, e)
    sys.exit(msg)  # Force close python ATS ##################################

__author__ = "Vladimir Roncevic"
__copyright__ = "Copyright 2018, Free software to use and distributed it."
__credits__ = ["Vladimir Roncevic"]
__license__ = "GNU General Public License (GPL)"
__version__ = "1.0.0"
__maintainer__ = "Vladimir Roncevic"
__email__ = "elektron.ronca@gmail.com"
__status__ = "Updated"


class WriteTemplate(object):
    """
        Define class WriteTemplate with attribute(s) and method(s).
        Write a template content with parameters to a file.
        It defines:
            attribute:
                __slots__ - Setting class slots
                VERBOSE - Console text indicator for current process-phase
            method:
                __init__ - Initial constructor
                write - Write a template content with parameters to a file
    """

    __slots__ = ('VERBOSE')
    VERBOSE = 'FORM::WRITE_TEMPLATE'

    def __init__(self, verbose=False):
        """
            Initial constructor.
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :exceptions: None
        """
        verbose_message(WriteTemplate.VERBOSE, verbose, 'Initial template')

    def write(self, form_content, form_name, verbose=False):
        """
            Write a template content with parameters to a file.
            :param form_content: Template form content
            :type form_content: <str>
            :param form_name: Parameter form name
            :type form_name: <str>
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :return: Boolean status True (success) | False
            :rtype: <bool>
            :exception: ATSBadCallError | ATSTypeError
        """
        func = stack()[0][3]
        form_content_txt = 'Argument: expected form_content <str> object'
        form_content_msg = "{0} {1} {2}".format('def', func, form_content_txt)
        form_name_txt = 'Argument: expected form_name <str> object'
        form_name_msg = "{0} {1} {2}".format('def', func, form_name_txt)
        if form_content is None or not form_content:
            raise ATSBadCallError(form_content_msg)
        if not isinstance(form_content, str):
            raise ATSTypeError(form_content_msg)
        if form_name is None or not form_name:
            raise ATSBadCallError(form_name_msg)
        if not isinstance(form_name, str):
            raise ATSTypeError(form_name_msg)
        file_name = FormSelector.format_name(form_name)
        if file_name:
            verbose_message(
                WriteTemplate.VERBOSE, verbose, 'Generating form model'
            )
            current_dir = getcwd()
            module_file = "{0}/{1}".format(current_dir, file_name)
            module_info = {
                'mod': "{0}".format(form_name),
                'modlc': "{0}".format(form_name.lower()),
                'date': "{0}".format(date.today()),
                'year': "{0}".format(date.today().year)
            }
            template = Template(form_content)
            with open(module_file, 'w') as form_file:
                form_file.write(template.substitute(module_info))
                chmod(module_file, 0o666)
                status = True
        else:
            error_message(
                WriteTemplate.VERBOSE, 'Failed to select module file name'
            )
        return True if status else False

