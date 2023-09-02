import json
import yaml


def parse_json(path):
    with open(path, 'r') as file:
        return json.load(file)


def parse_yml(path):
    with open(path, 'r') as file:
        return yaml.safe_load(file)


def parse(file1, file2):
    if file1.endswith('.json'):
        file1 = parse_json(file1)
    elif file1.endswith('.yml') or file1.endswith('.yaml'):
        file1 = parse_yml(file1)

    if file2.endswith('.json'):
        file2 = parse_json(file2)
    elif file2.endswith('.yml') or file2.endswith('.yaml'):
        file2 = parse_yml(file2)

    return file1, file2
