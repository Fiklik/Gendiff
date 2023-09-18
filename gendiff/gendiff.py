#!usr/bin/env python3
from gendiff.parser import parse
from gendiff.diff import get_difference_between_files
from gendiff.formatters.format import format_diff


def generate_diff(file_path1, file_path2, format='stylish'):
    with (
        open(file_path1, 'r') as file1,
        open(file_path2, 'r') as file2
    ):
        file1_extension = file_path1.split('.')[1]
        file2_extension = file_path2.split('.')[1]

        file1_data = parse(file1, file1_extension)
        file2_data = parse(file2, file2_extension)

    difference = get_difference_between_files(file1_data, file2_data)
    final_result = format_diff(difference, format)
    return final_result
