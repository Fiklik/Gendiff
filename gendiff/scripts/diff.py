def get_unique_sorted_keys_list(dict1, dict2):
    unique_keys = set(dict1.keys() | dict2.keys())
    keys_list = list(unique_keys)
    keys_list.sort()

    return keys_list


def get_difference_between_files(data1, data2):

    keys = get_unique_sorted_keys_list(data1, data2)

    diff_list = []
    for key in keys:
        diff_element = check_entry(key, data1, data2)
        diff_list.append(diff_element)

    return diff_list


def check_entry(key, data1, data2):

    if key not in data2:
        return create_dict(key, 'deleted', data1, data2)

    elif key not in data1:
        return create_dict(key, 'added', data1, data2)

    elif key in data1 and key in data2:
        if isinstance(data1[key], dict) \
                and isinstance(data2[key], dict):
            return create_dict(key, 'node', data1, data2)

        elif data1[key] != data2[key]:
            return create_dict(key, 'updated', data1, data2)

        elif data1[key] == data2[key]:
            return create_dict(key, 'unchanged', data1, data2)


def create_dict(key, change, data1=None, data2=None):

    match change:
        case 'added':
            dictionary = {
                'key': key,
                'change': change,
                'value': data2[key]
            }

        case 'deleted':
            dictionary = {
                'key': key,
                'change': change,
                'value': data1[key]
            }

        case 'updated':
            dictionary = {
                'key': key,
                'change': change,
                'old_value': data1[key],
                'new_value': data2[key]
            }

        case 'unchanged':
            dictionary = {
                'key': key,
                'change': change,
                'value': data1[key]
            }

        case 'node':
            dictionary = {
                'key': key,
                'change': 'node',
                'children': get_difference_between_files(
                    data1[key], data2[key]
                )
            }

    return dictionary
