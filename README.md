# FastAPI Template Vanilla

This project uses <b>poetry</b> to manage dependencies. 
This project uses <b>pytest</b> to run tests.

## How to use

to test locally:

1. Clone the repository
2. `cd backend` to go to the backend directory
3. Run `poetry install` to install the dependencies
4. Run `sh ./run.sh` to run tests and start the server

alternatively to test production:

1. Clone the repository
2. `cd backend` to go to the backend directory
3. `docker build -t fastapi-template-vanilla .` to build the docker image
4. `docker run -p 8000:8000 fastapi-template-vanilla` to run the docker image
