import sys
import argparse
import inspect

import controller

class CLI:

    controller_instance = controller.WritAPI()

    description_text = "Description text here"
    usage_text = "Usage text here"

    texts = {
        "main": {
            "description": "Description text here",
            "usage": "Usage text here"
        },
        "typos": {
            "description": "Typos Description text here",
            "usage": "Typos Usage text here"
        },
        "add": {
            "description": "Description text here",
            "usage": "Usage text here"
        },
        "checkout": {
            "description": "Description text here",
            "usage": "Usage text here"
        },
        "status": {
            "description": "Description text here",
            "usage": "Usage text here"
        }

    }
    
    def main(self):
        """Handles the root command and dispatches to appropriate subcommand handler methods."""
        texts = self.texts[inspect.currentframe().f_code.co_name]  # If we get name this function's name programatically,
                                                                    #  then one less thing to update.
        parser = argparse.ArgumentParser(
            description=texts["description"],
            usage=texts["usage"],
        )

        parser.add_argument("command", help="Subcommand to run")
        args = parser.parse_args(sys.argv[1:2])  # We want only sys.argv[1]. Default is sys.argv[1:]
        if not args.command:
            print(f"Unrecognized command")
            parser.print_help()
            exit(1)

        getattr(self, args.command)()  # Call the method matching the arg string.
        # TODO: Do this without getattr

    def typos(self):
        texts = self.texts[inspect.currentframe().f_code.co_name]
        parser = argparse.ArgumentParser(
            description=texts["description"],
            usage=texts["usage"],
        )

        parser.add_argument('-d')  # Default action is store value
        args = parser.parse_args(sys.argv[2:])

        print("[Simulated] Running typos checks")

    def add(self):
        texts = self.texts[inspect.currentframe().f_code.co_name]
        parser = argparse.ArgumentParser(
            description=texts["description"],
            usage=texts["usage"],
        )
        parser.add_argument(
            'document',
            help="filename of the document to add"
        )
        args = parser.parse_args(sys.argv[2:])

        print(f"[Simulated] Added {args.document} to the active deal.")

    def checkout(self):
        texts = self.texts[inspect.currentframe().f_code.co_name]
        parser = argparse.ArgumentParser(
            description=texts["description"],
            usage=texts["usage"],
        )

        parser.add_argument(
            "--new",
            action="store_true",
            help="flag to indicate a new deal not known to the system"
        )

        parser.add_argument(
            "deal_name",
            help="name of the deal you want to switch to as the active deal"
        )

        args = parser.parse_args(sys.argv[2:])

        if args.new:
            print(f"[Simulated] Created new deal in database: {args.deal_name}")

        self.controller_instance.set_deal(args.deal_name)

        print(f"[Simulated] Active deal is now {args.deal_name}")

    def status(self):
        texts = self.texts[inspect.currentframe().f_code.co_name]
        parser = argparse.ArgumentParser(
            description=texts["description"],
            usage=texts["usage"],
        )

        print(f"current deal is foo")
        print(f"active document is baz")