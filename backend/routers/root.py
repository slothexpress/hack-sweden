from fastapi import APIRouter, HTTPException
from fastapi import FastAPI
from database import connect_to_db

# Create an instance of the FastAPI class
app = FastAPI()

router = APIRouter()

# Root endpoint
@router.get("/")
def root():
    db_connection = connect_to_db()
    
    if db_connection is not None:
        # Create a cursor object
        cursor = db_connection.cursor()
        
        try:
            # Create table if it doesn't exist
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS USERS (
                    id SERIAL PRIMARY KEY,
                    Name VARCHAR(255),
                    Email VARCHAR(255)
                )
            """)
            
            # Insert sample row
            cursor.execute(
                "INSERT INTO USERS (Name, Email) VALUES (%s, %s) RETURNING *", 
                ("Farfarsmurfen", "farfar@smurfarna.se")
                )
            db_connection.commit()  
            
            # Fetch the inserted data and return for demo purposes
            inserted_data = cursor.fetchone()
            return {"message": "Data inserted and fetched successfully", 
                    "inserted_data": inserted_data}
        
        except Exception as e:
            return {"message": "An error occurred while creating table or inserting data"}
        
        finally:
            # Close the cursor and database connection
            cursor.close()
            db_connection.close()
    
    else:
        return {"message": "Failed to connect to the database"}
