import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO)

def pinging_the_server(whoami='Anjuman'):
    # Get the current time
    current_time = datetime.now()
    logging.info(f"{whoami} has pinged at {current_time}")
    # logging.error(f"this is an error")