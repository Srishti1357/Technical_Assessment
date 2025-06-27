

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from typing import List
from . import models, schemas
from .database import engine, SessionLocal

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/", tags=["Health"])
def read_root():
    return {"message": "Welcome to the Book Review API!"}

from .cache import get_books_from_cache, set_books_to_cache


@app.get("/books", response_model=List[schemas.Book], tags=["Books"])
def get_books(db: Session = Depends(get_db)):
    try:
        cached_books = get_books_from_cache()
        if cached_books:
            print("📦 From Cache")
            return cached_books
    except Exception as e:
        print("❌ Redis error:", e)

    # If cache miss or Redis fails, fetch from DB
    books = db.query(models.Book).all()
    books_data = [schemas.Book.model_validate(book).model_dump() for book in books]

    try:
        # Populate cache
        set_books_to_cache(books_data)
    except Exception as e:
        print("⚠️ Failed to cache data:", e)

    return books_data



@app.post("/books", response_model=schemas.Book, tags=["Books"])
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    db_book = models.Book(**book.model_dump())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


@app.post("/books/{book_id}/reviews", response_model=schemas.Review, tags=["Reviews"])
def create_review(book_id: int, review: schemas.ReviewCreate, db: Session = Depends(get_db)):
    db_book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")

    db_review = models.Review(**review.model_dump(), book_id=book_id)
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review


@app.get("/books/{book_id}/reviews", response_model=List[schemas.Review], tags=["Reviews"])
def list_reviews(book_id: int, db: Session = Depends(get_db)):
    reviews = db.query(models.Review).filter(models.Review.book_id == book_id).all()
    return reviews


from fastapi import status

@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Books"])
def delete_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    
    db.delete(book)
    db.commit()
    return
