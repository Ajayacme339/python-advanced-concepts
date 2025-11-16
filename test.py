### Configuring Logging in Python


from LOGGER1 import logging
def sum(a, b):
    logging.debug("Addition is taking place")
    return a + b

logging.debug("Addition is taking place")
sum(3,5)
