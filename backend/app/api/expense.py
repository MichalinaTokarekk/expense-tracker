from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.expense import ExpenseCreate, ExpenseResponse
from app.services.expense_service import ExpenseService
from fastapi import HTTPException
from app.schemas.expense import (
    ExpenseCreate,
    ExpenseResponse,
    ExpenseUpdate,
)

router = APIRouter()
service = ExpenseService()

@router.post("/", response_model=ExpenseResponse)
def create_expense(
    expense: ExpenseCreate,
    db: Session = Depends(get_db),
):
    created_expense = service.create_expense(db, expense)
    return created_expense

@router.get("/", response_model=list[ExpenseResponse])
def get_all_expenses(
    db: Session = Depends(get_db),
):
    return service.get_all(db)

@router.get("/{expense_id}", response_model=ExpenseResponse)
def get_expense(
    expense_id: int,
    db: Session = Depends(get_db),
):
    expense = service.get_by_id(db, expense_id)

    if expense is None:
        raise HTTPException(
            status_code=404,
            detail="Expense not found",
        )

    return expense

@router.delete("/{expense_id}", status_code=204)
def delete_expense(
    expense_id: int,
    db: Session = Depends(get_db),
):
    expense = service.delete_expense(db, expense_id)

    if expense is None:
        raise HTTPException(
            status_code=404,
            detail="Expense not found",
        )
    
@router.put(
    "/{expense_id}",
    response_model=ExpenseResponse,
)
def update_expense(
    expense_id: int,
    expense: ExpenseUpdate,
    db: Session = Depends(get_db),
):
    updated_expense = service.update_expense(
        db,
        expense_id,
        expense,
    )

    if updated_expense is None:
        raise HTTPException(
            status_code=404,
            detail="Expense not found",
        )

    return updated_expense