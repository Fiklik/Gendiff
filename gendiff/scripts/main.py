#!usr/bin/env python3
from gendiff.gendiff import generate_diff
from gendiff.cli import parse_command_line


def main():
    file_path1, file_path2, format = parse_command_line()
    diff = generate_diff(file_path1, file_path2, format)
    print(diff)


if __name__ == '__main__':
    main()
