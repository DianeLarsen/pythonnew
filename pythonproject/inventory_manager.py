import json

def load_inventory(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}  # Return an empty dictionary if the file doesn't exist

def save_inventory(filename, inventory):
    with open(filename, 'w') as file:
        json.dump(inventory, file, indent=4)
