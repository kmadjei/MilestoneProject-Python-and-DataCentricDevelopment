# accessing modules required to run the app
import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from re import search
from markupsafe import escape
from datetime import datetime
import json
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


@app.route('/recipes', methods=["GET", "POST"])
def get_recipes():

    # form submission
    if request.method == 'POST':

        # validates add-category form
        if 'add-category' in request.form.keys():        
            add_category = {
                'name': request.form.get('recipe-category'),
                'img_url': request.form.get('image-url')
            }

            # adds category to db
            mongo.db.food_categories.insert_one(add_category)
            flash(f'Successfully added {add_category["name"]}')

        # validates edit-category form
        if 'edit-category' in request.form.keys():        
            edit_category = {
                'name': request.form.get('recipe-category'),
                'img_url': request.form.get('image-url')
            }
            category_id = {"_id": ObjectId(request.form.get('category_id'))}

            # edit category in db
            mongo.db.food_categories.update_one(category_id, {'$set': edit_category})
            flash(f'Successfully edited {edit_category["name"]}')

         # deletes selected category
        if 'delete-category' in request.form.keys():

            category_id = {"_id": ObjectId(request.form.get('category_id'))}
            mongo.db.food_categories.delete_one(category_id)
            flash(f'Successful Deletion')

    # get food category data from db
    categories1 = list(mongo.db.food_categories.find({}))

    # Build new list that only dispplays food_categories with listed recipes
    categories2 = [{}]
    row2 = 0
    for row in range(len(categories1)):

        display_category_query = list(mongo.db.food.find({'category': categories1[row]['name']}))

        # filter through user data to protect against html injections
        if len(display_category_query) > 0:
            categories2[row2]['_id'] = categories1[row]['_id']
            categories2[row2]['name'] = filter_data(categories1[row]['name'])
            categories2[row2]['img_url'] = filter_data(categories1[row]['img_url'])
            row2 +=1
        print()
        print(categories2)


    return render_template('recipes.html', categories1 = categories1, categories2 = categories2)


@app.route('/recipes/list')
def show_all_recipes():
    recipes = list(mongo.db.food.find())
    return render_template('show_recipes.html', recipes=recipes)

# @app.route('/recipes/list/<name>')
# def recipe_details():
#    pass


@app.route('/add_recipe', methods=["GET", "POST"])
def add_recipe():
    categories = list(mongo.db.food_categories.find())

    # validate recipe form submitted
    if request.method == 'POST':
        # build list for recipe preparation steps
        recipe_prep = []
        for input in request.form:
            if search("prep", input):
                prep_step = request.form[input]
                recipe_prep.append(prep_step)
        # convert to a set element
        #recipe_prep = recipe_prep
     
        # create ingredients list
        ingredients = request.form.get('ingredients').split(",")
        # filter out user input data for ingredients - protect against injections
        #list_of_ingredients = set(map(filter_data, ingredients)) 

        recipe_name = request.form.get('recipe_name')
        recipe_category = request.form.get('category')
        recipe_author = request.form.get('author')
        recipe_img_url = request.form.get('img_url')
        created_at = datetime.now().strftime("%x")

        recipe_details = {
            'name': recipe_name,
            'category': recipe_category,
            'image_url': recipe_img_url,
            'author': recipe_author,
            'ingredients': ingredients,
            'preparations': json.dumps(recipe_prep),
            'created_at': created_at
        }

        mongo.db.food.insert_one(recipe_details)

        # user feedback - flash message
        flash("Recipe Successfully Added")
        
        #redirect to listed recipes
        return redirect(url_for("show_all_recipe"))          

    return render_template('add_recipe.html', categories=categories)


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
