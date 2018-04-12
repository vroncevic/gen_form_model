# -*- coding: UTF-8 -*-
# read_template.py
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

try:
    from pathlib import Path

    from ats_utilities.slots import BaseSlots
    from form.form_selector import FormSelector
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_bad_call_error import ATSBadCallError
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


class ReadTemplate(BaseSlots):
    """
        Define class ReadTemplate with attribute(s) and method(s).
        Read a template file (setup.template).
        It defines:
            attribute:
                __CLASS_SLOTS__ - Setting class slots
                VERBOSE - Console text indicator for current process-phase
                __TEMPLATE_DIR - Prefix path to templates
                __TEMPLATES - Modules (python templates)
                __template - Absolute template file path
            method:
                __init__ - Create and initial instance
                read - Read a template and return a string representation
    """

    __CLASS_SLOTS__ = (
        'VERBOSE', '__TEMPLATE_DIR', '__TEMPLATES',  # Read-Only
        '__template'
    )
    VERBOSE = 'FORM::READ_TEMPLATE'
    __TEMPLATE_DIR = '/../../conf/template'
    __TEMPLATES = {
        FormSelector.Django: 'django.template',
        FormSelector.Flask: 'flask.template'
    }

    def __init__(self, verbose=False):
        """
            Setting template configuration directory.
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
        """
        cls, module_dir = ReadTemplate, Path(__file__).resolve().parent
        verbose_message(cls.VERBOSE, verbose, 'Initial template')
        BaseSlots.__init__(self)
        self.__template = "{0}{1}".format(module_dir, cls.__TEMPLATE_DIR)

    def read(self, form_type, verbose=False):
        """
            Read template.
            :param form_type: Type of form
            :type form_type: <int>
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :return: Form content
            :rtype: <str> | <NoneType>
            :exception: ATSBadCallError | ATSTypeError
        """
        cls, func, form_content = ReadTemplate, stack()[0][3], None
        form_type_txt = 'Argument: expected form_type <int> object'
        form_type_msg = "{0} {1} {2}".format('def', func, form_type_txt)
        if form_type is None:
            raise ATSBadCallError(form_type_msg)
        if not isinstance(form_type, int):
            raise ATSTypeError(form_type_msg)
        template_file = "{0}/{1}".format(
            self.__template, cls.__TEMPLATES[form_type]
        )
        verbose_message(
            cls.VERBOSE, verbose, 'Loading template', template_file
        )
        try:
            with open(template_file, 'r') as form_file:
                form_content = form_file.read()
        except AttributeError:
            pass
        return form_content
