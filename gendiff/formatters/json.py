import json


def get_json_output(diff):
    return json.dumps(diff, indent=4)
