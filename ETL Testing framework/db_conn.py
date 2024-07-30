import mysql.connector

# Replace these with your actual database connection details
DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASSWORD = 'root'
DB_NAME = 'etldb'


def connect_to_db():
    try:
        # Establishing a connection to the database
        conn = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        return conn
    except mysql.connector.Error as e:
        print(f"Error connecting to the database: {e}")
        return None

def close_connection(conn):
    try:
        # Closing the connection
        conn.close()
    except mysql.connector.Error as e:
        print(f"Error closing connection to the database: {e}")


def db_connection():
    return None