import getrestaurant
from classifyimage import classify_image

test_url = "https://hips.hearstapps.com/hmg-prod/images/classic-buffalo-wings-horizontal-279-1547506155.jpg?crop=1xw:0.84375xh;center,top"

def getrestaurantssimilartoimage(location="irvine", url=test_url):

    classified_result = classify_image(url)

    print(classified_result)

    keyword = classified_result['category']
    return (getrestaurant.getrestaurantbykeyword(location, keyword))

if __name__ == 'main': 
    print(getrestaurantssimilartoimage())
