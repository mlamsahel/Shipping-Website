import psycopg2

# Replace these with your PostgreSQL connection details
host = '*****'  # Replace with your PostgreSQL server hostname or IP address
database_name = 'postgres'  # Replace with your database name
user = 'postgres'  # Replace with your PostgreSQL username
password = '*****'  # Replace with your PostgreSQL password


database = psycopg2.connect(
    dbname=database_name,
    user=user,
    password=password,
    host=host
)

class main:

    def execute(input): #simplifying the cursor.exeucte command into a simple method that creates the cursor, executes, and pushes
    
        cursor = database.cursor()
        cursor.execute(input)
        outp = cursor.fetchall()
        database.commit()
        return outp

    output = execute("select * from customer;")
    print(output)

database.close()