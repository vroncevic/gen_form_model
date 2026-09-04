# -*- coding: UTF-8 -*-

'''
Module
    opt_validator_test.py
Info
    Unit tests for GenFormModelBundleOptionsValidator class.
'''

from __future__ import annotations

import unittest

from gen_form_model.setup.opt_validator import GenFormModelBundleOptionsValidator


class TestGenFormModelBundleOptionsValidator(unittest.TestCase):

    def test_validate_success(self) -> None:
        options = {'info_file': 'some_path'}
        GenFormModelBundleOptionsValidator.validate(options)

    def test_validate_none(self) -> None:
        with self.assertRaises(Exception):
            GenFormModelBundleOptionsValidator.validate(None)

    def test_validate_invalid_type(self) -> None:
        with self.assertRaises(Exception):
            GenFormModelBundleOptionsValidator.validate("not_a_mapping")

        with self.assertRaises(Exception):
            options = {'info_file': 123}
            GenFormModelBundleOptionsValidator.validate(options)

    def test_is_valid_success(self) -> None:
        options = {'info_file': 'some_path'}
        self.assertTrue(GenFormModelBundleOptionsValidator.is_valid(options))

    def test_is_valid_failure(self) -> None:
        self.assertFalse(GenFormModelBundleOptionsValidator.is_valid(None))
        self.assertFalse(GenFormModelBundleOptionsValidator.is_valid("not_a_mapping"))
        self.assertFalse(GenFormModelBundleOptionsValidator.is_valid({'info_file': 123}))
