# accessing modules required to run the app
import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from re import search
from markupsafe import escape
if os.path.exists("env.py"):
    import env

# Initialize instance of the Flask App 
app = Flask(__name__)

# set the config Key & values of the flask app
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

# gets secret key for Flash message object
app.secret_key = os.environ.get("SECRET_KEY")

# connects the flask app to the MongoDB server
mongo = PyMongo(app)


# binds the home function to the default url route / view page
@app.route("/")
def home():
    return render_template('home.html')


@app.route('/recipes')
def get_recipes():
    categories = list(mongo.db.food_categories.find())
        
    #loop to find list of matching categories and display none for 0 list

    return render_template('recipes.html', categories = categories)


# @app.route('/recipes/list')
# def show_all_recipe():
#     pass


@app.route('/add_recipe',  methods=["GET", "POST"])
def add_recipe():
    categories = list(mongo.db.food_categories.find())

    if request.method == 'POST':

        # build list for recipe preparation steps
        recipe_prep = []
        for input in request.form:
            if search("prep", input):
                prep_step = filter_data(request.form[input])
                recipe_prep.append(prep_step)
        print(recipe_prep)
        print()
               

    return render_template('add_recipe.html', categories = categories)


def filter_data(input):
    '''Trim white space and Protect against injection attacks'''
    input = escape(input.strip())
    return input


# @app.route('/recipes/<category>')
# def get_food_category(category):
#     pass

# @app.route('/delete_category')
# def delete_category():
#     pass

# @app.route('/edit_category')
# def delete_category():
#     pass

# @app.route('/delete_recipe')
# def edit_recipe():
#     pass

# @app.route('/edit_recipe')
# def edit_recipe():
#     pass


# runs the flask application as the main module
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
