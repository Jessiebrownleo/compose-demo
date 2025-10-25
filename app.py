from flask import Flask
import redis
import os

app = Flask(__name__)
redis_client = redis.Redis(host='redis', port=6379)

@app.route('/')
def hello():
    redis_client.incr('hits')
    count = redis_client.get('hits').decode('utf-8')
    return f"Hello from Flask! This page has been visited {count} times."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
