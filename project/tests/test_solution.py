from fastapi.testclient import TestClient
from fastapi import status
from main import app
import unittest


data = {
    "orders": [
        {
            "id": 1,
            "item": "Laptop",
            "quantity": 1,
            "price": 999.99,
            "status": "completed"
        },
        {
            "id": 2,
            "item": "Smartphone",
            "quantity": 2,
            "price": 499.95,
            "status": "pending"
        },
        {
            "id": 3,
            "item": "Headphones",
            "quantity": 3,
            "price": 99.90,
            "status": "completed"
        },
        {
            "id": 4,
            "item": "Mouse",
            "quantity": 4,
            "price": 24.99,
            "status": "canceled"
        }
    ],
    "criterion": "completed"
}

sample = {
    "orders": [
         {
             "id": 1,
             "item": "Laptop",
             "quantity": -1,
             "price": 999.99,
             "status": "completed"
         },

    ],
    "criterion": "completed"
}


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.client = TestClient(app, base_url="http://localhost:8000")
        return super().setUp()

    def test_solution_status200(self) -> None:
        response = self.client.post("/solution", json=data)
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_solution_data(self) -> None:
        response = self.client.post("/solution", json=data)
        self.assertEqual(response.json(),1299.69)

    def test_solution_status422(self) -> None:
        response = self.client.post("/solution", json=sample)
        self.assertEqual(response.status_code,status.HTTP_422_UNPROCESSABLE_ENTITY) 
