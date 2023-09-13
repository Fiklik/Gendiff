#!usr/bin/env python3
from gendiff.scripts.cli import parse_command_line
from gendiff.scripts.diff import get_difference_between_files
from gendiff.formatters.format import format_diff


def main():
    file1, file2, format = parse_command_line()
    difference = get_difference_between_files(file1, file2)
    for_print = format_diff(difference, format)
    return for_print


if __name__ == '__main__':
    main()
