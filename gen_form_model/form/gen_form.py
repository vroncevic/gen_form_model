# -*- coding: UTF-8 -*-

"""
 Module
     gen_form.py
 Copyright
     Copyright (C) 2018 Vladimir Roncevic <elektron.ronca@gmail.com>
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
     Define class GenForm with attribute(s) and method(s).
     Generate form model by template and parameters.
"""

import sys
from inspect import stack

try:
    from gen_form_model.form.read_template import ReadTemplate
    from gen_form_model.form.write_template import WriteTemplate
    from gen_form_model.form.form_selector import FormSelector
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_bad_call_error import ATSBadCallError
except ImportError as error:
    MESSAGE = "\n{0}\n{1}\n".format(__file__, error)
    sys.exit(MESSAGE)  # Force close python ATS ##############################

__author__ = "Vladimir Roncevic"
__copyright__ = "Copyright 2018, Free software to use and distributed it."
__credits__ = ["Vladimir Roncevic"]
__license__ = "GNU General Public License (GPL)"
__version__ = "1.0.0"
__maintainer__ = "Vladimir Roncevic"
__email__ = "elektron.ronca@gmail.com"
__status__ = "Updated"


class GenForm(object):
    """
        Define class GenForm with attribute(s) and method(s).
        Generate form model by template and parameters.
        It defines:

            :attributes:
                | __slots__ - Setting class slots
                | VERBOSE - Console text indicator for current process-phase
                | __reader - Reader API
                | __writter - Writer API
            :methods:
                | __init__ - Initial constructor
                | get_reader - Getter for reader object
                | get_writer - Getter for writer object
                | gen_form - Generate form module file
    """

    __slots__ = ('VERBOSE', '__reader', '__writer')
    VERBOSE = 'GEN_FORM_MODEL::FORM::GEN_FORM'

    def __init__(self, verbose=False):
        """
            Initial constructor.

            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :exceptions: None
        """
        verbose_message(GenForm.VERBOSE, verbose, 'Initial form generator')
        self.__reader = ReadTemplate(verbose=verbose)
        self.__writer = WriteTemplate(verbose=verbose)

    def get_reader(self):
        """
            Getter for reader object.

            :return: Read template object
            :rtype: <ReadTemplate>
            :exceptions: None
        """
        return self.__reader

    def get_writer(self):
        """
            Getter for writer object.

            :return: Write template object
            :rtype: <WriteTemplate>
            :exceptions: None
        """
        return self.__writer

    def gen_form(self, form_name, verbose=False):
        """
            Generate form module file.

            :param form_name: Parameter form class name
            :type: <str>
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :return: Boolean status True (success) | False
            :rtype: <bool>
            :exceptions: ATSBadCallError | ATSTypeError
        """
        status, func, form_content = False, stack()[0][3], None
        form_name_txt = 'Argument: expected form_name <int> object'
        form_name_msg = "{0} {1} {2}".format('def', func, form_name_txt)
        if form_name is None or not form_name:
            raise ATSBadCallError(form_name_msg)
        if not isinstance(form_name, str):
            raise ATSTypeError(form_name_msg)
        form_type = FormSelector.choose_form(verbose=verbose)
        if form_type != FormSelector.Cancel:
            form_content = self.__reader.read(form_type, verbose=verbose)
            if form_content:
                status = self.__writer.write(
                    form_content, form_name, verbose=verbose
                )
        return True if status else False