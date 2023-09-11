import argparse
from .parser import parse


def parse_command_line():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument(
        '-f', '--format',
        type=str,
        default='stylish',
        const='stylish',
        nargs='?',
        help='set format of output (default: "stylish")'
    )
    args = parser.parse_args()
    path_to_file1 = parse(args.first_file)
    path_to_file2 = parse(args.second_file)
    format = args.format

    return path_to_file1, path_to_file2, format
