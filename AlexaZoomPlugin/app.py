from flask import Flask, request, jsonify
from flask_restful import Api, Resource


app = Flask(__name__)

@app.route("/integritycheck")
def main():
    return "Flask has been succesfully deployed using nginx"