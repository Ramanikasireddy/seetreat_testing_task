import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_calculator_get(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Calculator' in response.data

def test_calculator_post_valid(client):
    data = {'num1': '5', 'num2': '3', 'operator': '+'}
    response = client.post('/', data=data)
    assert response.status_code == 200
    assert b'Result: 8.0' in response.data

def test_calculator_post_invalid(client):
    data = {'num1': 'abc', 'num2': '3', 'operator': '+'}
    response = client.post('/', data=data)
    assert response.status_code == 200
    assert b'Invalid input. Please enter valid numbers.' in response.data

def test_calculator_post_unknown_operator(client):
    data = {'num1': '5', 'num2': '3', 'operator': '/'}
    response = client.post('/', data=data)
    assert response.status_code == 200
    assert b'error; allowed operators are +, -, or *' in response.data