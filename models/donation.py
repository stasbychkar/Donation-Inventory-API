from database import Base
from sqlalchemy import Column, Integer, String, Float, Date

class Donation(Base):
    __tablename__ = "donations"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    donor_name = Column(String, index=True, nullable=False)
    donation_type = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    date = Column(Date, nullable=False)