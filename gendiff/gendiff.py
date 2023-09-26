#!usr/bin/env python3
from gendiff.parser import parse
from gendiff.diff import get_difference_between_files
from gendiff.formatters.format import format_diff


def generate_diff(file_path1, file_path2, format='stylish'):
    file1_data, file2_data = (
        get_file_data(file_path1),
        get_file_data(file_path2)
    )
    difference = get_difference_between_files(file1_data, file2_data)
    final_result = format_diff(difference, format)
    return final_result


def get_file_data(file_path):
    file_extension = get_file_extension(file_path)
    with open(file_path, 'r') as file:
        file_data = parse(file, file_extension)
    return file_data


def get_file_extension(file_path):
    file_extension = file_path[file_path.rfind('.')+1:]
    return file_extension
