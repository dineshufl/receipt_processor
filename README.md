# Receipt Processor

This project implements a simple receipt processor API that calculates points for receipts based on specific rules. It uses a Flask web service with in-memory storage to handle receipt data and point calculations.

## API Endpoints

- `POST /receipts/process`: Processes a receipt and returns a unique receipt ID.
- `GET /receipts/{id}/points`: Retrieves the points awarded for a given receipt ID.

---

## Prerequisites

Make sure you have the following installed:

- Python 3.x
- Docker

## Project Setup

### Step 1: Clone the Repository

Clone the project to your local machine:

```bash
git clone <repository-url>
cd receipt_processor
```

### Step 2: Build the Docker Image

Build the Docker image for the Flask application:

```bash
docker build -t receipt-processor .
```

### Step 3: Run the Docker Container

Run the Docker container, exposing the app on port 5001 (which maps to port 5000 inside the container):

```bash
docker run -p 5001:5000 receipt-processor
```

### Step 4: Access the API

Once the Docker container is running, you can interact with the API using `curl` or Postman.

---

## Testing the API

### 1. Process a Receipt

You can send a POST request to the `/receipts/process` endpoint to process a receipt. Here’s an example `curl` command:

```bash
curl -X POST http://localhost:5001/receipts/process -H "Content-Type: application/json" -d '{
  "retailer": "Target",
  "purchaseDate": "2022-01-01",
  "purchaseTime": "13:01",
  "items": [
    {
      "shortDescription": "Mountain Dew 12PK",
      "price": "6.49"
    },
    {
      "shortDescription": "Emils Cheese Pizza",
      "price": "12.25"
    }
  ],
  "total": "18.74"
}'
```

The response will return a unique `id` for the receipt:

```json
{
  "id": "7fb1377b-b223-49d9-a31a-5a02701dd310"
}
```

### 2. Retrieve Points for a Receipt

Once you have the receipt ID, you can retrieve the points using a GET request to the `/receipts/{id}/points` endpoint:

```bash
curl http://localhost:5001/receipts/7fb1377b-b223-49d9-a31a-5a02701dd310/points
```

This will return the points for that specific receipt:

```json
{
  "points": 20
}
```

---

## Stopping the Application

To stop the Docker container, press `Ctrl+C` in the terminal where the container is running, or use the following command:

```bash
docker ps  # Get the container ID
docker stop <container-id>
```

---

## Scope for Improvements

- **Redis for In-Memory Storage**: Redis can be integrated as an in-memory storage solution for receipt data. This would allow the application to persist data more efficiently during the runtime, especially for distributed or large-scale deployments.
- **Database Integration**: Adding a persistent database like PostgreSQL or MongoDB would allow receipt data to be stored long-term, even after container restarts.
- **Unit Testing**: Expanding the codebase to include unit tests for point calculation logic and API routes would increase the reliability and maintainability of the system.
- **Rate Limiting**: Implementing rate limiting or authentication to secure and control access to the API.

---

## Notes

- The application stores data in-memory, so once the container is stopped, all receipt data will be lost.
- You can easily extend this project to use a persistent database if needed.

---

### Thank you for using the Receipt Processor API!
