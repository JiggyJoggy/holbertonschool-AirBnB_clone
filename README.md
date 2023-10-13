# Airbnb Clone // Holberton School
![68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f696e7472616e65742d70726f6a656374732d66696c65732f686f6c626572746f6e7363686f6f6c2d6869676865722d6c6576656c5f70726f6772616d6d696e672b2f3236332f4842544e2d68626e622d46696e616c2e706e67](https://github.com/JiggyJoggy/holbertonschool-AirBnB_clone/assets/57630651/886cfce3-e16b-46d9-9d74-20e1a63fa107)
### This is the console portion of the Airbnb Clone created by Jagger Van Winkle

# Description
This repo is a command line interface that allows for debugging and stores data of the HBNB. This was written in Python using the **cmd** module.

# How to install
Write in your console this:
```
git clone https://github.com/JiggyJoggy/holbertonschool-AirBnB_clone.git
```
Ensure you have installed Python onto your machine.

# Running the program
Continuing in your console, write:
```
python3 console.py
```
or an alternative:
```
./console.py
```

# Commands
Use the command ``help`` followed by a command listed underneath here, for documentation of said command in the console.
* ``quit`` or ``EOF`` will exit the program.

# Commands that are not in the console
* ``create``: Creates a new instance
  * ``Syntax: create <class name>``

* ``show``: Displays given information of an instance; based on class name and id
  * ``Syntax: show <class name> <id>``

* ``destroy``: Destorys information of an instance; based on class name and id
  * ``Syntax: destroy <class name> <id>``

* ``all``: Displays all instances of a class or every class
  * ``Syntax: all <class name>``

* ``update``: Updates the class name and id
  * ``Syntax: update <class name> <id> <attribute name> <attribute value>``

# Tests
Currently, only test_base_model.py has been tested as there aren't other files within this build.
```
python3 -m unittest tests/test_models/test_base_model.py
```
