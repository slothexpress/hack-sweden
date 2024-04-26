import os
from dotenv import load_dotenv
import psycopg2

def load_env_variables():
    dotenv_path = '.env'
    load_dotenv(dotenv_path)

def connect_to_db():
    load_env_variables()
    
    dbname = os.getenv("DATABASE_NAME")
    user = os.getenv("DATABASE_USER")
    password = os.getenv("DATABASE_PASSWORD")
    host = os.getenv("DATABASE_HOST")
    
    try:
        connection = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host
        )
        
        return connection
    
    except psycopg2.Error as e:
        print("Error connecting to the database:", e)
        return None
