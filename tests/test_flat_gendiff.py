from gendiff.scripts.gendiff import generate_diff
import pytest


@pytest.fixture
def comparison_file():
    with open('./tests/fixtures/file.txt') as result_file:
        result = result_file.read()
        print(result)
    path1 = './file1.json'
    path2 = './file2.json'
    gendiff_result = generate_diff(
        path1, path2
    )
    print(gendiff_result)
    return result, gendiff_result


def test_generate_diff(comparison_file):
    comparison_file_text, diff_result = comparison_file
    assert diff_result == comparison_file_text
