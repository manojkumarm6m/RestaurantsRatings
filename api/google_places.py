import requests

# API Setup (Replace with your Google Places API key)
API_KEY = 'AIzaSyAaKHs7IXIafaJAuXIT8P_DMFlyXBCVH9I'


def get_top_restaurants(city):
    """
    Function to fetch the top 10 restaurants in the specified city
    based on their ratings and reviews using Google Places API.
    """
    base_url = "https://maps.googleapis.com/maps/api/place/textsearch/json"

    # Construct the search query
    query = f"top restaurants in {city}"
    params = {
        'query': query,
        'type': 'restaurant',
        'key': API_KEY
    }

    # Send request to the Google Places API
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        # Parse the response JSON data
        data = response.json()

        if data.get('status') == 'OK':
            # Extract restaurant information from the response
            restaurants = data['results'][:10]  # Limit to top 10
            restaurant_data = {}

            for restaurant in restaurants:
                name = restaurant.get('name')
                rating = restaurant.get('rating')
                user_ratings_total = restaurant.get('user_ratings_total')

                # Add the restaurant details to the dictionary
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
