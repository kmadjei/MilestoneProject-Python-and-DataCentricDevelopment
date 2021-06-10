# accessing modules required to run the app
import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env

# Initialize instance of the Flask App 
app = Flask(__name__)

# set the config Key & values of the flask app
# app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
# app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
# gets secret key for Flash message object
app.secret_key = os.environ.get("SECRET_KEY")

# connects the flask app to the MongoDB server
# mongo = PyMongo(app)


# binds the home function to the default url route / view page
@app.route("/")
def home():
    return render_template('home.html')


@app.route('/recipes')
def get_recipes():
    return render_template('recipes.html')


# runs the flask application as the main module
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
