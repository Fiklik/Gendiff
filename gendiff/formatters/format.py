from . import stylish


def format_diff(diff, format='stylish'):
    if format == 'stylish':
        result = stylish.get_stylish_output(
            diff,
            replacer=' ',
            spaces_count=1,
            depth=1
        )

        return result
