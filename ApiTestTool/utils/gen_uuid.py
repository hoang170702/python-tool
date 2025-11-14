import json
import uuid

from .json_parse import try_json_parse


def gen_id():
    return str(uuid.uuid4())



def inject_unique_id(context):
    raw_data = context.get('data')
    json_obj = try_json_parse(raw_data)

    if json_obj is None:
        return

    json_obj['id'] = gen_id()
    context['data'] = json.dumps(json_obj)