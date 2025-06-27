import redis

# Connect to Redis running in Docker
r = redis.Redis(host='localhost', port=6379, decode_responses=True)

try:
    r.set("test", "redis is working from docker")
    print("✅ Redis is working! Value:", r.get("test"))
except Exception as e:
    print("❌ Redis connection failed:", e)
