from flask import Flask, jsonify, request
from flask_cors import CORS

from final import getrestaurantssimilartoimage
from getrestaurant import getrestaurantbykeyword
app = Flask(__name__)
CORS(app)

# instructions: - run the export once, and then flask run after each  ctrl+C
# export FLASK_RUN_PORT=5002
# flask run

# 127.0.0.1:5002/getRestaurants?location=irvine&imageUrl=https://upload.wikimedia.org/wikipedia/commons/thumb/6/64/Chicken_Nuggets.jpg/800px-Chicken_Nuggets.jpg

@app.route("/")
def hello():

	user_object ={"content1": "ZOT N' MUNCH'"}

	return jsonify(user_object)
	
# 127.0.0.1:5000/getRestaurants?location=irvine&imageUrl={url}
@app.route("/getRestaurants")
def hackfunc():

	location = request.args.get('location')
	imageUrl = request.args.get('imageUrl')

	# print(a, b)

	return getrestaurantssimilartoimage(location, imageUrl)


# 127.0.0.1:5000/getRestaurants?location=irvine&imageUrl={url}
@app.route("/getRestaurantsByFoodType")
def hackfunc1():

	location = request.args.get('location')
	foodType = request.args.get('foodType')

	# print(a, b)

	return getrestaurantbykeyword(location, foodType)
