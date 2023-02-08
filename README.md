# FastAPI Template Vanilla

This project uses <b>poetry</b> to manage dependencies. 
It also uses <b>alembic</b> to manage database migrations. 
This project uses <b>pytest</b> to run tests.

## How to use

to test locally:

1. Clone the repository
2. `cd backend` to go to the backend directory
3. Run `poetry install` to install the dependencies
4. Run `sh ./run.sh` to start the server

alternatively to test production:

1. Clone the repository
2. `cd backend` to go to the backend directory
3. docker build -t fastapi-template-vanilla .
4. docker run -p 8000:8000 fastapi-template-vanilla
