from flask import Flask
import redis
import os

app = Flask(__name__)

# Redis connection
r = redis.Redis(host=os.getenv("REDIS_HOST", "redis-cache"), port=6379, db=0)

@app.route("/")
def index():
    count = r.incr("page_hits")
    return f"Page visited {count} times!"

@app.route("/health")
def health():
    """Health check endpoint for Docker"""
    try:
        # Check if Redis is responsive
        r.ping()
        return "OK", 200
    except:
        return "Redis unavailable", 503

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)