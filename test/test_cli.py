import unittest

import sys
import os
import subprocess
# from contextlib import contextmanager

import cli

from project_constants import *

COMMAND_PREFIX = f"python3 -m {APP_NAME}"

class TestCLIObject(unittest.TestCase):

    def test_init(self):
        cli_object = cli.CLI()
        print(f"{type(cli_object)}")
        self.assertIsInstance(cli_object, cli.CLI)

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
