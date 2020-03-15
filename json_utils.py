import json


def read_json_file(path):
    """Returns dict from json file."""
    with open(path, 'r', encoding='utf-8') as f:
        json_dict = json.load(f)
    return json_dict
