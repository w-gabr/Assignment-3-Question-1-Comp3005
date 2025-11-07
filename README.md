# Student Crud Application (Python + PostgreSQL)

Setup:

1) Requirements:<br>
   Python 3.9+ <br>
   PostgreSQL <br>
   psycopg2 (use pip install to install this python library)<br>

2) DB setup <br>
   run the SQLDDLandDML file using a PostgreSQL GUI such as pgAdmin4 to create student table and insert sample data <br>

3) Configure Connection between python and PostgreSQL<br>
   connection = psycopg2.connect(
    dbname="StudentDB",
    user="postgres",
    password="postgres",
    host="localhost",
    port="5432"
)<br>

Usage:<br>
1) Running:<br>
   run all functions in main script at the bottom

video:https://www.youtube.com/watch?v=cF9ZfPDt_t0&t=17s
   

