import requests
from utils.json_handler import save_to_json  # Import the save_to_json function


class RestaurantFinder:
    def __init__(self, api_key):
        """
        Initialize the RestaurantFinder with the provided Google Places API key.
        """
        self.api_key = api_key
        self.base_url = "https://maps.googleapis.com/maps/api/place/textsearch/json"

    def get_top_restaurants(self, city):
        """
        Fetch the top 10 restaurants in the specified city
        based on their ratings and reviews using Google Places API.
        """

        # Create a search query for the specified city.
        query = f"top restaurants in {city}"

        # Prepare parameters for the API request, including the search query, type, and API key.
        params = {
            'query': query,
            'type': 'restaurant',
            'key': self.api_key
        }

        # Send a GET request to the Google Places API to retrieve restaurant data based on the search query.
        response = requests.get(self.base_url, params=params)

        # Parse the response JSON for restaurant information.
        if response.status_code == 200:
            data = response.json()

            if data.get('status') == 'OK': # Ensure the API response is successful before extracting the top 10 restaurants.
                restaurants = data['results'][:10]  # Limit to top 10
                restaurant_data = {}

                # Iterate over the list of restaurants to extract their names, ratings, and total user ratings.
                for restaurant in restaurants:
                    name = restaurant.get('name')
                    rating = restaurant.get('rating')
                    user_ratings_total = restaurant.get('user_ratings_total')

                    # Store the restaurant's name as the key and its rating and total user ratings as values in the restaurant_data dictionary.
                    restaurant_data[name] = {
                        'rating': rating,
                        'user_ratings_total': user_ratings_total
                    }

                return restaurant_data
            else:
                print("Error: No results found for the specified city.")
                return None
        else:
            print(f"Error: API request failed with status code {response.status_code}")
            return None

    def save_restaurant_data(self, data, city):
        """
        Save restaurant data to a JSON file using the utility function.
        """
        save_to_json(data, city)  # Call the utility function to save data
