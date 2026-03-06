
def standardize_keys(data):

    new_data = {}

    for key, value in data.items():

        new_key = key.lower().replace(" ", "_")

        if isinstance(value, dict):
            value = standardize_keys(value)

        new_data[new_key] = value

    return new_data
