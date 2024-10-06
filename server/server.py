import logging
import time

def pinging_the_server(whoami):
    logging.info(f"{whoami} has pinged at {time.localtime}")