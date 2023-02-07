import requests

def test_get():
    response = requests.get("http://localhost:8000")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}