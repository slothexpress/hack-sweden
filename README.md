# Hack Sweden - Team Beachfaces
WIP: About the app or purpose etc

## How to run
Clone this repository to your local machine.

### Requirements
- Python version 3 or higher
- Node.js version 18 or higher
- npm version 7 or higher

### Database: PostgreSQL
WIP 
- Postgres version 16
- pgAdmin 4

### Backend: Python
Navigate to the backend folder and create a virtual environment with the following command:

`python -m venv venv`

To install all Python dependencies, run command:

`pip install -r requirements.txt`

On Windows, activate the virtual environment by running:

`.\venv\Scripts\activate`

Or on MacOS, activate the virtual environment with command:

`source venv/bin/activate`

Open [http://localhost:8000](http://localhost:8000) to test the root endpoint which returns static sample data.

To start the backend project, run:

`uvicorn main:app --reload`

Uvicorn allows FASTapi apps to update live by reloading code changes as files are saved.

### Frontend: React.js
Navigate to the frontend folder, where the `package.json` file is located and install all dependencies with command:

`npm install`

Run the project (in development mode):

`npm start`

Open [http://localhost:3000](http://localhost:3000) to view it in your browser.

The page will reload when you make changes. You may also see any lint errors in the console.

On how to build the project for deployment - see README in the frontend folder.
