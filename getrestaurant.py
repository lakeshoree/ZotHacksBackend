import requests
from classifyimage import classify_image

##Spoonacular API Call
url = "https://api.spoonacular.com/food/images/classify"

##function to return list of restaurants
def getrestaurantbykeyword(location, term):

##Yelp API Call
    url = "https://api.yelp.com/v3/businesses/search"

    # Looks for these quereys
    querystring = {"location":location,"term":term}

    payload = ""
    headers = {
        "User-Agent": "insomnia/8.3.0",
        "Authorization": "Bearer yXQmgWc4Q-N5WmeUxzdPqBDZjREdJQid7ihXgqJWH7eF2h-JN0lSkFKSWLwWEB2KDT8YllJ_pdkmN_XwUtxLn_PRksjqKxZS8HxoO12CQjxH-PyJGnxhzHaUf4FGZXYx"
    }

    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

    return response.json()

if  __name__ == 'main':
    dictionary = classify_image(url)
    keyword = dictionary['category']

    result = getrestaurantbykeyword()

    print(result)
