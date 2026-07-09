from sqlalchemy.orm import Session

from app.repositories.expense_repository import ExpenseRepository
from app.schemas.expense import ExpenseCreate, ExpenseUpdate
from app.models.expense import Expense


class ExpenseService:
    def __init__(self):
        self.repository = ExpenseRepository()

    def create_expense(
        self,
        db: Session,
        expense: ExpenseCreate,
    ) -> Expense:
        return self.repository.create(db, expense)
    
    def get_all(
        self,
        db: Session,
    ) -> list[Expense]:
        return self.repository.get_all(db)
    
    def get_by_id(
        self,
        db: Session,
        expense_id: int,
    ) -> Expense | None:
        return self.repository.get_by_id(db, expense_id)
    
    def delete_expense(
        self,
        db: Session,
        expense_id: int,
    ) -> Expense | None:
        expense = self.repository.get_by_id(db, expense_id)

        if expense is None:
            return None

        self.repository.delete(db, expense)

        return expense
    
    def update_expense(
        self,
        db: Session,
        expense_id: int,
        expense_data: ExpenseUpdate,
    ) -> Expense | None:

        expense = self.repository.get_by_id(db, expense_id)

        if expense is None:
            return None

        return self.repository.update(
            db,
            expense,
            expense_data,
        )