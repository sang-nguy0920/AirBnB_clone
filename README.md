# AirBnB_clone

## Project Description
- In this project we will be building the console and will manage file storage for our AirBnB_clone which is the first project of many in the saga of AirBnB.

## Execution
- Interactive mode:
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```
- Non-Interactive mode:
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

## Task Descriptions
- 0. File: README.md, AUTHORS : README and AUTHORS
- 1. GitHub repository: AirBnB_clone : Ensure all code is pep8 compliant
- 2. File: tests/ : Ensure all files, classes and functions have been properly tested with unittests
- 3. File: models/base_model.py, models/__init__.py, tests/ : Write a class BaseModel that defines all common attributes/methods for other classes
- 4. File: models/base_model.py, tests/ : Now it’s time to re-create an instance with this dictionary representation. Update models/base_model.py with: __init__(self, *args, **kwargs): Further Instructions on project page
- 5. File: models/engine/file_storage.py, models/engine/__init__.py, models/__init__.py, models/base_model.py, tests/ : Now we can recreate a BaseModel from another one by using a dictionary representation: convert the dictionary representation to a JSON string. JSON is a standard representation of a data structure. With this format, humans can read and all programming languages have a JSON reader and writer
- 6. File: console.py : A program called console.py that contains the entry point of the command interpreter: Using the cmd module
- 7. File: console.py : Update your command interpreter (console.py) to have these commands:
    - create
    - show
    - destroy
    - all
    - update
- 8. File: models/user.py, models/engine/file_storage.py, console.py, tests/ : A class User that inherits from BaseModel: Contains the public attributes:
    - email
    - password
    - first_name
    - last_name
    - Update FileStorage to manage correctly serialization and deserialization of User
    - Update your command interpreter (console.py) to allow show, create, destroy, update and all used with User
- 9. File: models/state.py, models/city.py, models/amenity.py, models/place.py, models/review.py, tests/ : All classes that inherit from BaseModel:
    - State
    - City
    - Amenity
    - Place
    - Review
- 10. File: console.py, models/engine/file_storage.py, tests/ : Update FileStorage to manage correctly serialization and deserialization of all our new classes: Place, State, City, Amenity and Review. Update your command interpreter (console.py) to allow those actions: show, create, destroy, update and all with all classes created previously.
- 11. File: console.py : Update your command interpreter (console.py) to retrieve all instances of a class by using: <class name>.all().
- 12. File: console.py : Update your command interpreter (console.py) to retrieve the number of instances of a class: <class name>.count().
- 13. File: console.py : Update your command interpreter (console.py) to retrieve an instance based on its ID: <class name>.show(<id>).
- 14. File: console.py : Update your command interpreter (console.py) to destroy an instance based on his ID: <class name>.destroy(<id>).
- 15. File: console.py : Update your command interpreter (console.py) to update an instance based on his ID: <class name>.update(<id>, <attribute name>, <attribute value>).
- 16. File: console.py : Update your command interpreter (console.py) to update an instance based on his ID with a dictionary: <class name>.update(<id>, <dictionary representation>).
- 17. File: tests/test_console.py : Write all unittests for console.py, all features! 
    - For testing the console, you should “intercept” STDOUT of it, we highly recommend you to use:
    ```
    with patch('sys.stdout', new=StringIO()) as f:
    HBNBCommand().onecmd("help show")
    ```
    - Otherwise, you will have to re-write the console by replacing precmd by default.
    Update test
