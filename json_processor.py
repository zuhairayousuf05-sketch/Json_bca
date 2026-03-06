
import json
from utils.validator import validate_json
from utils.transformer import flatten_json, unflatten_json
from utils.formatter import standardize_keys

def process_json(input_json):

    try:
        data = json.loads(input_json)
    except:
        return "Invalid JSON"

    data = standardize_keys(data)

    flat = flatten_json(data)

    structured = unflatten_json(flat)

    validation = validate_json(structured)

    output = {
        "clean_json": structured,
        "flattened_json": flat,
        "validation": validation
    }

    return json.dumps(output, indent=4)
