from pydantic import BaseModel, Field
from typing import Optional
from datetime import date, datetime
from decimal import Decimal

class TransactionBase(BaseModel):
    property_address: str
    city: str
    county: str
    zip_code: str
    sales_price: Decimal = Field(..., decimal_places=2)
    earnest_money: Optional[Decimal] = Field(None, decimal_places=2)
    binding_agreement_date: Optional[date] = None
    due_diligence_end_date: Optional[date] = None
    financing_contingency_end_date: Optional[date] = None
    closing_date: Optional[date] = None
    closing_attorney_name: Optional[str] = None
    seller_name: str
    seller_contact: Optional[str] = None
    buyer_name: str
    buyer_contact: Optional[str] = None
    buyer_agent_name: Optional[str] = None
    buyer_agent_contact: Optional[str] = None
    seller_agent_name: Optional[str] = None
    seller_agent_contact: Optional[str] = None
    loan_type: Optional[str] = None
    property_type: Optional[str] = None
    client_type: str  # buyer/seller
    status: Optional[str] = "active"

class TransactionCreate(TransactionBase):
    pass

class TransactionUpdate(BaseModel):
    property_address: Optional[str] = None
    city: Optional[str] = None
    county: Optional[str] = None
    zip_code: Optional[str] = None
    sales_price: Optional[Decimal] = Field(None, decimal_places=2)
    earnest_money: Optional[Decimal] = Field(None, decimal_places=2)
    binding_agreement_date: Optional[date] = None
    due_diligence_end_date: Optional[date] = None
    financing_contingency_end_date: Optional[date] = None
    closing_date: Optional[date] = None
    closing_attorney_name: Optional[str] = None
    seller_name: Optional[str] = None
    seller_contact: Optional[str] = None
    buyer_name: Optional[str] = None
    buyer_contact: Optional[str] = None
    buyer_agent_name: Optional[str] = None
    buyer_agent_contact: Optional[str] = None
    seller_agent_name: Optional[str] = None
    seller_agent_contact: Optional[str] = None
    loan_type: Optional[str] = None
    property_type: Optional[str] = None
    client_type: Optional[str] = None
    status: Optional[str] = None

class TransactionResponse(TransactionBase):
    id: int
    transaction_id: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True  # For Pydantic v2 compatibility 