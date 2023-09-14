import pytest
from gendiff.scripts.diff import get_difference_between_files
from gendiff.scripts.parser import parse


@pytest.fixture
def flat_diff():
    file1 = parse('tests/fixtures/flat_files/flat1.json')
    file2 = parse('tests/fixtures/flat_files/flat2.json')
    return get_difference_between_files(file1, file2)


@pytest.fixture
def nested_diff():
    file1 = parse('tests/fixtures/nested_files/nested1.yml')
    file2 = parse('tests/fixtures/nested_files/nested2.json')
    return get_difference_between_files(file1, file2)


@pytest.fixture
def flat_text():
    path = 'tests/fixtures/flat_files/flat.txt'
    with open(path) as flat_file:
        return flat_file.read()


@pytest.fixture
def flat_plain_text():
    path = 'tests/fixtures/flat_files/flat_plain.txt'
    with open(path) as flat_plain_file:
        return flat_plain_file.read()


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
        return json_file.read()
