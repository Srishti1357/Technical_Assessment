from sqlalchemy import Column, Integer, String, Text, ForeignKey, Index
from sqlalchemy.orm import relationship
from .database import Base

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author = Column(String)

    reviews = relationship("Review", back_populates="book")




class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    reviewer = Column(String, nullable=False)
    content = Column(String, nullable=False)
    rating = Column(Integer, nullable=False)  # ✅ ADD THIS LINE
    book_id = Column(Integer, ForeignKey("books.id"))

    book = relationship("Book", back_populates="reviews")


# Index to speed up fetching reviews by book
Index("ix_review_book_id", Review.book_id)
