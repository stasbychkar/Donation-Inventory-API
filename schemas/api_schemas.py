from pydantic import BaseModel, Field
from typing import Optional
import datetime

class DonationBase(BaseModel):
    """Base donation model"""
    donor_name: str = Field(..., description="Name of the donor")
    donation_type: str = Field(..., description="Type of donation")
    amount: float = Field(..., gt=0, description="Amount of the donation")
    date: datetime.date = Field(..., description="Date of donation in YYYY-MM-DD format")

class DonationCreate(DonationBase):
    """Model for creating a new donation"""
    pass

class DonationUpdate(BaseModel):
    """Model for updating an existing donation"""
    donor_name: Optional[str] = Field(None, description="Name of the donor")
    donation_type: Optional[str] = Field(None, description="Type of donation")
    amount: Optional[float] = Field(None, gt=0, description="Amount of the donation")
    date: Optional[str] = Field(None, description="Date of donation in YYYY-MM-DD format")

class DonationResponse(DonationBase):
    """Model for donation responses"""
    id: int = Field(..., description="ID of the donation")
    
    class Config:
        from_attributes = True