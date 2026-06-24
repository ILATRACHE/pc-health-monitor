import logging

logging.basicConfig(
    filename='rapport.txt',
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
logging.info("Programme started :")
def info(message):
    logging.info(message)
def warning(message):
    logging.warning(message)
def error(message):
    logging.error(message)