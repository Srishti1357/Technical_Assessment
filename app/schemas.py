from pydantic import BaseModel
from typing import List, Optional

# 1. Base schema for review
class ReviewBase(BaseModel):
    reviewer: str
    content: str
    rating: float

# 2. Schema for creating a review
class ReviewCreate(ReviewBase):
    pass

# 3. Schema for returning a review
class Review(ReviewBase):
    id: int
    book_id: int

    model_config = {
        "from_attributes": True
    }

# 4. Base schema for book
class BookBase(BaseModel):
    title: str
    author: str

# 5. Schema for creating a book
class BookCreate(BookBase):
    pass

# 6. Schema for returning a book
class Book(BookBase):
    id: int
    reviews: Optional[List[Review]] = []

    model_config = {
        "from_attributes": True
    }
