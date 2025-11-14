import json


def try_json_parse(text):
    try:
        return  json.loads(text)
    except (json.JSONDecodeError,TypeError ):
        return None