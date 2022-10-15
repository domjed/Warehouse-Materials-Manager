# warehouse-materials-manager

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

## General info
The app was written to facilite management of raw materials stored in a warehouse. Update of current stock status can be done by clicking "Add new material trade" button on main page. Afterwards, the user is redirected to form filling page. Once material data is provided and saved it can be wieved together with other historical entries. It can be done by clicking "Go to saved trades" button. The user has a possibility to sort and filter results as per miscelaneous criteria. If neccessary, provided input can be wieved again, modified or pernamently removed from database. For better app navigation, unfolding menu at the top of a page is added.
	
## Technologies
Project is created with:
* Python v3.10.4
* Flask v2.0.2
* Flask-SQLAlchemy v2.5.1
* HTML5
* Bootstrap v4.3.1 (https://getbootstrap.com/)

## Setup
The first thing to do is to clone the repository from GitHub:

```sh
$ git clone https://github.com/domjed/Warehouse-Materials-Manager.git
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ python -m venv venv
$ venv/Scripts/activate
```

Then install the dependencies:

```sh
(venv)$ pip install -r requirements.txt
```
Note the `(venv)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `venv`.

Once `pip` has finished downloading the dependencies, run flask server:

```sh
(venv)$ python main.py
```