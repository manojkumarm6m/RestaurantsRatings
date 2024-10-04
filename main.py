# main.py

from api.google_places import get_top_restaurants
from utils.json_handler import save_to_json


def main():
    """
    Main function to execute the script.
    """
    # Step 1: Prompt the user to enter the city name
    city = input("Enter the name of the city: ").strip()

    # Step 2: Retrieve top 10 restaurants for the specified city
    restaurant_data = get_top_restaurants(city)

    if restaurant_data:
        # Step 3: Save the restaurant data to a JSON file
        save_to_json(restaurant_data, city)


if __name__ == '__main__':
    main()
