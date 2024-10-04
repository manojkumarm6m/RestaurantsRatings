# utils/json_handler.py

import json


def save_to_json(data, city):
    """
    Save the restaurant data to a JSON file.
    """
    filename = f"{city}_top_restaurants.json"

    try:
        with open(filename, 'w') as json_file:
            json.dump(data, json_file, indent=4)
        print(f"Data saved to {filename}")
    except Exception as e:
        print(f"Error saving data to file: {e}")
