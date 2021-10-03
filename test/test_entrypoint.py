import unittest

from project_constants import *

import writ

class TestBasicNonBrokenness(unittest.TestCase):

    def setUp(self):
        pass

    def test_entrypoint_module_name_matches_app_name(self):
        """Does the entrypoint script's name match the specified app name?"""
        self.assertEqual(writ.__name__, APP_NAME)
