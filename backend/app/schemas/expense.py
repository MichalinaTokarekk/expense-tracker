from datetime import date, time, datetime
from decimal import Decimal

from pydantic import BaseModel


class ExpenseCreate(BaseModel):
    amount: Decimal
    expense_date: date
    expense_time: time | None = None
    description: str


class ExpenseResponse(BaseModel):
    id: int
    amount: Decimal
    expense_date: date
    expense_time: time | None
    description: str
    created_at: datetime

    model_config = {
        "from_attributes": True
    }

class ExpenseUpdate(BaseModel):
    amount: Decimal
    expense_date: date
    expense_time: time | None = None
    description: str