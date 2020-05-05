from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from jwt_tools import generate_jwt


app = Flask(__name__)
api = Api(app)

@app.route("/integritycheck")
def main():
    return "Flask has been succesfully deployed using nginx"


class CreateJWT(Resource):
    def get(self):
        return generate_jwt()


api.add_resource(CreateJWT, "/jwt/create")