# import itertools
from gendiff.formatters.json import get_json_output
from gendiff.formatters.plain import get_plain_output
from gendiff.formatters.stylish import get_stylish_output


def format_diff(difference, format='stylish'):
    if format == 'stylish':
        formatted_diff = get_stylish_output(
            difference,
            replacer=' ',
            spaces_count=1,
            depth=1
        )

        return formatted_diff

    elif format == 'plain':
        formatted_diff = get_plain_output(
            difference
        )

        return formatted_diff

    elif format == 'json':
        formatted_diff = get_json_output(
            difference
        )

        return formatted_diff
