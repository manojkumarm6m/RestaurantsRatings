from api.google_places import RestaurantFinder


def main():
    """
    Main function to execute the script.
    """
    # Initialize the RestaurantFinder with your API key
    api_key = 'AIzaSyAaKHs7IXIafaJAuXIT8P_DMFlyXBCVH9I'
    finder = RestaurantFinder(api_key)

    # Step 1: Prompt the user to enter the city name
    city = input("Enter the name of the city: ").strip()

    # Step 2: Retrieve top 10 restaurants for the specified city
    restaurant_data = finder.get_top_restaurants(city)

    if restaurant_data:
        # Step 3: Save the restaurant data to a JSON file
        finder.save_restaurant_data(restaurant_data, city)


if __name__ == '__main__':
    main()
