# Donation Inventory API

A FastAPI backend application for managing donations with full CRUD operations.

## Features

- **Full CRUD Operations**: Create, Read, Update, and Delete donations
- **SQLite Database**: Lightweight database with SQLAlchemy ORM
- **Data Validation**: Pydantic models for request/response validation
- **Interactive API Documentation**: Auto-generated docs with Swagger UI
- **Statistics Endpoint**: Get donation statistics and summaries

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

This will show the interactive Swagger UI documentation where you can test all endpoints.

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

## Development

The code is well-structured with:

- **Database Models**: SQLAlchemy models in `DonationDB`
- **API Schemas**: Pydantic models for validation
- **Error Handling**: Proper HTTP status codes and error messages
- **Documentation**: Comprehensive docstrings and comments

## Running in Production

For production deployment, consider:

1. Using a production ASGI server like Gunicorn
2. Switching to PostgreSQL or MySQL for the database
3. Adding authentication and authorization
4. Implementing logging and monitoring
5. Setting up environment-based configuration