from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.auth import get_current_user
from app.models.user import User
from app.models.transaction import Transaction
from app.schemas.transaction import TransactionCreate, TransactionUpdate, TransactionResponse
from datetime import datetime
import uuid

router = APIRouter()

def generate_transaction_id(client_name: str, property_address: str) -> str:
    """Generate a unique transaction ID based on client name and property address."""
    # Clean the inputs
    client_name = client_name.strip().replace(" ", "-").lower()
    property_address = property_address.strip().replace(" ", "-").lower()
    
    # Generate a unique suffix
    unique_suffix = str(uuid.uuid4())[:8]
    
    # Combine into transaction ID
    return f"{client_name}-{property_address}-{unique_suffix}"

@router.post("/", response_model=TransactionResponse)
async def create_transaction(
    transaction: TransactionCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Create a new transaction."""
    # Generate transaction ID
    client_name = transaction.seller_name if transaction.client_type == "seller" else transaction.buyer_name
    transaction_id = generate_transaction_id(client_name, transaction.property_address)
    
    # Create transaction
    db_transaction = Transaction(
        **transaction.dict(),
        transaction_id=transaction_id
    )
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction

@router.get("/", response_model=List[TransactionResponse])
async def list_transactions(
    status: Optional[str] = None,
    client_type: Optional[str] = None,
    search: Optional[str] = Query(None, description="Search in property address, client names, or transaction ID"),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """List transactions with optional filtering and search."""
    query = db.query(Transaction)
    
    if status:
        query = query.filter(Transaction.status == status)
    if client_type:
        query = query.filter(Transaction.client_type == client_type)
    if search:
        search = f"%{search}%"
        query = query.filter(
            (Transaction.property_address.ilike(search)) |
            (Transaction.seller_name.ilike(search)) |
            (Transaction.buyer_name.ilike(search)) |
            (Transaction.transaction_id.ilike(search))
        )
    
    return query.all()

@router.get("/{transaction_id}", response_model=TransactionResponse)
async def get_transaction(
    transaction_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Get a specific transaction by ID."""
    transaction = db.query(Transaction).filter(Transaction.transaction_id == transaction_id).first()
    if not transaction:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Transaction not found"
        )
    return transaction

@router.put("/{transaction_id}", response_model=TransactionResponse)
async def update_transaction(
    transaction_id: str,
    transaction_update: TransactionUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Update a transaction."""
    db_transaction = db.query(Transaction).filter(Transaction.transaction_id == transaction_id).first()
    if not db_transaction:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Transaction not found"
        )
    
    update_data = transaction_update.dict(exclude_unset=True)
    
    # If client name or property address changes, regenerate transaction ID
    if "seller_name" in update_data or "buyer_name" in update_data or "property_address" in update_data:
        client_name = update_data.get("seller_name", db_transaction.seller_name) if db_transaction.client_type == "seller" else update_data.get("buyer_name", db_transaction.buyer_name)
        property_address = update_data.get("property_address", db_transaction.property_address)
        update_data["transaction_id"] = generate_transaction_id(client_name, property_address)
    
    for field, value in update_data.items():
        setattr(db_transaction, field, value)
    
    db.commit()
    db.refresh(db_transaction)
    return db_transaction

@router.delete("/{transaction_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_transaction(
    transaction_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Delete a transaction."""
    transaction = db.query(Transaction).filter(Transaction.transaction_id == transaction_id).first()
    if not transaction:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Transaction not found"
        )
    db.delete(transaction)
    db.commit()

@router.post("/{transaction_id}/archive", response_model=TransactionResponse)
async def archive_transaction(
    transaction_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Archive a transaction by setting its status to 'archived'."""
    transaction = db.query(Transaction).filter(Transaction.transaction_id == transaction_id).first()
    if not transaction:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Transaction not found"
        )
    transaction.status = "archived"
    db.commit()
    db.refresh(transaction)
    return transaction

@router.post("/{transaction_id}/activate", response_model=TransactionResponse)
async def activate_transaction(
    transaction_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Activate a transaction by setting its status to 'active'."""
    transaction = db.query(Transaction).filter(Transaction.transaction_id == transaction_id).first()
    if not transaction:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Transaction not found"
        )
    transaction.status = "active"
    db.commit()
    db.refresh(transaction)
    return transaction 