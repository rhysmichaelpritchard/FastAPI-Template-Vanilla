poetry run python3 -m pytest test --verbose
poetry run uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload