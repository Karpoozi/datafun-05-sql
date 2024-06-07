# datafun-05-sql

## Getting Started
1. Create a GitHub project repository with a README.md
2. Open your systems terminal and clone the repository down to your machine
   ```
   git clone URL
   ```
3. Open the project folder on your machine in VS Code
4. Add .gitignore file
5. Update your README.md
6. In your system terminal Git Add / Commit / Push to GitHub
   ```
   git add .
   git commit -m "initial commit"
   git push -u origin main
   ```
7. In VS code open a terminal and activate the virtual enviroment
   ```
   .venv\Scripts\Activate
   ```
8. Install packages into active environment
   ```
   py -m pip install pandas pyarrow
   ```
## Remember to edit your README.md file to record your commands, process, and notes.
   
csharp
Copy code
# Project 5: SQL Database Interactions

This project focuses on database creation, schema development, and diverse SQL operations, including joins, filters, and aggregations.

## Dependencies

This project requires the following external modules:

- pandas
- pyarrow

It is recommended to set up a virtual environment for the project to manage dependencies. Use the following commands to create and activate the virtual environment:

```bash
# Windows example
py -m venv .venv
.\.venv\Scripts\activate

# Mac example
python3 -m venv .venv
source .venv/bin/activate
Install required packages using pip:

bash
Copy code
python -m pip install pandas pyarrow
Usage
Database Initialization
To initialize the database and populate it with data from CSV files, run:

bash
Copy code
python db_initialize_yourname.py
SQL Operations
To perform various SQL operations, execute:

bash
Copy code
python db_operations_yourname.py
Project Structure
data/: Directory containing CSV files for data insertion.
insert_records.sql: SQL script to insert additional records into the database.
Other SQL files: Separate SQL files for different operations like updating, deleting, querying, etc.
db_initialize_yourname.py: Python script for database initialization.
db_operations_yourname.py: Python script for executing SQL operations.
log.txt: Log file containing program execution logs.
Schema Design
The database schema consists of at least two related tables, including foreign key constraints. Detailed schema design can be found in the schema.sql file.

Logging
The program logs start and end of major functions, exceptions, and other major events to the log.txt file.
