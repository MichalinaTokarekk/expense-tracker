from sqlalchemy.orm import Session

from app.models.expense import Expense
from app.schemas.expense import ExpenseCreate, ExpenseUpdate
from sqlalchemy import select


class ExpenseRepository:

    def create(self, db: Session, expense: ExpenseCreate) -> Expense:
        db_expense = Expense(
            amount=expense.amount,
            expense_date=expense.expense_date,
            expense_time=expense.expense_time,
            description=expense.description,
        )

        db.add(db_expense)
        db.commit()
        db.refresh(db_expense)

        return db_expense
    
    def get_all(self, db: Session) -> list[Expense]:
        statement = select(Expense)
        result = db.execute(statement)
        return list(result.scalars().all())
    
    def get_by_id(
        self,
        db: Session,
        expense_id: int,
    ) -> Expense | None:
        statement = select(Expense).where(Expense.id == expense_id)
        result = db.execute(statement)
        return result.scalars().first()
    
    def delete(
            self,
            db: Session,
            expense: Expense,
        ) -> None:
            db.delete(expense)
            db.commit()

    def update(
        self,
        db: Session,
        expense: Expense,
        expense_data: ExpenseUpdate,
    ) -> Expense:
        expense.amount = expense_data.amount
        expense.expense_date = expense_data.expense_date
        expense.expense_time = expense_data.expense_time
        expense.description = expense_data.description

        db.commit()
        db.refresh(expense)

        return expense