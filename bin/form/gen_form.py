# -*- coding: UTF-8 -*-
# gen_form.py
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
    from form.read_template import ReadTemplate
    from form.write_template import WriteTemplate
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


class GenForm(ReadTemplate, WriteTemplate):
    """
        Define class GenForm with attribute(s) and method(s).
        Generate form model by template and parameters.
        It defines:
            attribute:
                __CLASS_SLOTS__ - Setting class slots
                VERBOSE - Console text indicator for current process-phase
                __status - Operation status
            method:
                __init__ - Initial constructor
                gen_form - Generate form module file
    """

    __CLASS_SLOTS__ = (
        'VERBOSE',  # Read-Only
        '__status'
    )
    VERBOSE = 'FORM::GENFORM'

    def __init__(self, verbose=False):
        """
            Initial constructor.
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
        """
        cls = GenForm
        verbose_message(cls.VERBOSE, verbose, 'Initial form generator')
        ReadTemplate.__init__(self)
        WriteTemplate.__init__(self)
        self.__status = False

    def gen_form(self, form_name, verbose=False):
        """
            Generate form module file.
            :param form_name: Parameter form class name
            :type: <str>
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :return: Boolean status True (success) | False
            :rtype: <bool>
        """
        cls, func, form_content = ReadTemplate, stack()[0][3], None
        form_name_txt = 'Argument: expected form_name <int> object'
        form_name_msg = "{0} {1} {2}".format('def', func, form_name_txt)
        if form_name is None or not form_name:
            raise ATSBadCallError(form_name_msg)
        if not isinstance(form_name, str):
            raise ATSTypeError(form_name_msg)
        form_type = FormSelector.choose_form(verbose=verbose)
        if form_type != FormSelector.Cancel:
            form_content = self.read(form_type, verbose=verbose)
            if form_content:
                self.__status = self.write(
                    form_content, form_name, verbose=verbose
                )
                self.__status = True
        else:
            self.__status = True
        return self.__status
