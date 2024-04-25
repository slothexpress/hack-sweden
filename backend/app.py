from fastapi import FastAPI

# Create an instance of the FastAPI class
app = FastAPI()

test = {"id": "1234", "name": "bagarsmurfen"}

# Root endpoint
@app.get("/")
def read_root():
    return test

# Run the FastAPI application using Uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)