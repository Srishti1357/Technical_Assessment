from fastapi.testclient import TestClient
from app.main import app
from app.cache import r

client = TestClient(app)

def test_books_cache_miss_then_set():
    r.delete("books")  # Clear Redis cache

    # First request - should fetch from DB and set cache
    response1 = client.get("/books")
    assert response1.status_code == 200
    assert isinstance(response1.json(), list)

    # Check if Redis now has cached data
    cached = r.get("books")
    assert cached is not None
