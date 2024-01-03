from renardo.boot_supercollider import boot_supercollider
import argparse
import time


def launch(args):

    # if args.cli:
    # if args.dir:
    #     try:
    #         # Use given directory
    #         FoxDotCode.use_sample_directory(args.dir)
    #     except OSError as e:
    #         # Exit with last error
    #         import sys, traceback
    #         sys.exit(traceback.print_exc(limit=1))

    # if args.startup:
    #     try:
    #         FoxDotCode.use_startup_file(args.startup)
    #     except OSError as e:
    #         import sys, traceback
    #         sys.exit(traceback.print_exc(limit=1))

    # if args.no_startup:
    #     FoxDotCode.no_startup()

    if args.boot:
        boot_supercollider()
        time.sleep(15)

    from renardo_lib.lib import FoxDotCode, handle_stdin
    if args.pipe:
        # Just take commands from the CLI
        handle_stdin()
    else:
        # Open the GUI
        from FoxDotEditor.Editor import workspace
        FoxDot = workspace(FoxDotCode).run()


def entrypoint():
        parser = argparse.ArgumentParser(
            prog="renardo", 
            description="Live coding with Python and SuperCollider", 
            epilog="More information: https://renardo.org/"
        )

        parser.add_argument('-p', '--pipe', action='store_true', help="run FoxDot from the command line interface")
        parser.add_argument('-d', '--dir', action='store', help="use an alternate directory for looking up samples")
        parser.add_argument('-s', '--startup', action='store', help="use an alternate startup file")
        parser.add_argument('-n', '--no-startup', action='store_true', help="does not load startup.py on boot")
        parser.add_argument('-b', '--boot', action='store_true', help="Boot SuperCollider from the command line")

        args = parser.parse_args()

        launch(args)
