
def validate_json(data):

    issues = []

    for key, value in data.items():

        if value is None:
            issues.append(f"{key} has null value")

        if type(value) == str and value.strip() == "":
            issues.append(f"{key} is empty string")

    if len(issues) == 0:
        return "JSON is valid"

    return issues
