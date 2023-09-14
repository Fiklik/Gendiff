#!usr/bin/env python3
from gendiff.scripts.cli import parse_command_line
from gendiff.scripts.diff import get_difference_between_files
from gendiff.formatters.format import format_diff


def generate_diff():
    file1, file2, format = parse_command_line()
    difference = get_difference_between_files(file1, file2)
    final_result = format_diff(difference, format)
    return final_result


def main():
    return generate_diff()


if __name__ == '__main__':
    main()
