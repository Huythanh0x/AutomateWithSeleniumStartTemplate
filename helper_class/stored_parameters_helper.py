import json

def update_value_json(key, new_value, file_name = "parameters"):
    with open(f"{file_name}.json", 'r') as f:
        data = json.load(f)
    data[key] = new_value
    with open(f"{file_name}.json", 'w') as f:
        f.write(json.dumps(data, indent=4))

def get_stored_parameter(key, file_name = "parameters"):
    with open(f"{file_name}.json") as f:
        return json.load(f)[key]