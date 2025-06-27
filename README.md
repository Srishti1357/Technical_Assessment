# BACKEND ENGINEER TECHNICAL ASSESSMENT
# 📚 Book Review API

A FastAPI-based backend service that allows users to manage books and their reviews. Built as part of a backend engineering technical assessment.

---

## 🔧 Tech Stack

- ⚙️ **Backend**: Python, FastAPI
- 🗄️ **Database**: SQLite + SQLAlchemy ORM
- 🚀 **Caching**: Redis (via Docker)
- 📜 **Documentation**: Swagger/OpenAPI (`/docs`)
- 🧪 **Testing**: Pytest, HTTPX
- 🛠️ **Migrations**: Alembic

---

## 🚀 Features

- `GET /books`: List all books (with Redis caching)
- `POST /books`: Add a new book
- `GET /books/{id}/reviews`: List all reviews for a book
- `POST /books/{id}/reviews`: Add a review to a book
- Health check endpoint at `/`
- Swagger UI at `/docs`

---

## 🛠️ Getting Started

### 1. Clone the repository

In your terminal or cmd:
```
git clone https://github.com/Srishti1357/Technical_Assessment.git
cd .\Technical_Assessment\
```
### 2. Create & activate a virtual environment

In your terminal or cmd:
```
python -m venv venv
```
If you use macOS/Linux then use this command:
```
source venv/bin/activate
```
If you use Windows OS then use this command:
```
venv\Scripts\activate
```
### 3. Install dependencies

In your terminal or cmd:
```
pip install -r requirements.txt
```
### 4. Run the application

In your terminal or cmd:
```
uvicorn app.main:app --reload
```

Visit [Swagger UI Link]http://127.0.0.1:8000/docs to access the Swagger UI.

## 🧱 Database Setup

### Run Alembic Migrations

In your terminal or cmd:
```
alembic upgrade head`
```

## 💾 Caching Setup

### Redis Setup (via Docker)
Ensure Docker is running, then:

```
docker run -d -p 6379:6379 --name redis redis
```

Redis is used to cache the /books list for faster responses.
In production, caching can be extended to frequently accessed review endpoints like /books/{id}/reviews, but for this assessment I focused on caching the /books list for simplicity.

## 🧪 Running Tests

Run unit and integration tests using this command run this in tour terminal or cmd:
```
pytest
```

Tests cover:
- Unit tests for GET /books, POST /books, POST /reviews, GET /reviews
- Integration test for cache-miss path on /books

## 📁 Project Structure


```
.
├── app/
│   ├── main.py           # FastAPI application entrypoint
│   ├── models.py         # SQLAlchemy models
│   ├── schemas.py        # Pydantic schemas for request/response validation
│   ├── database.py       # DB session and engine configuration
│   └── cache.py          # Redis connection and caching logic
│
├── tests/
│   ├── test_books.py     # Unit tests for book endpoints
│   ├── test_reviews.py   # Unit tests for review endpoints
│   └── test_cache.py     # Integration test for Redis cache
│
├── alembic/              # Alembic migrations folder
│   └── versions/         # Auto-generated migration scripts
```

## ✅ Conclusion
This project demonstrates a complete backend service using FastAPI, SQLAlchemy, Alembic, SQLite, and Redis. It showcases key engineering practices such as:

- RESTful API design
- Data modeling and migrations
- Caching with Redis
- Robust error handling
- Unit and integration testing
- Clear documentation and project structure

Feel free to fork the repo, open issues, or contribute improvements!

## 📬 Contact

If you have any questions, feel free to reach out at - srishtichawla999@gmail.com

Let me know if you want me to:

- [Github Link]https://github.com/Srishti1357/Technical_Assessment
- srishtichawla999@gmail.com
