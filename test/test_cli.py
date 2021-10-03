import unittest

import sys
import os
import subprocess
# from contextlib import contextmanager

import cli

from project_constants import *

COMMAND_PREFIX = f"python3 -m {APP_NAME}"

class TestCLIObject(unittest.TestCase):
    """Tests for the CLI object and its methods."""

    def setUp(self):
        self.cli_object = cli.CLI()

    def test_init(self):
        self.assertIsInstance(self.cli_object, cli.CLI)

    def test_main(self):
        with self.assertRaises(SystemExit):  # SystemExit happens when main is called with no sysargv
            self.cli_object.main()

    def test_typos(self):
        self.assertIsNone(self.cli_object.typos())  # Doesn't return anything. If nothing broken, a None return
                                                    #   should be result of calling the method directly.

    def test_add(self):
        with self.assertRaises(SystemExit):  # "add" command can't be called without argument specifying the document
                                                #  to add
            self.cli_object.add()

    def test_checkout(self):
        with self.assertRaises(SystemExit):  # "checkout" command cannot be called without an argument specifying the
                                                #   deal to be checked out
            self.cli_object.checkout()

    def test_status(self):
        self.assertIsNone(self.cli_object.status())

class TestCommands(unittest.TestCase):
    """Test all supported commands by simulating command line user inputs and capturing stdout returned in response."""

    def setUp(self):
        pass

    def test_help(self):

        command_suffix = "--help"
        command = COMMAND_PREFIX + ' ' + command_suffix
        args = command.split()

        completed_proc = subprocess.run(
            args,
            capture_output=True,
            encoding="utf-8"
        )
        actual_output = completed_proc.stdout
        self.assertTrue(actual_output.startswith("usage:"))

class TestTyposCommand(unittest.TestCase):

    def setUp(self):
        pass

    def test_typos_command_returns_simulated_output(self):
        command_suffix = "typos"
        command = COMMAND_PREFIX + ' ' + command_suffix
        args = command.split()

        completed_proc = subprocess.run(
            args,
            capture_output=True,
            encoding="utf-8"
        )
        actual_output = completed_proc.stdout
        print(f"{actual_output=}")
        self.assertTrue(actual_output.startswith("[Simulated]"))

class TestAdd(unittest.TestCase):



    def test_add_command_simulates_adding_document_to_deal(self):
        command_suffix = "add Eighth_Lien_Unsecured_Cov_Lite_Credit_Agreement_Taylors_Version.docx"
        command = COMMAND_PREFIX + ' ' + command_suffix
        args = command.split()

        completed_proc = subprocess.run(
            args,
            capture_output=True,
            encoding="utf-8"
        )
        actual_output = completed_proc.stdout
        print(f"{actual_output=}")
        self.assertTrue(actual_output.startswith("[Simulated]"))

    def test_add_command_supports_spaces_in_filename(self):
        """Does the CLI correctly parse the filename as a single string even when it includes space characters?"""
        command_suffix = "add Eigth Lien Unsecured Cov Lite Credit Agreement Taylors Version.docx"
        command = COMMAND_PREFIX + ' ' + command_suffix
        args = command.split()
        completed_proc = subprocess.run(
            args,
            capture_output=True,
            encoding="utf-8"
        )
        actual_output = completed_proc.stdout
        print(f"{actual_output=}")
        self.assertTrue(actual_output.startswith("[Simulated]"))

    def test_add_command_supports_apostrophe_in_filename(self):
        command_suffix = "add Eigth Lien Unsecured Cov Lite Credit Agreement Taylor's Version.docx"
        command = COMMAND_PREFIX + ' ' + command_suffix
        args = command.split()
        completed_proc = subprocess.run(
            args,
            capture_output=True,
            encoding="utf-8"
        )
        actual_output = completed_proc.stdout
        print(f"{actual_output=}")
        self.assertTrue(actual_output.startswith("[Simulated]"))