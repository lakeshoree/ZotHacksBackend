import requests

api_url = "https://api.spoonacular.com/food/images/classify"

""" Makes a call to Spoonacular Image Classifier API, accepts an image URL as a parameter, returns category image belongs to"""

def classify_image(url):
    #try:
    #image_url = str(input("Enter a URL: "))
    querystring = {"apiKey":"68c4137f70bc4735adb96741342cf5f6","imageUrl":url}

    payload = ""
    headers = {"User-Agent": "insomnia/8.3.0"}

    response = requests.request("GET", api_url, data=payload, headers=headers, params=querystring)
   # except: 
        #print("Invalid URL. ")

    return response.json()

if __name__ == 'main':
    classify_image()

