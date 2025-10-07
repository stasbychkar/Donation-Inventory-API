# Donation Inventory API

A FastAPI backend application for managing donations with full CRUD operations.

## Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the Application

```bash
python main.py
```

The API will be available at: `http://localhost:8000`

### 3. View API Documentation

Open your browser and go to: `http://localhost:8000/docs`

## API Endpoints

### Core CRUD Operations

- `GET /donations` - List all donations
- `GET /donations/{id}` - Get a single donation by ID
- `POST /donations` - Create a new donation
- `PUT /donations/{id}` - Update an existing donation
- `DELETE /donations/{id}` - Delete a donation

### Additional Endpoints

- `GET /` - API information and endpoint list
- `GET /donations/stats/summary` - Get donation statistics

## Data Model

Each donation has the following fields:

```json
{
  "id": 1,
  "donor_name": "John Doe",
  "donation_type": "money",
  "amount": 100.00,
  "date": "2024-01-15"
}
```

## Example Usage

### Create a New Donation

```bash
curl -X POST "http://localhost:8000/donations" \
  -H "Content-Type: application/json" \
  -d '{
    "donor_name": "Jane Smith",
    "donation_type": "food",
    "amount": 50.0,
    "date": "2024-01-20"
  }'
```

### Get All Donations

```bash
curl "http://localhost:8000/donations"
```

### Update a Donation

```bash
curl -X PUT "http://localhost:8000/donations/1" \
  -H "Content-Type: application/json" \
  -d '{
    "amount": 150.0
  }'
```

### Delete a Donation

```bash
curl -X DELETE "http://localhost:8000/donations/1"
```

## Database

The application uses SQLite with a local file called `donations.db`. The database is created automatically when you first run the application.

## Frontend

The frontend implementation of the application: [Donation Inventory Frontend](https://github.com/stasbychkar/Donation-Inventory-Frontend)
