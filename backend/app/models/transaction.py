from sqlalchemy import Column, Integer, String, Date, Numeric, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.core.database import Base
from datetime import datetime

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    transaction_id = Column(String, unique=True, index=True)
    property_address = Column(String)
    city = Column(String)
    county = Column(String)
    zip_code = Column(String)
    sales_price = Column(Numeric(12, 2))
    earnest_money = Column(Numeric(12, 2))
    binding_agreement_date = Column(Date)
    due_diligence_end_date = Column(Date)
    financing_contingency_end_date = Column(Date)
    closing_date = Column(Date)
    closing_attorney_name = Column(String)
    seller_name = Column(String)
    seller_contact = Column(String)
    buyer_name = Column(String)
    buyer_contact = Column(String)
    buyer_agent_name = Column(String)
    buyer_agent_contact = Column(String)
    seller_agent_name = Column(String)
    seller_agent_contact = Column(String)
    loan_type = Column(String)
    property_type = Column(String)
    client_type = Column(String)  # buyer/seller
    status = Column(String, default="active")
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    documents = relationship("Document", back_populates="transaction")
    tasks = relationship("Task", back_populates="transaction")
    
    def __repr__(self):
        return f"<Transaction {self.transaction_id}>" 