from flask import Flask
import redis
import os

app = Flask(__name__)

# Redis connection (uses Docker internal DNS: "redis")
r = redis.Redis(host=os.getenv("REDIS_HOST", "redis"), port=6379, db=0)

@app.route("/")
def index():
    count = r.incr("page_hits")
    return f"Page visited {count} times!"
