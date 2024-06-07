# project 5 start brooke richards
'''
This project focuses on database creation, 
schema development, and diverse SQL operations, 
including joins, filters, and aggregations.
'''


# import dependencies 
import sqlite3
import pandas as pd
import pathlib
import logging


# configure logging to write to a file
logging.basicConfig(filename='log.txt', level=logging.DEBUG, filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')
logging.info("Program started") # log the start of the program

# define the directory path where the script is located
script_dir = pathlib.Path(__file__).parent

# define the database file path
db_file = "project.db"

# combine the directory path and file name to get the database file path
db_file_path = script_dir / db_file

def create_schema():
    """Create database schema"""
    try:
        with sqlite3.connect(db_file) as conn:
            schema_file = pathlib.Path("create_tables.sql")
            with open(schema_file, "r") as file:
                schema_script = file.read()
            conn.executescript(schema_script)
            logging.info("Schema created successfully.")
    except sqlite3.Error as e:
        logging.exception("Error creating schema")
        print("Error creating schema:", e)

def insert_data_from_csv():
    """Insert records from CSV files into database"""
    try:
        author_data_path = script_dir / "data" / "authors.csv"
        book_data_path = script_dir / "data" / "books.csv"
        authors_df = pd.read_csv(author_data_path)
        books_df = pd.read_csv(book_data_path)
        with sqlite3.connect(db_file_path) as conn:
            # Use the pandas DataFrame to_sql() method to insert data
            # Pass in the table name and the connection
            authors_df.to_sql("authors", conn, if_exists="replace", index=False)
            books_df.to_sql("books", conn, if_exists="replace", index=False)
            logging.info("Data inserted sucessfully.")
            print("Data inserted successfully.")
    except (sqlite3.Error, pd.errors.EmptyDataError, FileNotFoundError) as e:
        logging.exception("Error inserting data from CSV")  # log the exception
        print("Error inserting data from CSV:", e)

def insert_records():
    """Function to read and execute SQL statements to insert data"""
    try:
        with sqlite3.connect(db_file) as conn:
            sql_file = "C:\\Users\\brichards\\Projects\\datafun-05-sql\\query_records.sql"
            with open(sql_file, "r") as file:
                sql_script = file.read()
            conn.executescript(sql_script)
            logging.info("Data inserted sucessfully.")
            print("Data inserted successfully.")
    except sqlite3.Error as e:
        logging.exception("Error inserting data from SQL")
        print("Error inserting data from SQL:", e)

def update_records():
    """Function to update one or more records in the authors table"""
    try:
        db_file = pathlib.Path("project.db")
        with sqlite3.connect(db_file) as conn:
            sql_file = pathlib.Path("update_records.sql")
            with open(sql_file, "r") as file:
                sql_script = file.read()
            conn.executescript(sql_script)
            logging.info("Records updated successfully.")
            print("Records updated successfully.")
    except sqlite3.Error as e:
        logging.exception("Error updating records")
        print("Error updating records:", e)

def delete_records():
    """Function to delete records from a table"""
    try:
        db_file = pathlib.Path("project.db")
        with sqlite3.connect(db_file) as conn:
            sql_file = pathlib.Path("delete_records.sql")
            with open(sql_file, "r") as file:
                sql_script = file.read()
            conn.executescript(sql_script)
            logging.info("Records deleted successfully.")
            print("Records deleted successfully.")
    except sqlite3.Error as e:
        logging.exception("Error deleting records")
        print("Error deleting records:", e)

def query_aggregation():
    """Function to perform aggregation functions on the books table"""
    try:
        db_file = pathlib.Path("project.db")
        with sqlite3.connect(db_file) as conn:
            sql_file = pathlib.Path("query_aggregation.sql")
            with open(sql_file, "r") as file:
                sql_script = file.read()
            cursor = conn.execute(sql_script)
            result = cursor.fetchone()
            print("Total Books:", result[0])
            print("Average Year Published:", round(result[1]))
            print("Average Title Length:", round(result[2]), "characters.")
    except sqlite3.Error as e:
        logging.exception("Error querying aggregation for books:")
        print("Error querying aggregation for books:", e)

def query_filter():
    """Function to filter book data based on conditions"""
    try:
        db_file = pathlib.Path("project.db")
        with sqlite3.connect(db_file) as conn:
            sql_file = pathlib.Path("query_filter.sql")
            with open(sql_file, "r") as file:
                sql_script = file.read()
            cursor = conn.execute(sql_script)
            books = cursor.fetchall()
            for book in books:
                print(book[1], book[2])  # print title and year_published
    except sqlite3.Error as e:
        print("Error filtering book data:", e)

def query_sorting():
    """Function to sort book data based on publication date"""
    try:
        db_file = pathlib.Path("project.db")
        with sqlite3.connect(db_file) as conn:
            sql_file = pathlib.Path("query_sorting.sql")
            with open(sql_file, "r") as file:
                sql_script = file.read()
            cursor = conn.execute(sql_script)
            books = cursor.fetchall()
            for book in books:
                print(book[0], book[1])  # print year_published and title
    except sqlite3.Error as e:
        print("Error sorting book data:", e)

def query_group_by():
    """Function to execute SQL query with GROUP BY clause and display the count of each grouping."""
    try:
        db_file = pathlib.Path("project.db")
        with sqlite3.connect(db_file) as conn:
            sql_file = pathlib.Path("query_group_by.sql")
            with open(sql_file, "r") as file:
                sql_script = file.read()
            cursor = conn.cursor()
            cursor.execute(sql_script)
            results = cursor.fetchall()
            print("Title Length Group\tCount of Books")
            for row in results:
                print(f"{row[0]}\t\t{row[1]}")
            print("Query executed successfully.")
    except sqlite3.Error as e:
        print("Error executing query:", e)

def query_join():
    """Function to read and execute SQL statements to perform INNER JOIN and display the results"""
    try:
        with sqlite3.connect(db_file) as conn:
            sql_file = pathlib.Path("query_join.sql")
            with open(sql_file, "r") as file:
                sql_script = file.read()
            cursor = conn.execute(sql_script)
            rows = cursor.fetchall()
            # display the joint data
            for row in rows:
                print(f"Title: {row[0]}, Author's Last Name: {row[3]}")
            print("Query executed successfully.")
    except sqlite3.Error as e:
        print("Error executing query:", e)


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
    
if __name__ == "__main__":
    main()


logging.info("Program ended")  # log the end of the main method


