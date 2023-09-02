import json
import yaml


def parse_json(path):
    with open(path, 'r') as file:
        return json.load(file)


def parse_yml(path):
    with open(path, 'r') as file:
        return yaml.safe_load(file)


def parse(path):
    if path.endswith('.json'):
        file = parse_json(path)
    elif path.endswith('.yml') or path.endswith('.yaml'):
        file = parse_yml(path)

    return file
