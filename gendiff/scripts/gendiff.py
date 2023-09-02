#!usr/bin/env python3
import argparse
from .parser import parse


def generate_diff(file1, file2):
    file1_keys = list(file1)
    file2_keys = list(file2)
    unique_keys = set(file1_keys + file2_keys)
    keys = list(unique_keys)
    keys.sort()
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
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    file1, file2 = parse(
        args.first_file, args.second_file
    )
    diff = generate_diff(file1, file2)
    print(diff)


if __name__ == '__main__':
    main()
