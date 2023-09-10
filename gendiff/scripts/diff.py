def get_unique_sorted_keys_list(dict1, dict2):
    unique_keys = set(dict1.keys() | dict2.keys())
    keys_list = list(unique_keys)
    keys_list.sort()

    return keys_list


def get_difference_between_files(data1, data2):

    keys = get_unique_sorted_keys_list(data1, data2)

    diff_list = []
    for key in keys:

        if key not in data2:
            diff_list.append({
                'key': key,
                'change': 'deleted',
                'value': data1[key]
            })

        elif key not in data1:
            diff_list.append({
                'key': key,
                'change': 'new',
                'value': data2[key]
            })

        elif key in data1 and key in data2:

            if isinstance(data1[key], dict) \
                    and isinstance(data2[key], dict):
                diff_list.append({
                    'key': key,
                    'change': 'node',
                    'children': get_difference_between_files(
                        data1[key], data2[key]
                    )
                })

            elif data1[key] != data2[key]:
                diff_list.append({
                    'key': key,
                    'change': 'updated',
                    'old_value': data1[key],
                    'new_value': data2[key]
                })

            elif data1[key] == data2[key]:
                diff_list.append({
                    'key': key,
                    'change': 'unchanged',
                    'value': data1[key]
                })

    return diff_list
