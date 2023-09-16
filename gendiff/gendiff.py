#!usr/bin/env python3
from gendiff.scripts.parser import parse
from gendiff.scripts.diff import get_difference_between_files
from gendiff.formatters.format import format_diff


def generate_diff(file_path1: str, file_path2: str, format='stylish') -> str:
    file1, file2 = parse(file_path1), parse(file_path2)
    difference = get_difference_between_files(file1, file2)
    final_result = format_diff(difference, format)
    print(final_result)
