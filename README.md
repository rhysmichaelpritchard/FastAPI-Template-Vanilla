# FastAPI Template Vanilla

This project uses <b>poetry</b> to manage dependencies. 
It also uses <b>alembic</b> to manage database migrations. 
This project uses <b>pytest</b> to run tests.

## How to use

1. Clone the repository
2. `cd backend` to go to the backend directory
3. Run `poetry install` to install the dependencies
4. Run `poetry run alembic upgrade head` to create the database
5. Run `sh ./sh` to start the server