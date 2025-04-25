from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    due_date: Optional[datetime] = None
    priority: Optional[str] = "medium"  # high, medium, low
    category: Optional[str] = None  # inspection, document, communication, etc.
    asana_task_id: Optional[str] = None

class TaskCreate(TaskBase):
    transaction_id: int
    assigned_to_id: Optional[int] = None

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    due_date: Optional[datetime] = None
    completed: Optional[bool] = None
    completed_at: Optional[datetime] = None
    priority: Optional[str] = None
    category: Optional[str] = None
    asana_task_id: Optional[str] = None
    assigned_to_id: Optional[int] = None

class TaskResponse(TaskBase):
    id: int
    transaction_id: int
    assigned_to_id: Optional[int]
    created_by_id: int
    completed: bool
    completed_at: Optional[datetime]
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True  # For Pydantic v2 compatibility 