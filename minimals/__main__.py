"""Command-line interface to Minimals."""

from . import hello

import argparse


def main():
    """The ``minimals`` program takes one argument: the minimal name.

    .. code-block:: sh

        minimals <name>

    """
    parser = argparse.ArgumentParser(
        prog="minimals",
        description="An amazing game with mini animals in it!",
    )
    parser.add_argument("name", help="Print a customized hello message")
    args = parser.parse_args()
    if args.name:
        print(hello(args.name))


if __name__ == "__main__":
    main()
