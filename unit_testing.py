from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def sample_student():
    return {
        "name": "Test",
        "age": 20,
        "course": "AI"
    }

def test_create_student():
    student = sample_student()
    response = client.post("/students", json=student)
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Test"
    assert data["age"] == 20
    assert data["course"] == "AI"

def test_get_students():
    response = client.get("/students")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def add_numbers(a, b):
    return a + b

def numbers():
    return (2, 3)

def test_add_numbers():
    a, b = numbers()
    result = add_numbers(a, b)
    assert result == 5