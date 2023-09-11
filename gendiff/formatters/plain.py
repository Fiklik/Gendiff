def get_plain_output(data, root=''):

    result = []
    parent = root

    for elem in data:
        if elem['change'] == 'added':
            parent += f"{str(elem['key'])}"
            result.append(
                f"""Property '{parent}' was added with value: {
                    format_value(
                        elem['value']
                    )
                }"""
            )
            parent = root

        elif elem['change'] == 'deleted':
            parent += f"{str(elem['key'])}"
            result.append(
                f"Property '{parent}' was removed"
            )
            parent = root

        elif elem['change'] == 'updated':
            parent += f"{str(elem['key'])}"
            result.append(
                f"Property '{parent}' was updated. "
                f"From {format_value(elem['old_value'])} "
                f"to {format_value(elem['new_value'])}"
            )
            parent = root

        elif elem['change'] == 'node':
            parent = f"{root}{elem['key']}."
            result.append(get_plain_output(
                elem['children'],
                parent
            ))
            parent = root

    return '\n'.join(result)


def format_value(data):

    if isinstance(data, dict):
        return '[complex value]'
    elif isinstance(data, bool):
        return str(data).lower()
    elif data is None:
        return 'null'

    return f"'{str(data)}'"
