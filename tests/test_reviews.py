from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_add_review():
    # First add a book (needed to test review)
    book_res = client.post("/books", json={
        "title": "Reviewable Book",
        "author": "Review Author"
    })
    book = book_res.json()

    # Now add a review for that book
    review_res = client.post(f"/books/{book['id']}/reviews", json={
        "reviewer": "Srishti",
        "rating": 4.0,
        "content": "Nice book!"
    })
    assert review_res.status_code == 200
    review = review_res.json()
    assert review["reviewer"] == "Srishti"
    assert review["rating"] == 4.0
    assert review["content"] == "Nice book!"
    assert review["book_id"] == book["id"]

def test_get_reviews():
    # First add a book again
    book_res = client.post("/books", json={
        "title": "Another Book",
        "author": "Tester"
    })
    book = book_res.json()

    # Add a review
    client.post(f"/books/{book['id']}/reviews", json={
        "reviewer": "TestUser",
        "rating": 5.0,
        "content": "Excellent!"
    })

    # Now fetch reviews
    res = client.get(f"/books/{book['id']}/reviews")
    assert res.status_code == 200
    reviews = res.json()
    assert isinstance(reviews, list)
    assert len(reviews) > 0
    assert reviews[0]["book_id"] == book["id"]
