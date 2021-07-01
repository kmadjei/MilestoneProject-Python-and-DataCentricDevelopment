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
def get_recipe_categories():

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
            flash(f'Successfully deleted category')

    # get food category data from db
    categories1 = list(mongo.db.food_categories.find())
    display_category_query = list(mongo.db.food.find({'category': 'Breakfast'}))

    # Build new list that only displays food_categories with listed recipes
    categories2 = [{}]
    row2 = 0 
    for row in range(len(categories1)):

        display_category_query = list(mongo.db.food.find({'category': categories1[row]['name']}))
        
        # filter through user data to protect against html injections
        if len(display_category_query) > 0:
            categories2[row2]['_id'] = categories1[row]['_id']
            categories2[row2]['name'] = filter_data(categories1[row]['name'])
            categories2[row2]['img_url'] = filter_data(categories1[row]['img_url'])
            if categories2[row2 - 1]['_id'] != categories1[row]['_id']:
                # increments row2 if previous category is not the same one
                row2 +=1
            else:
                continue
                
        print()
        print(categories2)
            #categories2 = categories2

    return render_template('recipes.html', categories1 = categories1, categories2 = categories2)


@app.route('/recipes/list', methods=["GET", "POST"])
def show_all_recipes():
   
    if request.method == 'POST':
        # deletes selected recipe from db
        if 'delete-recipe' in request.form.keys():

            recipe_id = {"_id": ObjectId(request.form.get('recipe_id'))}
            mongo.db.food.delete_one(recipe_id)
            flash('The recipe has been successfully deleted')

    recipes = list(mongo.db.food.find())
    return render_template('show_recipes.html', recipes=recipes)


@app.route('/add_recipe', methods=["GET", "POST"])
def add_recipe():

    # validate recipe form submitted
    if request.method == 'POST':
        # build list for recipe preparation steps
        recipe_prep = []
        for input in request.form:
            if search("prep", input):
                prep_step = request.form[input]
                recipe_prep.append(prep_step)

        recipe_details = {
            'name': request.form.get('recipe_name'),
            'category': request.form.get('category'),
            'image_url': request.form.get('img_url'),
            'author': request.form.get('author'),
            'prep_time': request.form['prep_time'],
            'cook_time': request.form['cook_time'],
            'servings': request.form['servings'],
            'description': request.form['description'],
            'ingredients': request.form.get('ingredients').split("\n"),
            'preparations': recipe_prep,
            'created_at': datetime.now().strftime("%x")
        }
        # adds recipe to db
        mongo.db.food.insert_one(recipe_details)
        # user feedback - flash message
        flash("Recipe Successfully Added")
        
        #redirect to listed recipes
        return redirect(url_for("show_all_recipes"))

    # get food menu category from db
    categories = list(mongo.db.food_categories.find())
    return render_template('add_recipe.html', categories=categories)


@app.route('/recipes/<menu>/<product_page>') 
def recipe_details(menu, product_page):

    search_query = {'name': product_page, 'category': menu}
    # get recipe data from db
    recipe = list(mongo.db.food.find(search_query))

    return render_template('product_page.html', recipe = recipe, filter_data = filter_data)




@app.route('/recipes/<menu>/<product_page>/edit', methods=["GET", "POST"])
def edit_recipe(menu, product_page):  
    # validate form submitted
    if request.method == 'POST':

        print() 
        print(product_page)
        print('fuck 1 u from Edit_recipt function')  
        print() 
        # executes if user clicks edit_recipe from product_page
        if 'edit_selected' in request.form.keys():
            # retrieve data from db
            recipe_id = {"_id": ObjectId(request.form.get('recipe_id'))}
            recipe = list(mongo.db.food.find(recipe_id)) 
            categories = list(mongo.db.food_categories.find())
            
            #print(recipe[0]['preparations'])
            return render_template('edit_recipe.html', recipe = recipe, categories =  categories)

        
        # executes when user submits form to update recipe
        if 'edit-recipe' in request.form.keys():
            print('fuck u 2 from edit-recipe -form submitting.....')
            #gets recipe preparation data
            recipe_prep = []
            for input in request.form:
                if search("prep", input):
                    prep_step = filter_data(request.form[input])
                    recipe_prep.append(prep_step)

            print('fuck u 3 recipe_prep array')
            recipe_info = {
                'name': request.form.get('recipe_name'),
                'category': request.form.get('category'),
                'image_url': request.form.get('img_url'),
                'author': request.form.get('author'),
                'prep_time': request.form['prep_time'],
                'cook_time': request.form['cook_time'],
                'servings': request.form['servings'],
                'description': request.form['description'],
                'ingredients': request.form.get('ingredients').split("\n"),
                'preparations': recipe_prep
            }
            print('fuck u 4 recipe edit schema')
            recipe_id = {"_id": ObjectId(request.form.get('recipe_id'))}
        
            # update recipe in db
            mongo.db.food.update_one(recipe_id, {'$set': recipe_info})
            # user feedback message
            flash(f'Successfully edited --> {recipe_info["name"]}')
            
            recipe = list(mongo.db.food.find(recipe_id))
            print('fuck u 5 form sent to DB')
            menu = recipe[0]['category']
            product_page = recipe[0]['name']

            # redirect to product_page.html after form submission
            return redirect(url_for("recipe_details", menu=menu, product_page=product_page)) 


def filter_data(input):
    '''Trim white space and Protect against injection attacks'''
    input = escape(input.strip())
    return input





# runs the flask application as the main module
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
