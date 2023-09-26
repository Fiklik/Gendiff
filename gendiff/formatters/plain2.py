def get_plain_output(data, root=''):

    result = []
    parent = root

    for key, val in data.items():
        match val['change']:
            case 'added':
                # if elem['change'] == 'added':
                parent += f"{str(key)}"
                result.append(
                    f"""Property '{parent}' was added with value: {
                        format_value(
                            val['value']
                        )
                    }"""
                )
                parent = root

            case 'deleted':
                # elif elem['change'] == 'deleted':
                parent += f"{str(key)}"
                result.append(
                    f"Property '{parent}' was removed"
                )
                parent = root

            case 'updated':
                # elif elem['change'] == 'updated':
                parent += f"{str(key)}"
                result.append(
                    f"Property '{parent}' was updated. "
                    f"From {format_value(val['old_value'])} "
                    f"to {format_value(val['new_value'])}"
                )
                parent = root

            case 'node':
                # elif elem['change'] == 'node':
                parent = f"{root}{key}."
                result.append(get_plain_output(
                    val['children'],
                    parent
                ))
                parent = root

    return '\n'.join(result)


def format_value(val):

    if isinstance(val, dict):
        return '[complex value]'
    elif isinstance(val, bool):
        return str(val).lower()
    elif val is None:
        return 'null'
    elif isinstance(val, int):
        return val

    return f"'{str(val)}'"
