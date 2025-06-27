# from pydantic import BaseModel
# from typing import List, Optional

# class ReviewBase(BaseModel):
#     content: str
#     rating: int

# class ReviewCreate(ReviewBase):
#     pass

# class Review(ReviewBase):
#     id: int
#     class Config:
#         orm_mode = True

# class BookBase(BaseModel):
#     title: str
#     author: str

# class BookCreate(BookBase):
#     pass

# class Book(BookBase):
#     id: int
#     reviews: Optional[List[Review]] = []

#     # class Config:
#     #     orm_mode = True

#     model_config = {
#     "from_attributes": True
# }




# from pydantic import BaseModel
# from typing import List, Optional

# class ReviewBase(BaseModel):
#     content: str
#     rating: int

# class ReviewCreate(ReviewBase):
#     pass

# class Review(ReviewBase):
#     id: int

#     model_config = {
#         "from_attributes": True
#     }

# class BookBase(BaseModel):
#     title: str
#     author: str

# class BookCreate(BookBase):
#     pass

# class Book(BookBase):
#     id: int
#     reviews: Optional[List[Review]] = []

#     model_config = {
#         "from_attributes": True
#     }


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
