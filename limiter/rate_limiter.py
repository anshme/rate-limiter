import logging
from datetime import datetime
from flask import Flask, request
import requests
from bucket import Bucket

app = Flask(__name__)
SIZE = 3
REFILL_RATE = 1
token_bucket_rate_limiter = Bucket(SIZE, REFILL_RATE)


logging.basicConfig(level=logging.INFO)

# Home route
@app.route('/')
def home():
    return "Hello, Flask! This is the home page."


def call_server(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return f"Ping successful: {response.text}"
        else:
            return f"Ping failed with status code: {response.status_code}"
    except requests.exceptions.RequestException as e:
        return f"Error pinging service: {e}"

#How to pass a variable to /ping
@app.route('/ping/<name>')
def client_request(name):

    url = f"http://localhost:2002/ping/{name}"
    current_time = datetime.now()
    logging.info(f"{name} has hit the rate limiter at {current_time}")
    to_proceed  = token_bucket_rate_limiter.token_bucket_algo()
    logging.info(f"Bucket size = {token_bucket_rate_limiter.get_current_bucket_status()}")
    if to_proceed:
        return call_server(url)
    else:
        return f"Url Limit Exceeded , Try after 1 min"
    


def is_service_running(host, port):
    import socket
    try:
        # Attempt to connect to the given host and port
        with socket.create_connection((host, port), timeout=2):
            return True
    except (OSError, ConnectionRefusedError):
        return False


#how to call curl http://localhost:2022/ping/name

if __name__ == '__main__':
    if is_service_running('localhost', '2002'):
        app.run(host='0.0.0.0', port=2022, debug=True)
    else:
        print("Server is not running, rate limiter not starting")