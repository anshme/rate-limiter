import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO)

def pinging_the_server(whoami='Anjuman'):
    # Get the current time
    current_time = datetime.now()
    logging.info(f"{whoami} has pinged at {current_time}")
    # logging.error(f"this is an error")

#TODO write a function to host the server. localhost:2002


#TODO write a function which calls pinging_the_server method -> localhost:2002/ping should be the path. How to pass a variable to /ping


#how to call curl -v http://localhost:2002/ping