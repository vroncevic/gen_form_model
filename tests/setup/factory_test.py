# -*- coding: UTF-8 -*-

'''
Module
    factory_test.py
Info
    Unit tests for GenFormModelBundleFactory class.
'''

from __future__ import annotations

import unittest

from gen_form_model.setup.bundle import GenFormModelBundle
from gen_form_model.setup.factory import GenFormModelBundleFactory


class TestGenFormModelBundleFactory(unittest.TestCase):

    def test_create_bundle_default(self) -> None:
        bundle = GenFormModelBundleFactory.create_bundle()
        self.assertIsInstance(bundle, GenFormModelBundle)

    def test_create_bundle_with_options(self) -> None:
        options = {'info_file': 'gen_form_model/infrastructure/config/gen_form_model.cfg'}
        bundle = GenFormModelBundleFactory.create_bundle(options)
        self.assertIsInstance(bundle, GenFormModelBundle)

    def test_create_bundle_invalid_options(self) -> None:
        options = {'info_file': 123}
        with self.assertRaises(Exception):
            GenFormModelBundleFactory.create_bundle(options)

    def test_get_version(self) -> None:
        self.assertEqual(GenFormModelBundleFactory.get_version(), '2.0.0')
