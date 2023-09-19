import pytest
from gendiff.diff import get_difference_between_files
from gendiff.parser import parse


FILE1_PATH = 'tests/fixtures/files/file1.yml'
FILE1_EXTENSION = FILE1_PATH.split('.')[1]
FILE2_PATH = 'tests/fixtures/files/file2.json'
FILE2_EXTENSION = FILE2_PATH.split('.')[1]


@pytest.fixture
def nested_diff():
    with (
        open(FILE1_PATH, 'r') as file1,
        open(FILE2_PATH, 'r') as file2
    ):
        file1_data = parse(file1, FILE1_EXTENSION)
        file2_data = parse(file2, FILE2_EXTENSION)
    return get_difference_between_files(file1_data, file2_data)


@pytest.fixture
def stylish_text():
    path = 'tests/fixtures/stylish.txt'
    with open(path) as stylish_file:
        return stylish_file.read()


@pytest.fixture
def plain_text():
    path = 'tests/fixtures/plain.txt'
    with open(path) as plain_file:
        return plain_file.read()


@pytest.fixture
def json_text():
    path = 'tests/fixtures/json.txt'
    with open(path) as json_file:
        print(type(json_file))
        return json_file.read()
