# utils/json_handler.py

import json


def save_to_json(data, city):
    """
    Save the restaurant data to a JSON file.
    """

    # Create a filename for the JSON file using the city name to store the top restaurant data.
    filename = f"{city}_top_restaurants.json"

    # Try to open the specified file for writing JSON data and handle any errors that occur.
    try:
        with open(filename, 'w') as json_file:
            json.dump(data, json_file, indent=4)
        print(f"Data saved to {filename}")
    except Exception as e:
        print(f"Error saving data to file: {e}")
