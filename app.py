from flask import Flask, jsonify, request
from db_utils import get_all_recipes, search_recipes,insert_new_recipe

app = Flask(__name__)

# HOMEPAGE
@app.route('/')
def hello():
    return "<h4>Hello fellow food enthusiasts, welcome to our recipe database where you can browse and add your favourite recipes for the world to see!<h4> "

#CREATING AN ENDPOINT CONATINING ALL RECIPES FROM MYSQL DB 'project_4', TABLE 'recipes'
@app.route('/recipes')
def get_recipes():
    all_recipes = get_all_recipes()
    return jsonify(all_recipes) #converting dict to json

# CREATING AN ENDPOINT WHICH RETURNS DB RECIPES BASED ON CUISINE TYPE (american, middle eastern, central europe,...)
@app.route('/recipes/<cuisine>')
def get_recipes_by_cuisine(cuisine):
    recipe = search_recipes(cuisine, get_all_recipes()) # get_all_recipes() returns data
    return jsonify(recipe)

# ADDING A NEW RECIPE DEFINED BY USER FROM MAIN.PY
@app.route('/recipes', methods=['POST'])
def add_recipe():
    new_addition = request.get_json()
    insert_new_recipe(new_recipe=new_addition)

    return new_addition


if __name__ == '__main__':
    app.run(debug=True)