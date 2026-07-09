from fastapi import FastAPI
from app.api.expense import router as expense_router

app = FastAPI()


@app.get("/")
def root():
    return {
        "message": "Expense Tracker API"
    }


@app.get("/health")
def health():
    return {
        "status": "ok"
    }

app.include_router(
    expense_router,
    prefix="/expenses",
    tags=["Expenses"],
)