from typing import List
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from models import Donation
from schemas.api_schemas import DonationCreate, DonationUpdate, DonationResponse
from utils.db_utils import get_database
from database import Base, engine
from contextlib import asynccontextmanager

# ================================
# FastAPI Application Setup
# ================================

app = FastAPI(
    title="Donation Inventory API",
    description="A REST API for managing donation inventory",
    version="1.0.0"
)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup logic
    Base.metadata.create_all(bind=engine)
    yield
    engine.dispose()

app = FastAPI(lifespan=lifespan)

# ================================
# API Endpoints
# ================================

@app.get("/", summary="Root endpoint")
async def root():
    return {
        "message": "Welcome to the Donation Inventory API",
        "version": "1.0.0",
        "endpoints": {
            "GET /donations": "List all donations",
            "GET /donations/{id}": "Get a single donation by ID",
            "POST /donations": "Create a new donation",
            "PUT /donations/{id}": "Update an existing donation",
            "DELETE /donations/{id}": "Delete a donation"
        }
    }

@app.get("/donations", response_model=List[DonationResponse], summary="Get all donations")
async def get_donations(db: Session = Depends(get_database)):
    """Retrieve all donations from the database"""
    donations = db.query(Donation).all()
    return donations

@app.get("/donations/{donation_id}", response_model=DonationResponse, summary="Get donation by ID")
async def get_donation(donation_id: int, db: Session = Depends(get_database)):
    """Retrieve a single donation by its ID"""
    donation = db.query(Donation).filter(Donation.id == donation_id).first()
    if not donation:
        raise HTTPException(status_code=404, detail=f"Donation with ID {donation_id} not found")
    return donation

@app.post("/donations", response_model=DonationResponse, status_code=201, summary="Create new donation")
async def create_donation(donation: DonationCreate, db: Session = Depends(get_database)):
    """Create a new donation in the database"""    
    db_donation = Donation(
        donor_name=donation.donor_name,
        donation_type=donation.donation_type,
        amount=donation.amount,
        date=donation.date
    )
    
    db.add(db_donation)
    db.commit()
    db.refresh(db_donation)
    
    return db_donation

@app.put("/donations/{donation_id}", response_model=DonationResponse, summary="Update existing donation")
async def update_donation(
    donation_id: int, 
    donation_update: DonationUpdate, 
    db: Session = Depends(get_database)
):
    """Update an existing donation"""

    # Find the existing donation
    db_donation = db.query(Donation).filter(Donation.id == donation_id).first()
    if not db_donation:
        raise HTTPException(status_code=404, detail=f"Donation with ID {donation_id} not found")
    
    # Update only the provided fields
    update_data = donation_update.dict(exclude_unset=True)
    
    for field, value in update_data.items():
        setattr(db_donation, field, value)
    
    # Commit changes to database
    db.commit()
    db.refresh(db_donation)
    
    return db_donation

@app.delete("/donations/{donation_id}", summary="Delete donation")
async def delete_donation(donation_id: int, db: Session = Depends(get_database)):
    """Delete a donation from the database"""
    
    # Find the donation to delete
    db_donation = db.query(Donation).filter(Donation.id == donation_id).first()
    if not db_donation:
        raise HTTPException(status_code=404, detail=f"Donation with ID {donation_id} not found")
    
    # Delete from database
    db.delete(db_donation)
    db.commit()
    
    return {"message": f"Donation with ID {donation_id} has been deleted successfully"}

# ================================
# Additional Utility Endpoints
# ================================

@app.get("/donations/stats/summary", summary="Get donation statistics")
async def get_donation_stats(db: Session = Depends(get_database)):
    """Get statistics about donations"""
    donations = db.query(Donation).all()
    
    if not donations:
        return {
            "total_donations": 0,
            "total_amount": 0.0,
            "donation_types": {}
        }
    
    # Calculate statistics
    total_amount = sum(donation.amount for donation in donations)
    
    # Group by donation type
    type_stats = {}
    for donation in donations:
        donation_type = donation.donation_type
        if donation_type not in type_stats:
            type_stats[donation_type] = {"count": 0, "total_amount": 0.0}
        type_stats[donation_type]["count"] += 1
        type_stats[donation_type]["total_amount"] += donation.amount
    
    return {
        "total_donations": len(donations),
        "total_amount": total_amount,
        "donation_types": type_stats
    }

if __name__ == "__main__":
    import uvicorn
    print("Starting Donation Inventory API...")
    print("API Documentation: http://localhost:8000/docs")
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)