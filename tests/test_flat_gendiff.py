from gendiff.scripts.gendiff import generate_diff, get_files_from_paths
import pytest


@pytest.fixture
def comparison_file():
    with open('./tests/fixtures/file.txt') as result_file:
        result = result_file.read()
        print(result)
    file1, file2 = get_files_from_paths(
        './file1.json',
        './file2.json'
    ) 
    gendiff_result = generate_diff(
        file1, file2
    )
    print(gendiff_result)
    return result, gendiff_result


def test_generate_diff(comparison_file):
    comparison_file_text, diff_result = comparison_file
    assert diff_result == comparison_file_text
