import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg://postgres:postgres@db:5432/orm_demo",
)

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


def init_db() -> None:
    from app.models import Base, Author, Book
    from sqlalchemy import func, select

    Base.metadata.create_all(bind=engine)

    with SessionLocal() as session:
        author_count = session.scalar(select(func.count(Author.id)))
        if author_count:
            return

        authors = [
            Author(name="Ada Lovelace"),
            Author(name="Grace Hopper"),
            Author(name="Alan Turing"),
        ]
        session.add_all(authors)
        session.flush()

        books = [
            Book(title="Notes on the Analytical Engine", pages=120, author_id=authors[0].id),
            Book(title="Compilers and Cobol", pages=220, author_id=authors[1].id),
            Book(title="Computing Machinery and Intelligence", pages=90, author_id=authors[2].id),
        ]
        session.add_all(books)
        session.commit()
