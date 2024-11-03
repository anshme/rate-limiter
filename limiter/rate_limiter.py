import logging
from datetime import datetime
from flask import Flask, request
import requests

app = Flask(__name__)


logging.basicConfig(level=logging.INFO)


def pinging_the_server(whoami='Anjuman'):
    # Get the current time
    current_time = datetime.now()
    logging.info(f"{whoami} has pinged at {current_time}")
    # logging.error(f"this is an error")

#TODO write a function to host the server. localhost:2002
# Home route
@app.route('/')
def home():
    return "Hello, Flask! This is the home page."


#TODO write a function which calls pinging_the_server method -> localhost:2002/ping should be the path.
#How to pass a variable to /ping
@app.route('/ping/<name>')
def client_request(name):

    url = f"http://localhost:2002/ping/{name}"
    current_time = datetime.now()
    logging.info(f"{name} has hit the rate limiter at {current_time}")
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return f"Ping successful: {response.text}"
        else:
            return f"Ping failed with status code: {response.status_code}"
    except requests.exceptions.RequestException as e:
        return f"Error pinging service: {e}"



def is_service_running(host, port):
    import socket
    try:
        # Attempt to connect to the given host and port
        with socket.create_connection((host, port), timeout=2):
            return True
    except (OSError, ConnectionRefusedError):
        return False


#how to call curl -v http://localhost:2022/ping

if __name__ == '__main__':
    if is_service_running('localhost', '2002'):
        app.run(host='0.0.0.0', port=2022, debug=True)
    else:
        print("Server is not running, rate limiter not starting")