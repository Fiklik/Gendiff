import pytest
import itertools
from gendiff.scripts.parser import parse
from gendiff.scripts.diff import get_difference_between_files
from gendiff.formatters.format import format_diff


@pytest.fixture
def comparison_file():
    with open('tests/fixtures/step_6_fixtures/file.txt') as example_file:
        example = example_file.read()
    # file1 = 'tests/fixtures/file1.json'
    # file2 = 'tests/fixtures/file2.json'
    file1 = parse('tests/fixtures/step_6_fixtures/file1.yml')
    file2 = parse('tests/fixtures/step_6_fixtures/file2.yml')
    difference = get_difference_between_files(file1, file2)
    result = list(itertools.chain(difference))
    for_print = format_diff(result)

    return example, for_print


def test_generate_diff(comparison_file):
    example_text, for_print = comparison_file
    assert for_print == example_text
