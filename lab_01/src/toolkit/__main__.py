import argparse
import sys

from .calculator import calculate_expression
from .converter import convert
from .errors import ToolkitError


def build_parser():
    parser = argparse.ArgumentParser(prog="toolkit")
    sub = parser.add_subparsers(dest="command", required=True)

    calc = sub.add_parser("calc")
    calc.add_argument("expression")

    conv = sub.add_parser("convert")
    conv.add_argument("value", type=float)
    conv.add_argument("--from", dest="from_unit", required=True)
    conv.add_argument("--to", dest="to_unit", required=True)
    return parser


def main():
    args = build_parser().parse_args()
    try:
        if args.command == "calc":
            result = calculate_expression(args.expression)
        else:
            result = convert(args.value, args.from_unit, args.to_unit)
        print(result)
    except ToolkitError as error:
        print(error, file=sys.stderr)
        return 2
    return 0 


sys.exit(main())