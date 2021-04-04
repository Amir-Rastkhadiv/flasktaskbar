# Project/db_create.py

import sqlite3
from _config import DATABASE_PATH

# create a new database if the database isn't already exist
with sqlite3.connect(DATABASE_PATH) as connection:

# get the cursor object used to execute SQL coommands
    c = connection.cursor()
# create the table
    c.execute(""" CREATE TABLE tasks(task_id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, due_date TEXT NOT NULL,
        priority INT NOT NULL, status
        INTEGER NOT NULL)""")

# Insert dummy data into the table
    c.execute(
        'INSERT INTO tasks (name, due_date, priority ,status)'
        'VALUES("Finish this web blog", 6/04/2021, 1, 1)')
    c.execute(
        'INSERT INTO tasks (name, due_date, priority ,status)'
        'VALUES("Loose 4kg by April", 30/04/2021, 2, 1)')
