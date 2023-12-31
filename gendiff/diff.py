def get_unique_sorted_keys_list(dict1, dict2):
    unique_keys = set(dict1.keys() | dict2.keys())
    keys_list = list(unique_keys)
    keys_list.sort()

    return keys_list


def get_difference(data1, data2):

    keys = get_unique_sorted_keys_list(data1, data2)

    diff = {}
    for key in keys:
        if key not in data2:

            diff[key] = {
                'change': 'deleted',
                'value': data1[key]
            }

        elif key not in data1:

            diff[key] = {
                'change': 'added',
                'value': data2[key]
            }

        elif key in data1 and key in data2:
            if isinstance(data1[key], dict) \
                    and isinstance(data2[key], dict):

                diff[key] = {
                    'change': 'node',
                    'children': get_difference(
                        data1[key], data2[key]
                    )
                }

            elif data1[key] != data2[key]:

                diff[key] = {
                    'change': 'updated',
                    'old_value': data1[key],
                    'new_value': data2[key]
                }

            elif data1[key] == data2[key]:
                diff[key] = {
                    'change': 'unchanged',
                    'value': data1[key]
                }

    return diff
