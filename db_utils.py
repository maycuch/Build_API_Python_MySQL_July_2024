import mysql.connector #pip install mysql-connector-python
from config import USER, PASSWORD, HOST


class DbConnectionError(Exception):
    pass

# function to connect to DB
def _connect_to_db(db_name):
    cnx = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        auth_plugin = 'mysql_native_password',
        database = db_name
    )
    return cnx

# EXTRACTING ALL DATA FROM MYSQL DATABASE 'project_4', table 'recipes AND CONVERTING IT TO LIST OF DICTIONARIES (EACH DICT REPRESENTS ONE RECIPE)-------------------------------------------
def get_all_recipes():
    db_connection = None
    try:
        db_name = 'project_4'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print(f"Connected to DB: {db_name}")

        query = """SELECT * FROM recipes"""
        cur.execute(query)
        result = cur.fetchall()  # this is a list with db records where each record is a tuple


        # changing result from list of tuples to a list of dictionaries

        element_list = [] #this is going to be a list of lists instead of list of tuples
        for element in result:
            element_list.append(list(element))

        #creating a list of keys to be used for a dictionaries (matching to headers in a table recipes in MySQL database project_4)
        keys = ('label','url','meal_type','cuisine_type','calories','minutes_to_cook','no_of_serving')

        data = []
        for i in element_list: # iterating over each recipe in element_list
            dict = {}
            for j in range(0,len(keys)):
                dict[keys[j]] = i[j]
            data.append(dict)
        # print(f'data {data}')
            # print(f'Dict: {dict}')

        return data
        cur.close()


    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")



# SEARCH RECIPE BY ID / CUISINE TYPE (options are : american,middle eastern, central Europe) -------------------------------------------------------------------------------------------------------------
def search_recipes(cuisine,data):
    return [element for element in data if element['cuisine_type'] == cuisine]


# ADD NEW RECIPE TO MYSQL DB  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def insert_new_recipe(new_recipe):
    db_connection = None
    try:
        db_name = 'project_4'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor() # cur talks to database
        print("Connected to DB: %s" % db_name) # the same as f"Connected to DB: {db_name}"

        # below '{}' and {} depending if I want string or number
        query = """INSERT INTO recipes ({}) VALUES ('{}', '{}', '{}', '{}', {}, {}, {})""".format(
            ', '.join(new_recipe.keys()), # this is for name of columns we are inserting into

            new_recipe['label'],
            new_recipe['url'],
            new_recipe['meal_type'],
            new_recipe['cuisine_type'],
            new_recipe['calories'],
            new_recipe['minutes_to_cook'],
            new_recipe['no_of_serving'],
        )
        cur.execute(query)
        db_connection.commit()  # VERY IMPORTANT, otherwise, rows would not be added or reflected in the DB!
        cur.close()

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")

    print("Record added to DB")


def main():
    get_all_recipes()
    search_recipes()
    # insert_new_recipe()



if __name__ == '__main__':
    main()