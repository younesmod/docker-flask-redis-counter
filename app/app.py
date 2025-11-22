from flask import Flask
import redis
import os
import time
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

def wait_for_redis():
    """Wait for Redis to be ready"""
    max_retries = 5
    retry_delay = 2
    
    for i in range(max_retries):
        try:
            redis_host = os.getenv("REDIS_HOST", "redis-cache")
            logger.info(f"Attempting to connect to Redis at {redis_host}, attempt {i+1}")
            
            r = redis.Redis(
                host=redis_host, 
                port=6379, 
                db=0, 
                socket_connect_timeout=5,
                socket_keepalive=True
            )
            r.ping()  # Test connection
            logger.info("Successfully connected to Redis")
            return r
        except redis.ConnectionError as e:
            logger.warning(f"Redis connection failed: {e}")
            if i < max_retries - 1:
                logger.info(f"Retrying in {retry_delay} seconds...")
                time.sleep(retry_delay)
            else:
                logger.error("Max retries reached, could not connect to Redis")
                raise

# Initialize Redis connection
try:
    r = wait_for_redis()
except Exception as e:
    logger.error(f"Failed to initialize Redis: {e}")
    r = None

@app.route("/")
def index():
    if r is None:
        return "Redis service unavailable", 503
    
    try:
        count = r.incr("page_hits")
        return f"Page visited {count} times!"
    except redis.RedisError as e:
        return f"Redis error: {str(e)}", 500

@app.route("/health")
def health():
    """Health check endpoint"""
    if r and r.ping():
        return "OK", 200
    return "Redis unavailable", 503

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)