import redis
import json

r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

def get_books_from_cache():
    data = r.get("books")
    if data:
        return json.loads(data)
    return None

def set_books_to_cache(books):
    r.set("books", json.dumps(books), ex=3600)  # cache expires in 1 hr
