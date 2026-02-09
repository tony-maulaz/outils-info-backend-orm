from fastapi import APIRouter, Depends
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.db import get_session
from app.schemas import BookSummary

router = APIRouter(prefix="/raw", tags=["SQL brut"])


@router.get("/books", response_model=list[BookSummary])
def list_books_raw(session: Session = Depends(get_session)) -> list[BookSummary]:
    """Query SQL brute avec text() et mapping manuel."""
    stmt = text("SELECT id, title FROM books ORDER BY id")
    rows = session.execute(stmt).mappings().all()
    return [BookSummary(**row) for row in rows]
