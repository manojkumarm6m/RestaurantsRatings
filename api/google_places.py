import requests

# API Key for Google Places API
API_KEY = 'AIzaSyAaKHs7IXIafaJAuXIT8P_DMFlyXBCVH9I'


def get_top_restaurants(city):
    """
    Function to fetch the top 10 restaurants in the specified city
    based on their ratings and reviews using Google Places API.
    """

    # Base URL for the Google Places API Text Search
    base_url = "https://maps.googleapis.com/maps/api/place/textsearch/json"

    # Construct the search query for the Google Places API
    # The parameters dictionary includes:
    # - 'query': The search term to look for restaurants.
    # - 'type': Specifies the type of place to search for, in this case, 'restaurant'.
    # - 'key': The API key needed for authentication with the Google Places API.
    query = f"top restaurants in {city}"
    params = {
        'query': query,
        'type': 'restaurant',
        'key': API_KEY
    }

    # Send a GET request to the Google Places API to retrieve restaurant data based on the search query.
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        # Parse the response JSON data
        data = response.json()

        if data.get('status') == 'OK':
            # Extract restaurant information from the response
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
