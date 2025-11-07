# Student Crud Application (Python + PostgreSQL)

Setup:

1) Requirements:
   Python 3.9+
   PostgreSQL
   psycopg2 (use pip install to install this python library)

2) DB setup
   run the SQLDDLandDML file using a PostgreSQL GUI such as pgAdmin4 to create student table and insert sample data

3) Configure Connection between python and PostgreSQL
   connection = psycopg2.connect(
    dbname="StudentDB",
    user="postgres",
    password="postgres",
    host="localhost",
    port="5432"
)

Usage:
1) Running:
   run all functions in main script at the bottom
   

