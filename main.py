from gui import *
import psycopg2

# Replace these with your PostgreSQL connection details
host = '192.168.1.42'  # Replace with your PostgreSQL server hostname or IP address
database_name = 'postgres'  # Replace with your database name
user = 'postgres'  # Replace with your PostgreSQL username
password = '06896#Qz1'  # Replace with your PostgreSQL password


database = psycopg2.connect(
    dbname=database_name,
    user=user,
    password=password,
    host=host
)

def execute(input): #simplifying the cursor.exeucte command into a simple method that creates the cursor, executes, and pushes
    
    cursor = database.cursor()
    cursor.execute(input)
    outp = cursor.fetchall()
    database.commit()
    return outp

createGUI()

database.close()