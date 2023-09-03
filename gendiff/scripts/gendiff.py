#!usr/bin/env python3
from . import cli, diff
import itertools


def get_unique_sorted_keys_list(dict1, dict2):
    unique_keys = set(dict1.keys() | dict2.keys())
    keys_list = list(unique_keys)
    keys_list.sort()

    return keys_list


def generate_diff(file1, file2, format='stylish'):
    format = format
    keys = get_unique_sorted_keys_list(file1, file2)
    result = '{\n'
    for key in keys:
        if key in file1 and key in file2:
            if file1.get(key) != file2.get(key):
                result += f'  - {key}: {str(file1[key])}\n'
                result += f'  + {key}: {str(file2[key])}\n'
            else:
                result += f'    {key}: {str(file1[key])}\n'
        elif key in file1 and key not in file2:
            result += f'  - {key}: {str(file1[key])}\n'
        elif key in file2 and key not in file1:
            result += f'  + {key}: {str(file2[key])}\n'
    result += '}'
    return result


def main():
    file1, file2 = cli.parse_command_line()
    difference = diff.difference_between_files(file1, file2)
    # difference = generate_diff(file1, file2)
    result = itertools.chain(difference)
    print(*result, sep='\n')


if __name__ == '__main__':
    main()
