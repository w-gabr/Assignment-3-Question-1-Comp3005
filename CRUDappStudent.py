import psycopg2
from psycopg2 import IntegrityError, Error

connection = psycopg2.connect(
    dbname="StudentDB",
    user="postgres",
    password="postgres",
    host="localhost",
    port="5432"
)

cursor = connection.cursor()

def getAllStudents():
    SQLquery = "SELECT * FROM Students ORDER BY student_id;" # Define the SQL query
    cursor.execute(SQLquery) # Execute the query
    results = cursor.fetchall() # Fetch all results
    for row in results:
        print(row)

def addStudent(first_name, last_name, email, enrollment_date):
    SQLquery ="""
    INSERT INTO Students (first_name, last_name, email, enrollment_date)
    VALUES (%s, %s, %s, %s);""" # Define the SQL query
    try:
        cursor.execute(SQLquery, (first_name, last_name, email, enrollment_date)) # Execute the query
        connection.commit()
    except IntegrityError as e: # Catch unique constraint violation
        print("Error Email is not unique: ", e)
        connection.rollback()
    except Error as e: # Catch other database errors
        print("Database Error: ", e)
        connection.rollback()

def updateStudentEmail(student_id, new_email):
    SQLquery = """
    UPDATE Students
    SET email = %s
    WHERE student_id = %s;
    """ # Define the SQL query
    try:
        cursor.execute(SQLquery, (new_email, student_id)) # Execute the query
        connection.commit()
    except IntegrityError as e: # Catch unique constraint violation
        print("Error Email is not unique: ", e)
        connection.rollback()
    except Error as e: # Catch other database errors
        print("Database Error: ", e)
        connection.rollback()

def deleteStudent(student_id):
    SQLquery = """
    DELETE FROM Students
    WHERE student_id = %s;
    """ # Define the SQL query
    try:
        cursor.execute(SQLquery, (student_id,)) # Execute the query
        connection.commit()
    except Error as e: # Catch other database errors
        print("Database Error: ", e) 
        connection.rollback()
if __name__ == "__main__":
    # Example usage:
    addStudent("Lamine", "Yamal", "LY10@example.com", "2023-01-25") # Add a new student
    getAllStudents()
    print("----------")
    updateStudentEmail(3, "jimmy.beam@example.com") # Update email for student_id 3
    getAllStudents()
    print("----------")
    updateStudentEmail(2, "john.doe@example.com") # This should raise an error
    print("----------")
    deleteStudent(1) # Delete student with student_id 1
    getAllStudents()
    cursor.close()
    connection.close()
    