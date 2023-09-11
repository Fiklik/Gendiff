from . import stylish, plain


def format_diff(diff, format='stylish'):
    if format == 'stylish':
        formatted_diff = stylish.get_stylish_output(
            diff,
            replacer=' ',
            spaces_count=1,
            depth=1
        )

        return formatted_diff

    elif format == 'plain':
        formatted_diff = plain.get_plain_output(
            diff
        )

        return formatted_diff
