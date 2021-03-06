"""
Command line interface to mymodule
"""
import argparse
from mypackage.mymodule import playRPS


def parse_command_line():
    "parses args for the playRPS funtion"

    # init parser and add arguments
    parser = argparse.ArgumentParser()

    # add long args
    parser.add_argument(
        "--throw",
        type= str,
        help="choose rock, paper or scissors",
        action="store")

    # parse args
    args = parser.parse_args()

    # check that user only entered one action arg
    if args.throw not in ['rock', 'paper', 'scissors']:
        raise SystemExit(
            "throw must be 'rock', 'paper' or 'scissors'")
    return args


def main():
    "run main function on parsed args"

    # get arguments from command line as a dict-like object
    args = parse_command_line()
    playRPS(args.throw)
