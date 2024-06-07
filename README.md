# datafun-05-sql

## Overview
Project 5 integrates Python and SQL, focusing on database interactions using SQLite. This project introduces logging, a useful tool for debugging and monitoring projects, and involves creating and managing a database, building a schema, and performing various SQL operations, including queries with joins, filters, and aggregations.

Clone the Repository: Start by cloning the repository to your local machine. Use the following command in your terminal or command prompt:
'''
git clone URL
'''
Navigate to the Project Directory: After cloning the repository, navigate to the project directory using the following 

bash
Copy code
cd project_name
Install Dependencies: Before running the project, install the required dependencies. Execute the following command to install dependencies listed in the requirements.txt file:

Copy code
pip install -r requirements.txt
Usage
Ensure Python is Installed: Ensure you have Python installed on your system. If not, download and install Python from the official Python website.

Run the Main Script: To execute the project, run the main.py script using the following command:

css
Copy code
python main.py
This will initiate the execution of various database operations and display relevant outputs in the console.

File Structure
The project directory is organized as follows:

main.py: The main Python script orchestrating the execution of all database operations.
SQL Scripts: These files contain SQL queries for different database tasks:
create_tables.sql: Schema creation.
query_records.sql: Record insertion.
update_records.sql: Record updating.
delete_records.sql: Record deletion.
query_aggregation.sql: Aggregation queries.
query_filter.sql: Filtering queries.
query_sorting.sql: Sorting queries.
query_group_by.sql: Grouping queries.
query_join.sql: Joining queries.
data/ Directory: Contains sample CSV files (authors.csv and books.csv) for data insertion.
log.txt: Logs errors or exceptions encountered during execution.
README.md: Contains detailed information about the project.
Dependencies
The project relies on the following dependencies:

Python 3.x: Programming language used to write scripts.
pandas: Python library for data manipulation and analysis.
sqlite3: Lightweight, serverless database engine for local storage.
