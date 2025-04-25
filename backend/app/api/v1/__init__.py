from fastapi import APIRouter
from .endpoints import auth, users, tasks, transactions

api_router = APIRouter()

# Include all routers here
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(tasks.router, prefix="/tasks", tags=["tasks"])
api_router.include_router(transactions.router, prefix="/transactions", tags=["transactions"])

# Import and include all routers here
# from .endpoints import auth, users, transactions, etc. 