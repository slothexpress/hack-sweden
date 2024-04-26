import sys
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.users import router as users_router
from database import connect_to_db
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Create a logger
logger = logging.getLogger(__name__)

# Create an instance of the FastAPI class
app = FastAPI()

# Include routers
app.include_router(users_router)

# Define allowed origins
allowed_origins = [
    "http://localhost:3000",
    "http://example.com",
]

# Allow CORS and requests from defined origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

# Root endpoint
@app.get("/")
def root():
    # Connect to the database
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
            cursor.execute("INSERT INTO USERS (Name, Email) VALUES (%s, %s) RETURNING *", ("Bagarsmurfen", "bagare@smurfarna.se"))
            db_connection.commit()  # Commit the transaction
            
            # Fetch the inserted data
            inserted_data = cursor.fetchone()
            
            return {"message": "Table created, data inserted and fetched successfully", "inserted_data": inserted_data}
        
        except Exception as e:
            # Log the exception
            logger.error("Error inserting data: %s", e)
            return {"message": "An error occurred while creating table or inserting data"}
        
        finally:
            # Close the cursor and database connection
            cursor.close()
            db_connection.close()
    
    else:
        return {"message": "Failed to connect to the database"}

    
    # Connect to the database
    db_connection = connect_to_db()
    
        
    if db_connection is not None:
        # Create a cursor object
        cursor = db_connection.cursor()
        
        try:
            # Execute SQL query to insert data into a table
            cursor.execute("INSERT INTO your_table_name (column1, column2) VALUES (%s, %s) RETURNING *", ("value1", "value2"))
            db_connection.commit()  # Commit the transaction
            
            # Fetch the inserted data
            inserted_data = cursor.fetchone()
            
            return {"message": "Data inserted and fetched successfully", "inserted_data": inserted_data}
        
        except Exception as e:
            # Log any errors that occur during the insertion process
            print("Error inserting data:", e)
            return {"message": "An error occurred while inserting data"}
        
        finally:
            # Close the cursor and database connection
            cursor.close()
            db_connection.close()
    
    else:
        return {"message": "Failed to connect to the database"}
    
    return "OK SAMI"

# Run the FastAPI application using Uvicorn
#if __name__ == "__main__":
    #import uvicorn
    #uvicorn.run(app, host="localhost", port=8000)
    