from gendiff.scripts.gendiff import generate_diff
import pytest
from gendiff.scripts.parser import parse


@pytest.fixture
def comparison_file():
    with open('./tests/fixtures/file.txt') as result_file:
        result = result_file.read()
        print(result)
    # file1 = 'tests/fixtures/file1.json'
    # file2 = 'tests/fixtures/file2.json'
    file1, file2 = parse(
        'tests/fixtures/file1.json', 
        'tests/fixtures/file2.json'
    )
    gendiff_result = generate_diff(
        file1, file2
    )
    print(gendiff_result)
    return result, gendiff_result


def test_generate_diff(comparison_file):
    comparison_file_text, diff_result = comparison_file
    assert diff_result == comparison_file_text
