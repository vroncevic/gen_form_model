# -*- coding: UTF-8 -*-
# form_selector.py
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

try:
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.console_io.error import error_message
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


class FormSelector(object):
    """
        Define class ModelSelector with attribute(s) and method(s).
        Selecting python template form for generating process.
        It defines:
            attribute:
                __slots__ - Setting class slots
                VERBOSE - Console text indicator for current process-phase
                Django  - 0 Django form
                Flask   - 1 Flask form
                Cancel  - 2 Cancel option
                __MODULES - Dictionary with options
            method:
                __init__ - Initial constructor
                choose_form - Selecting type of form for generating process
                format_name - Formatting name (class and file name)
    """

    __slots__ = ('VERBOSE', 'Django', 'Flask', 'Cancel', '__MODULES')
    VERBOSE = 'FORM::FORM_SELECTOR'
    Django, Flask, Cancel = range(3)
    __MODULES = {
        Django: 'Django form',
        Flask: 'Flask form',
        Cancel: 'Cancel'
    }

    def __init__(self, verbose=False):
        """
            Initial constructor.
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :exceptions: None
        """
        verbose_message(FormSelector.VERBOSE, verbose, 'Initial form selector')

    @classmethod
    def choose_form(cls, verbose=False):
        """
            Selecting type of form for generating process.
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :return: Form type
            :rtype: <int>
            :exceptions: None
        """
        verbose_message(FormSelector.VERBOSE, verbose, 'Selecting form model')
        print("\n form option list:")
        for key in sorted(FormSelector.__MODULES):
            print("  {0} {1}".format(key, FormSelector.__MODULES[key]))
        while True:
            form_type = int(input(' Select form: '))
            if form_type not in FormSelector.__MODULES.keys():
                error_message(FormSelector.VERBOSE, 'Not supported choice')
            else:
                break
        return form_type

    @classmethod
    def format_name(cls, form_name, verbose=False):
        """
            Formatting name (class and file name).
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :param form_name: Form name
            :type form_name: <str>
            :return: File name with extension | None
            :rtype: <str> | <NoneType>
        """
        verbose_message(FormSelector.VERBOSE, verbose, 'form name', form_name)
        return "{0}{1}".format(form_name.lower(), '.py') if form_name else None

