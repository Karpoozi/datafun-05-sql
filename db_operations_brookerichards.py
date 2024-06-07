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


# log the start of the program
logging.info("Program started")


# define the directory path where the script is located
script_dir = pathlib.Path(__file__).parent


# define the database file path
db_file = "project.db"


# combine the directory path and file name to get the database file path
db_file_path = script_dir / db_file


# create database schema
def create_schema():
    try:
        with sqlite3.connect(db_file_path) as conn:
            schema_file = "C:\\Users\\brichards\\Projects\\datafun-05-sql\\sql\\create_tables.sql"
            with open(schema_file, "r") as file:
                schema_script = file.read()
            conn.executescript(schema_script)
            logging.info("Schema created successfully.")
            print("Schema created successfully.")
    except sqlite3.Error as e:
        logging.exception("Error creating schema")
        print("Error creating schema:", e)


# insert records from CSV files
def insert_data_from_csv():
    try:
        author_data_path = script_dir / "data" / "authors.csv"
        book_data_path = script_dir / "data" / "books.csv"
        authors_df = pd.read_csv(author_data_path)
        books_df = pd.read_csv(book_data_path)
        with sqlite3.connect(db_file_path) as conn:
            authors_df.to_sql("authors", conn, if_exists="replace", index=False)
            books_df.to_sql("books", conn, if_exists="replace", index=False)
            logging.info("Data inserted sucessfully.")
            print("Data inserted successfully.")
    except (sqlite3.Error, pd.errors.EmptyDataError, FileNotFoundError) as e:
        logging.exception("Error inserting data from CSV")  # log the exception
        print("Error inserting data from CSV:", e)


# function to read and execute SQL statements to insert data
def insert_records():
    try:
        with sqlite3.connect(db_file_path) as conn:
            sql_file = "C:\\Users\\brichards\\Projects\\datafun-05-sql\\sql\\insert_records.sql"
            with open(sql_file, "r") as file:
                sql_script = file.read()
            conn.executescript(sql_script)
            logging.info("Data inserted successfully.")
            print("Data inserted successfully.")
    except sqlite3.Error as e:
        logging.exception("Error inserting data from SQL")
        print("Error inserting data from SQL:", e)


# function to update one or more records in the authors table
def update_records():
    try:
        with sqlite3.connect(db_file_path) as conn:
            sql_file = "C:\\Users\\brichards\\Projects\\datafun-05-sql\\sql\\update_records.sql"
            with open(sql_file, "r") as file:
                sql_script = file.read()
            conn.executescript(sql_script)
            logging.info("Records updated successfully.")
            print("Records updated successfully.")
    except sqlite3.Error as e:
        logging.exception("Error updating records")
        print("Error updating records:", e)


# function to delete records from a table
def delete_records():
    try:
        with sqlite3.connect(db_file_path) as conn:
            sql_file = "C:\\Users\\brichards\\Projects\\datafun-05-sql\\sql\\delete_records.sql"
            with open(sql_file, "r") as file:
                sql_script = file.read()
            conn.executescript(sql_script)
            logging.info("Records deleted successfully.")
            print("Records deleted successfully.")
    except sqlite3.Error as e:
        logging.exception("Error deleting records")
        print("Error deleting records:", e)


# function to perform aggregation functions on the books table
def query_aggregation():
    try:
        with sqlite3.connect(db_file_path) as conn:
            sql_file = "C:\\Users\\brichards\\Projects\\datafun-05-sql\\sql\\query_aggregation.sql"
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


# function to filter book data based on conditions
def query_filter():
    try:
        with sqlite3.connect(db_file_path) as conn:
            sql_file = "C:\\Users\\brichards\\Projects\\datafun-05-sql\\sql\\query_filter.sql"
            with open(sql_file, "r") as file:
                sql_script = file.read()
            cursor = conn.execute(sql_script)
            books = cursor.fetchall()
             # print title and year_published
            for book in books:
                print(book[1], book[2])
    except sqlite3.Error as e:
        logging.exception("Error filtering book data", e)
        print("Error filtering book data:", e)


# function to sort book data based on publication date
def query_sorting():
    try:
        with sqlite3.connect(db_file_path) as conn:
            sql_file = "C:\\Users\\brichards\\Projects\\datafun-05-sql\\sql\\query_sorting.sql"
            with open(sql_file, "r") as file:
                sql_script = file.read()
            cursor = conn.execute(sql_script)
            books = cursor.fetchall()
            for book in books:
                print(book[0], book[1])  # print year_published and title
    except sqlite3.Error as e:
        logging.exception("Error sorting book data:", e)
        print("Error sorting book data:", e)


# function to execute SQL query with GROUP BY clause and display the count of each grouping
def query_group_by():
    try:
        with sqlite3.connect(db_file_path) as conn:
            sql_file = "C:\\Users\\brichards\\Projects\\datafun-05-sql\\sql\\query_group_by.sql"
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
        logging.exception("Error executing query:", e)
        print("Error executing query:", e)


# function to read and execute SQL statements to perform INNER JOIN and display the results
def query_join():
    try:
        with sqlite3.connect(db_file_path) as conn:
            sql_file = "C:\\Users\\brichards\\Projects\\datafun-05-sql\\sql\\query_join.sql"
            with open(sql_file, "r") as file:
                sql_script = file.read()
            cursor = conn.execute(sql_script)
            rows = cursor.fetchall()
            # display the joint data
            for row in rows:
                print(f"Title: {row[0]}, Author's Last Name: {row[1]}")
            logging.info("Query executed successfully")
            print("Query executed successfully.")
    except sqlite3.Error as e:
        logging.exception("Error executing query:", e)
        print("Error executing query:", e)


#  main function to execute all SQL operations
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
    

# conditionally execute the main() function if this is the script being run
if __name__ == "__main__":
    main()


# log the end of the main method
logging.info("Program ended")


