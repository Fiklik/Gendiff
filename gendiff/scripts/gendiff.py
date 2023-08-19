#!usr/bin/env python3
import argparse
import json


def generate_diff(file_path1, file_path2):
    file1 = json.load(open(file_path1))
    file2 = json.load(open(file_path2))

    keys = list(set(list(file1) + list(file2)))
    keys.sort()
    result = '{\n'
    for key in keys:
        if key in file1 and key in file2:
            if file1[key] != file2[key]:
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
    diff = generate_diff(args.first_file, args.second_file)
    print(diff)


if __name__ == '__main__':
    main()
