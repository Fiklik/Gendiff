import pytest
from gendiff.formatters.format import format_diff


@pytest.mark.usefixtures
def test_stylish_diff(nested_diff, stylish_text):
    assert format_diff(nested_diff) == stylish_text


@pytest.mark.usefixtures
def test_plain_diff(nested_diff, plain_text):
    assert format_diff(nested_diff, format='plain') == plain_text


@pytest.mark.usefixtures
def test_json_diff(nested_diff, json_text):
    assert format_diff(nested_diff, format='json') == json_text
