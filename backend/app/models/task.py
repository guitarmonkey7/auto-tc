from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app.core.database import Base
from datetime import datetime

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String)
    due_date = Column(DateTime)
    completed = Column(Boolean, default=False)
    completed_at = Column(DateTime)
    priority = Column(String)  # high, medium, low
    category = Column(String)  # inspection, document, communication, etc.
    asana_task_id = Column(String)  # For Asana integration
    
    # Foreign Keys
    transaction_id = Column(Integer, ForeignKey("transactions.id"))
    assigned_to_id = Column(Integer, ForeignKey("users.id"))
    created_by_id = Column(Integer, ForeignKey("users.id"))
    
    # Timestamps
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    transaction = relationship("Transaction", back_populates="tasks")
    assigned_to = relationship("User", foreign_keys=[assigned_to_id])
    created_by = relationship("User", foreign_keys=[created_by_id])
    
    def __repr__(self):
        return f"<Task {self.title}>" 