import logging
from datetime import datetime
from flask import Flask

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


#TODO write a function which calls pinging_the_server method -> localhost:2002/ping should be the path. How to pass a variable to /ping
@app.route('/ping/<name>')
def client_request(name):
    return f"Hello, {name}! This is the home page."

#how to call curl -v http://localhost:2002/ping

if __name__ == '__main__':
    # Set host to '0.0.0.0' to make the server publicly available
    app.run(host='0.0.0.0', port=2002, debug=True)