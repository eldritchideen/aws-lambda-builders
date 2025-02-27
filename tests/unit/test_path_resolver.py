from unittest import TestCase

import os
import mock

from aws_lambda_builders import utils
from aws_lambda_builders.path_resolver import PathResolver


class TestPathResolver(TestCase):
    def setUp(self):
        self.path_resolver = PathResolver(runtime="chitti2.0", binary="chitti", additional_binaries=["chitti2"])

    def test_inits(self):
        self.assertEqual(self.path_resolver.runtime, "chitti2.0")
        self.assertEqual(self.path_resolver.binary, "chitti")
        self.assertEqual(self.path_resolver.executables, ["chitti2.0", "chitti", "chitti2"])

    def test_which_fails(self):
        with self.assertRaises(ValueError):
            utils.which = lambda x: None
            self.path_resolver._which()

    def test_which_success_immediate(self):
        with mock.patch.object(self.path_resolver, "_which") as which_mock:
            which_mock.return_value = os.getcwd()
            self.assertEqual(self.path_resolver.exec_paths, os.getcwd())
