import requests
import json


def fetch_all_recipes():
    result = requests.get(
        'http://127.0.0.1:5000/recipes',
        headers={'content-type': 'application/json'}
    )
    return result.json()

def display_database(records):
    # Print the names of the columns.
    print("{:<50} {:<15} {:<15} {:<15} {:<15} {:<15} {:<100} ".format(
        'recipe\'s title', 'meal type', 'cuisine type', 'calories', 'duration (min)', 'servings', 'url'))
    print('-' * 200)

    # print each data item.
    for item in records:
        print("{:<50} {:<15} {:<15} {:<15} {:<15} {:<15} {:<100} ".format(
            item['label'], item['meal_type'], item['cuisine_type'], item['calories'], item['minutes_to_cook'], item['no_of_serving'], item['url']
        ))


def add_new_recipe(label,url,meal_type,cuisine_type,calories,minutes_to_cook,no_of_serving):

    new_addition = {

        "label": label,
        "url": url,
        "meal_type": meal_type,
        "cuisine_type": cuisine_type,
        "calories": calories,
        "minutes_to_cook": minutes_to_cook,
        "no_of_serving": no_of_serving
    }

    result = requests.post(
        'http://127.0.0.1:5000/recipes',
        headers={'content-type': 'application/json'},
        data=json.dumps(new_addition)
    )
    result = add_new_recipe(label, url, meal_type, cuisine_type, calories, minutes_to_cook, no_of_serving)
    return ("POST request result:",result.json())
#

def run():
    print('############################')
    print('Hello fellow food enthusiast and welcome to our recipe database!')
    print('############################')
    print()
    print('Below you can find all recipes currently in the database')
    print()
    print()
    records = fetch_all_recipes()
    display_database(records)
    print()
    add_recipe = input('Would you like to add a new recipe into database (y/n)? ')
    print()
    add = add_recipe == 'y'

    if add:
        label = input('Enter the name of recipe: ')
        url = input('Enter the url of recipe:  ')
        meal_type = input('Enter the meal type (breakfast,lunch, snack, dinner, teatime) ')
        cuisine_type = input('Enter the cuisine type (american, central europe, middle eastern, italian, ...) ')
        calories = input('Enter calories per recipe: ')
        minutes_to_cook = input('Enter how long it takes to cook in whole minutes: ')
        no_of_serving = input('Enter number of portions: ')
        add_new_recipe(label,url,meal_type,cuisine_type,calories,minutes_to_cook,no_of_serving)
        print("Booking is Successful")
        print()

    print()
    print('See you soon!')

if __name__ == '__main__':
    run()