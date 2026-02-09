from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db import get_session
from app.models import Author, Book
from app.schemas import BookWithAuthor

router = APIRouter(prefix="/orm", tags=["ORM jointure"])


@router.get("/books-with-authors", response_model=list[BookWithAuthor])
def list_books_with_authors(
    session: Session = Depends(get_session),
) -> list[BookWithAuthor]:
    stmt = (
        select(
            Book.id,
            Book.title,
            Book.pages,
            Author.name.label("author_name"),
        )
        .join(Author)
        .order_by(Book.id)
    )
    rows = session.execute(stmt).all()
    return [
        BookWithAuthor(
            id=row.id,
            title=row.title,
            pages=row.pages,
            author_name=row.author_name,
        )
        for row in rows
    ]
