import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",          # Your MySQL password
        database="library_db"
    )
# hoyr database is completed in one table ?