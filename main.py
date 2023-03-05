from flask import Flask, jsonify,request
from prediction import *
import os

app = Flask(__name__)

@app.route("/getPlantDisease",methods=["POST"])
def getPlantDiseaseData():
	if(request.method=="POST"):
		data = request.get_json()
		imageUrl = data["imageURL"]
		print(fetchResponse(imageUrl))
		return fetchResponse(imageUrl)
	else:
		return f"{request.method} will not work";

@app.route('/getPlantDiseases')
def getPlantDiseaseDatas():
    return jsonify({"Choo Choo": "Welcome to your Flask app 🚅"})

@app.route('/')
def index():
    return jsonify({"Choo Choo": "Welcome to your Flask app 🚅"})


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
