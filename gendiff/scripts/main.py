from gendiff.gendiff import generate_diff
from gendiff.scripts.cli import parse_command_line


def main():
    file_path1, file_path2, format = parse_command_line()
    diff = generate_diff(file_path1, file_path2, format)
    return diff


if __name__ == '__main__':
    main()
