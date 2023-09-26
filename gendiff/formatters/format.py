from gendiff.formatters.json import get_json_output
from gendiff.formatters.plain2 import get_plain_output
from gendiff.formatters.stylish import stylize


def format_diff(difference, format='stylish'):
    if format == 'stylish':
        formatted_diff = stylize(difference)

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
