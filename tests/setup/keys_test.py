# -*- coding: UTF-8 -*-

'''
Module
    keys_test.py
Info
    Unit tests for GenFormModelBundleKeys class.
'''

from __future__ import annotations

import unittest
from types import MappingProxyType

from gen_form_model.setup.keys import GenFormModelBundleKeys


class TestGenFormModelBundleKeys(unittest.TestCase):

    def test_get_dependency_to_type(self) -> None:
        deps = GenFormModelBundleKeys.get_dependency_to_type()
        self.assertIsInstance(deps, MappingProxyType)
        self.assertIn(GenFormModelBundleKeys.DEPENDENCY_BASE, deps)
        self.assertIn(GenFormModelBundleKeys.DEPENDENCY_SERVICE, deps)
        self.assertIn(GenFormModelBundleKeys.DEPENDENCY_SUBPROCESSOR, deps)
        self.assertIn(GenFormModelBundleKeys.DEPENDENCY_CLI, deps)

    def test_get_option_to_type(self) -> None:
        opts = GenFormModelBundleKeys.get_option_to_type()
        self.assertIsInstance(opts, MappingProxyType)
        self.assertIn(GenFormModelBundleKeys.OPTION_INFO_FILE, opts)
