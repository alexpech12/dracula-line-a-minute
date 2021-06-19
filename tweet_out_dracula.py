import sys
import time
import logging
from dracula_account_api import api

logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(asctime)s %(message)s')
logger = logging.getLogger()

dracula = open('dracula.txt', 'r', encoding='utf-8')

try:
  chars_read = int(sys.argv[1])
except (IndexError, ValueError):
  chars_read = 0

logger.info("Starting at character " + str(chars_read) + "..")

dracula.read(chars_read)

chars_per_line = 160

while True:
  text = dracula.read(chars_per_line)
  if not text:
    break
  
  api.update_status(text)
  
  logger.info("Printed chars " + str(chars_read) + " to " + str(chars_read + chars_per_line - 1))
  chars_read += chars_per_line
  
  time.sleep(60)

logger.info("THE END!")
dracula.close()


