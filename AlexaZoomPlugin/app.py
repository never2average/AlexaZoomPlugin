from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from jwt_tools import generate_jwt
from list_meetings import listmeetings


app = Flask(__name__)
api = Api(app)

@app.route("/integritycheck")
def main():
    return "Flask has been succesfully deployed using nginx"


class CreateJWT(Resource):
    def get(self):
        return jsonify(generate_jwt())


class ListMeetings(Resource):
    def get(self):
        pageno = request.args["pageno"]
        userid = request.args["userid"]
        jwt = request.headers.get("Authorization")
        return jsonify(listmeetings(pageno, userid, jwt))


api.add_resource(CreateJWT, "/jwt/create")
api.add_resource(ListMeetings, "/meetings/list")

if __name__ == "__main__":
    app.run(debug=True)