from flask import Flask, render_template, request, session, url_for, redirect, jsonify
# from flask_session import Session
# from resources import routes
from flask_restful import Api, Resource
from datetime import date

app = Flask(__name__)
app.config.from_object("config")
app.secret_key = app.config["SECRET_KEY"]
api = Api(app)
# routes.initialize_routes(api)
# Session(app)

@app.route("/")
def home():
    return "test passed !! "

if __name__ == "__main__":
    app.run(debug=True)