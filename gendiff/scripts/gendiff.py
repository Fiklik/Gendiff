#!usr/bin/env python3
from . import cli, diff
import itertools
from ..formatters.format import format_diff


def main():
    file1, file2 = cli.parse_command_line()
    difference = diff.get_difference_between_files(file1, file2)
    result = list(itertools.chain(difference))
    for_print = format_diff(result, format='stylish')

    return for_print


if __name__ == '__main__':
    main()
