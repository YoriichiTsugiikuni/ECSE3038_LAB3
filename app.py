
from flask import Flask,request,jsonify
from flask_pymongo import PyMongo
from dotenv import load_dotenv
from marshmallow import Schema,fields,ValidationError
from bson.json_util import dumps
from json import loads 
from datetime import datetime 
import os

t=datetime.now()
mad_Thing={}
hinokami=[]
kagura=0

app=Flask(__name__)
app.config["MONGO_URI"]=os.getenv("MONGO_CONNECTION_STRING")
mongo=PyMongo(app)

#Profile
@app.route("/profile",methods=["GET"])
def home():
    return jsonify(mad_Thing)

@app.route("/profile",methods=["POST"])
def profPost():
    t=datetime.now()
    username=request.json["username"]
    role=request.json["role"]
    color=request.json["color"]
    user_object={
        "data":{
            "username":username,
            "color":color,
            "role":role,
            "last_updated":t
        }
    }
    global mad_Thing
    mad_Thing=user_object

    return jsonify(mad_Thing)

@app.route("/profile",methods=["PATCH"])
def profPatch():
    t=datetime.now()
    if 'username' in request.json:
        mad_Thing["data"]["username"]=request.json["username"]
        mad_Thing["data"]["last_updated"]=t
    
    if 'role' in request.json:
        mad_Thing["data"]["role"]=request.json["role"]
        mad_Thing["data"]["last_updated"]=t

    if 'color' in request.json:
        mad_Thing["data"]["color"]=request.json["color"]
        mad_Thing["data"]["last_updated"]=t
    
    return jsonify(mad_Thing)


#DATA-------------------------------------
class DataSchema(Schema):
    location = fields.String(required=True)
    lat = fields.Float(required=True)
    long = fields.Float(required=True)
    percentage_full = fields.Integer(required=True)

@app.route("/data",methods = ["GET"])
def dataGET(): 
    kokushi = mongo.db.tanks.find()
    juuni_kizuki = loads(dumps(kokushi))
    return jsonify(juuni_kizuki)

@app.route("/data",methods = ["POST"])
def dataPost():    
    request_dict = request.json
    try:
        added_Data =  DataSchema().load(request_dict)

    except ValidationError as err:
        return (err.messages,400) #produces this error is a nonexistent field/key is added

    data_document = mongo.db.tanks.insert_one(added_Data)
    data_id = data_document.inserted_id

    dataa = mongo.db.tanks.find_one({"_id":data_id})

    data_json = loads(dumps(dataa))
    return jsonify(data_json)


@app.route("/data/<ObjectId:id>",methods = ["DELETE"])
def dataDelete(id):
    result = mongo.db.tanks.delete_one({"_id": id})
    if result.deleted_count == 1:
        return {
            "success": True}
    else:
        return{ 
            "success": False},500



@app.route("/data/<ObjectId:id>",methods = ["PATCH"])
def dataPatch(id):
    request_dict = request.json
    try:
        patch_data = DataSchema(partial=True).load(request_dict)

    except ValidationError as err:
        return(err.messages,400)
    mongo.db.tanks.update_one({"_id": id}, {"$set": request.json})
    
    stress_out = mongo.db.tanks.find_one({"_id":id})
    muzan = loads(dumps(stress_out))
   
    return (muzan)
    


if __name__ =='__main__':
    app.run(
        debug=True,
        port=3000,
        host="0.0.0.0"
    )


