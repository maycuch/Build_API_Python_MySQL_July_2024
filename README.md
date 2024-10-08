# Python API MySQL project

### What does this project do
- it is a recipe API built in Python using data from MySQL and user's input
- it extracts recipes from MySQL database into URL, where you can filter recipes by cuisine type
- it asks user if they would like to add a new recipe into database and if so it adds it into URL and MySQL database

### How to use it
- programmes you need to run this applicaton:
  - [Python](https://www.python.org/downloads/) software,
  - editor to run the code, eg. [PyCharm](https://www.jetbrains.com/pycharm/download/?section=windows),
  - interpreter for the MYSQL language [MySQL Community Server](https://dev.mysql.com/downloads/file/?id=526336),
  - application to see database data. e.g. [MySQL WorkBench](https://downloads.mysql.com/archives/workbench/)

 #### Instructions

- open Pycharm and run `app.py`; the URL is located in result window (http://127.0.0.1:5000);
- click on url which takes you to the homepage;
- add an endpoint 'recipes' to the url and you will be able to see all recipes from MySQL database *project_4*, table *recipes* (there are 4 recipes);
- you can filter recipes by cuisine type by using endpoint `.../recipes/<cuisine type>` (options based on recipes in MySQL database are american, middle eastern, central europe)
- go back to Pycharm and in terminal navigate into the folder `assignment-4-build-API` and type 'python main.py', you will be greeted with welcome message and a list of all recipes in the database
  ![main py screenshot](https://github.com/maycuch/CFG-Assignments/assets/104008913/e764091c-0ba8-4ad4-97dd-4dabec50a0a5)

- when asked if you want to add a recipe type 'y' and answer questions regarding a new recipe you want to add
  ![Screenshot main py user input](https://github.com/maycuch/CFG-Assignments/assets/104008913/c0bbca9e-65be-4b3c-bc39-c8988a7193e5)

- at this point a new recipe has been added to the URL and MySQL database; 
- MySQL result:
 ![Screenshot MySQL table with added recipe from user](https://github.com/maycuch/CFG-Assignments/assets/104008913/45891de7-8015-4bfd-b696-71aab7015de9)

- URL result:
![URL with newly added recipe](https://github.com/maycuch/CFG-Assignments/assets/104008913/c14243d2-ca79-4295-9662-0d7f5bc7095b)

