from flask import Flask, jsonify,request
from bson import json_util
from pymongo import MongoClient
import urllib 
from flask_cors import CORS 


app = Flask(__name__)
CORS(app)

# update this below line with monogdb cluster URL
client = MongoClient("mongodb+srv://admin:VIni2003@cluster0.mzevonl.mongodb.net/test")
db = client.db
images = db.images

@app.route('/images')
def index():
    all_images = list(images.find())
    print(all_images)
    response = json_util.dumps(all_images)
    return response

@app.route("/images/add")
def add():
    imageUrl = urllib.parse.unquote(request.args.get("image"))
    images.insert_one({"imageUrl": imageUrl, "likes": 0})
    return "success"
# @app.route('/images/add', methods = ['POST'])
# def addImages():
    

