from flask import Flask, jsonify, request
from flask_restful import Api, Resource


app = Flask(__name__)
api = Api(app)

class Segment(Resource):
    def post(self):
        postedData = request.get_json()
        x = postedData["x"]
        y = postedData["y"]
        x = int(x)
        y = int(y)

        ret = x+y
        retMap = {
            "Sum": ret,
            "Status Code" : 200
        }
        return jsonify(retMap)

api.add_resource(Segment, "/segment")

@app.route('/')
def hello_jaga():
    return "Hello Jaga"

if __name__ == "__main__":
    app.run(debug=True)