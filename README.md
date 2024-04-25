# Hack Sweden
WIP: About the app or purpose etc


## How to run
Clone this repository to your local machine.


### Requirements
- Python version 3 or higher
- Node.js version 18 or higher
- npm version 7 or higher

### Database
WIP: PostgreSQL

### Backend
Python

To install all Python dependencies, navigate to the backend folder and run command:

`pip install -r requirements.txt`

On Windows, activate the virtual environment by running:

`.\venv\Scripts\activate`

Or on MacOS, activate the virtual environment with command:

`source venv/bin/activate`

Open [http://localhost:8000](http://localhost:8000) to test the root endpoint which returns static sample data.

To start the backend project, run:

`uvicorn main:app --reload`

Uvicorn allows FASTapi apps to update live by reloading code changes as files are saved.

### Frontend
Navigate to the frontend folder, where the `package.json` file is located and run the project (in development mode) with command:

`npm start`

Open [http://localhost:3000](http://localhost:3000) to view it in your browser.

The page will reload when you make changes. You may also see any lint errors in the console.

On how to build the project for deployment - see README in the frontend folder.