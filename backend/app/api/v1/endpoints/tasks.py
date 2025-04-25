from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.auth import get_current_user
from app.models.user import User
from app.models.task import Task
from app.schemas.task import TaskCreate, TaskUpdate, TaskResponse
from datetime import datetime

router = APIRouter()

@router.post("/", response_model=TaskResponse)
async def create_task(
    task: TaskCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Create a new task."""
    db_task = Task(
        **task.dict(),
        created_by_id=current_user.id
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

@router.get("/", response_model=List[TaskResponse])
async def list_tasks(
    transaction_id: int = None,
    completed: bool = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """List tasks with optional filtering."""
    query = db.query(Task)
    if transaction_id:
        query = query.filter(Task.transaction_id == transaction_id)
    if completed is not None:
        query = query.filter(Task.completed == completed)
    return query.all()

@router.get("/{task_id}", response_model=TaskResponse)
async def get_task(
    task_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Get a specific task by ID."""
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )
    return task

@router.put("/{task_id}", response_model=TaskResponse)
async def update_task(
    task_id: int,
    task_update: TaskUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Update a task."""
    db_task = db.query(Task).filter(Task.id == task_id).first()
    if not db_task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )
    
    update_data = task_update.dict(exclude_unset=True)
    
    # Handle completion status change
    if "completed" in update_data and update_data["completed"]:
        update_data["completed_at"] = datetime.utcnow()
    elif "completed" in update_data and not update_data["completed"]:
        update_data["completed_at"] = None
    
    for field, value in update_data.items():
        setattr(db_task, field, value)
    
    db.commit()
    db.refresh(db_task)
    return db_task

@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(
    task_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Delete a task."""
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )
    db.delete(task)
    db.commit()

@router.post("/{task_id}/complete", response_model=TaskResponse)
async def complete_task(
    task_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Mark a task as completed."""
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )
    task.completed = True
    task.completed_at = datetime.utcnow()
    db.commit()
    db.refresh(task)
    return task

@router.post("/{task_id}/uncomplete", response_model=TaskResponse)
async def uncomplete_task(
    task_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Mark a task as not completed."""
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )
    task.completed = False
    task.completed_at = None
    db.commit()
    db.refresh(task)
    return task 