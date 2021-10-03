import sys
import argparse

import controller

class CLI:

    controller_instance = controller.WritAPI()

    description_text = "Description text here"
    usage_text = "Usage text here"

    def __init__(self):
        parser = argparse.ArgumentParser(
            description=self.description_text,
            usage=self.usage_text,
        )
        parser.add_argument("command", help="Subcommand to run")
        args = parser.parse_args(sys.argv[1:2])  # We want only sys.argv[1]. Default is sys.argv[1:]
        # args = parser.parse_args()
        print(f"{args.command=}")
        if not args.command:
            print(f"Unrecognized command")
            parser.print_help()
            exit(1)

        getattr(self, args.command)()  # Call the method matching the arg string.
            # TODO: Do this without getattr

    def typos(self):
        subdescription_text = "baz"
        subusage_text = "foo"

        print("[Simulated] Running typos checks")

        parser = argparse.ArgumentParser(
            description=subdescription_text,
            usage=subusage_text
        )

        parser.add_argument('-d')  # Default action is store value
        args = parser.parse_args(sys.argv[2:])
        print(f"{args.d=}")

    def add(self):
        subdescription_text = "bar"
        subusage_text = "corge"

        parser = argparse.ArgumentParser(
            description=subdescription_text,
            usage=subusage_text
        )
        parser.add_argument(
            'document',
            help="filename of the document to add"
        )
        args = parser.parse_args(sys.argv[2:])

        print(f"[Simulated] Added {args.document} to the active deal.")

    def checkout(self):
        subdescription_text = "garply"
        subusage_text = "grault"

        parser = argparse.ArgumentParser(
            description=subdescription_text,
            usage=subusage_text
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
        subdescription_text = "garply"
        subusage_text = "grault"

        print(f"current deal is foo")
        print(f"active document is baz")