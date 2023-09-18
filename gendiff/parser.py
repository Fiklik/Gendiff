import json
import yaml


def parse(file, file_extension):
    if file_extension == 'json':
        return json.load(file)
    elif file_extension == 'yml' or file_extension == 'yaml':
        return yaml.safe_load(file)
