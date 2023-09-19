REPLACER = ' '
SPACES_COUNT = 1


def stylize(array):
    output = get_stylish_output(array)
    return output


def get_stylish_output(array, depth=1):

    result = []

    for elem in array:

        indent_before_key = REPLACER * (SPACES_COUNT * depth * 4 - 2)
        indent_before_bracket = REPLACER * (SPACES_COUNT * depth * 4)

        match elem['change']:
            case 'deleted':
                formatted_str = format_value(elem['value'], depth)
                result.append(
                    f"{indent_before_key}- {elem['key']}: "
                    f"{formatted_str}"
                )

            case 'added':
                formatted_str = format_value(elem['value'], depth)
                result.append(
                    f"{indent_before_key}+ {elem['key']}: "
                    f"{formatted_str}"
                )

            case 'updated':
                old_formatted_str = format_value(elem['old_value'], depth)
                new_formatted_str = format_value(
                    elem['new_value'], depth
                )
                result.append(
                    f"{indent_before_key}- {elem['key']}: "
                    f"{old_formatted_str}"
                )
                result.append(
                    f"{indent_before_key}+ {elem['key']}: "
                    f"{new_formatted_str}"
                )

            case 'unchanged':
                formatted_str = format_value(elem['value'], depth)
                result.append(
                    f"{indent_before_key}  {elem['key']}: "
                    f"{formatted_str}"
                )

            case 'node':
                result.append(
                    f"{indent_before_key}  {elem['key']}: " + '{'
                )
                children = get_stylish_output(elem['children'], depth + 1)
                result.append(
                    f"{children}"
                    f"\n{indent_before_bracket}{'}'}"
                )

    if depth == 1:
        result = ['{'] + result + ['}']

    return '\n'.join(result)


def format_value(value, spaces_count=1, depth=1):

    if isinstance(value, dict):
        indent_before_key = REPLACER * (spaces_count * depth * 4 + 4)
        indent_before_bracket = REPLACER * (spaces_count * depth * 4)
        result = []
        result.append('{')

        for key in value:
            result.append(
                f"\n{indent_before_key}{key}: "
                f"""{format_value(
                    value[key],
                    spaces_count + 1
                )}"""
            )

        result.append(f"\n{indent_before_bracket}" + '}')
        return ''.join(result)

    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    if isinstance(value, (str, int)):
        return value

    return str(value)
