# Fonoma Test

This repository contains a Fonoma Test implementation for serving HTTP requests. Python3.11 is required

## Installation

1. Clone the repository:

```bash
git clone https://github.com/MBI-88/fonoma-test.git
```

2. Install the dependencies:

```bash
pip install -r requirements.txt
```

## Usage

To start the FastAPI server and run the endpoint, follow these steps:

1. Run the server:

```bash
python main.py 
```

2. Navigate to `http://localhost:8000/solution` in your web browser or use an API client such as Postman or cURL to send requests to the endpoint.

## API Documentation

The API documentation is automatically generated using Swagger UI and can be accessed at `http://localhost:8000/docs` or `http://localhost:8000/redoc`. It provides detailed information about the available endpoints, request parameters, and response schemas.

## Endpoints

### `POST /solution`

This endpoint returns a JSON response with data retrieved from the server.

#### Example Request

```http
curl -X POST "https://your-app-url.onrender.com/solution" -H "Content-Type: application/json" -d '{
   "orders": [
       {"id": 1, "item": "Laptop", "quantity": 1, "price": 999.99, "status": "completed"},
       {"id": 2, "item": "Smartphone", "quantity": 2, "price": 499.95, "status": "pending"},
       {"id": 3, "item": "Headphones", "quantity": 3, "price": 99.90, "status": "completed"},
       {"id": 4, "item": "Mouse", "quantity": 4, "price": 24.99, "status": "canceled"},
   ],
   "criterion": "completed"
}'
```

#### Example Response

```json
HTTP/1.1 200 OK
Content-Type: application/json

{
    "result":1299.90,
   
}
```

## Contributing

Contributions are welcome! If you find any issues or want to enhance the endpoint, feel free to submit a pull request. Please ensure that you follow the existing code style and write unit tests for any new features.
