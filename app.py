from flask import Flask, jsonify, request
from flask_restful import Api, Resource
import base64

app = Flask(__name__)
api = Api(app)

class Segment(Resource):
    def post(self):
        postedData = request.get_json()
        rg = postedData["rg"]

        image =  open("seg.jpg","rb")
        seg_image = image.read()
        en_seg_image = base64.b64encode(seg_image).decode()
        retMap = {
            "Image": en_seg_image,
            "Status Code" : 200
        }
        return jsonify(retMap)

api.add_resource(Segment, "/segment")

@app.route('/')
def hello_jaga():
    return "Hello Jaga"

if __name__ == "__main__":
    app.run(debug=True)