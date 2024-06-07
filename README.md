# datafun-05-sql project

## Overview
Project 5 integrates Python and SQL, focusing on database interactions using SQLite. This project introduces logging, a useful tool for debugging and monitoring projects, and involves creating and managing a database, building a schema, and performing various SQL operations, including queries with joins, filters, and aggregations.

## Start a New Project in GitHub & Clone it 
In your browser, create a GitHub project repository with a default README.md.
Clone your new repository down to your machine where you want your root project folder to be by running the following:
```
git clone URL
```
 
## Add .gitignore file
Use VS Code to create a new file with the name .gitignore and add at least the following entries:
```
# Ignore project virtual environment in the .venv folder
.venv/

# Ignore Visual Studio Code settings in the .vscode folder
.vscode/
```

## Add empty requirements.txt file
Create an empty txt file in your root project folder

## Edit README.md
Edit your README.md file to record your commands, process, and notes. Use one hash space for the title.

## Git Add / Commit / Push to GitHub
Use your terminal to add your files to source control, commit your changes to git, and push them up to GitHub by running the following:
```
git add .
git commit -m "initial commit"
git push origin main
```

## Create and Activate Project Virtual Environment
Use your terminal to create your project virtual environment by running venv as a Python module (python -m venv) and providing the name the destination folder for the project virtual environment as .venv by running the following:
```
py -m venv .venv
.venv\Scripts\Activate
```

## Install Packages into Active Environment
Windows command to install project dependencies:
```
py -m pip install jupyterlab numpy pandas matplotlib seaborn
```

## Update requirements.txt File
Run the following:
```
python -m pip freeze > requirements.txt
```

## Create Two Related CSV Data Files
On your machine, open your project repository folder in VS Code. In the root project repository folder, create a data folder. In this folder, create two CSV files; authors.csv and books.csv

## Git add / commit / push

## Create Databases
Create file "db_initialize_yourname.py"
Run the following:
```
import sqlite3
import pandas as pd
import pathlib

# Define the database file in the current root project directory
db_file = pathlib.Path("project.sqlite3")

def create_database():
    """Function to create a database. Connecting for the first time
    will create a new database file if it doesn't exist yet.
    Close the connection after creating the database
    to avoid locking the file."""
    try:
        conn = sqlite3.connect(db_file)
        conn.close()
        print("Database created successfully.")
    except sqlite3.Error as e:
        print("Error creating the database:", e)

def main():
    create_database()
    create_tables()

if __name__ == "__main__":
    main()
```

## Create Tables
Create file "create_tables.sql"
Run the following:
```
-- Start by deleting any tables if the exist already
-- We want to be able to re-run this script as needed.
-- DROP tables in reverse order of creation 
-- DROP dependent tables (with foreign keys) first

DROP TABLE IF EXISTS books;
DROP TABLE IF EXISTS authors;

-- Create the authors table 
-- Note that the author table has no foreign keys, so it is a standalone table

CREATE TABLE authors (
    author_id TEXT PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    year_born INTEGER
);

-- Create the books table
-- Note that the books table has a foreign key to the authors table
-- This means that the books table is dependent on the authors table
-- Be sure to create the standalone authors table BEFORE creating the books table.

CREATE TABLE books (
    book_id TEXT PRIMARY KEY,
    title TEXT,
    year_published INTEGER,
    author_id TEXT,
    FOREIGN KEY (author_id) REFERENCES authors(author_id)
);
```

# Start
Create file "db_operations_yourname.py"
In your Python file, create a docstring with a brief introduction to your project.

# Import Dependencies
Import each package just once near the top of the file.
```
import sqlite3
import pandas as pd
import pathlib
import logging
```

# Logging
Implement logging to enhance debugging and maintain a record of program execution.
```
import logging

# Configure logging to write to a file, appending new logs to the existing file
logging.basicConfig(filename='log.txt', level=logging.DEBUG, filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')

logging.info("Program started") # add this at the beginning of the main method
logging.info("Program ended")  # add this at the end of the main method
```

# Design a Schema
Document the schema design in your README.md.
```
def create_schema():
    """Create database schema"""
    try:
        with sqlite3.connect(db_file_path) as conn:
            schema_file = script_dir / "create_tables.sql"
            with open(schema_file, "r") as file:
                schema_script = file.read()
            conn.executescript(schema_script)
            logging.info("Schema created successfully.")
            print("Schema created successfully.")
    except sqlite3.Error as e:
        logging.exception("Error creating schema")
        print("Error creating schema:", e)
```

# SQL Operations
Implement SQL statements and queries to perform additional operations and use Python to execute your SQL statements.
Include the following SQL files:
create_tables.sql - create your database schema using sql
insert_records.sql - insert at least 10 additional records into each table.
update_records.sql - update 1 or more records in a table.
delete_records.sql - delete 1 or more records from a table.
query_aggregation.sql - use aggregation functions including COUNT, AVG, SUM.
query_filter.sql - use WHERE to filter data based on conditions.
query_sorting.sql - use ORDER BY to sort data.
query_group_by.sql - use GROUP BY clause (and optionally with aggregation)
query_join.sql - use INNER JOIN operation and optionally include LEFT JOIN, RIGHT JOIN, etc.

# Define Main Function for SQL Operations Script
Fun the following:
```
def main():
    create_schema()
    insert_data_from_csv()
    insert_records()
    update_records() 
    delete_records()
    query_aggregation()
    query_filter()
    query_sorting()
    query_group_by()
    query_join()    
    logging.info("All SQL operations completed successfully")

# Conditional Script Execution
Conditionally execute the main() function if this is the script being run
```
if __name__ == "__main__":
    main()
```
## Git add / commit / push


