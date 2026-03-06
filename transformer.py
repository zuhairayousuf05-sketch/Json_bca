
def flatten_json(data, parent_key='', sep='_'):

    items = {}

    for k, v in data.items():

        new_key = parent_key + sep + k if parent_key else k

        if isinstance(v, dict):
            items.update(flatten_json(v, new_key, sep=sep))
        else:
            items[new_key] = v

    return items


def unflatten_json(data):

    result = {}

    for key, value in data.items():

        parts = key.split('_')
        d = result

        for part in parts[:-1]:
            if part not in d:
                d[part] = {}
            d = d[part]

        d[parts[-1]] = value

    return result
