import logging as log
import dotenv
import os

dotenv.load_dotenv()

LOG_LEVEL = os.environ.get("LOG_LEVEL", "DEBUG").upper()
logging = log.getLogger(__name__)
log.basicConfig(encoding='utf-8', level=LOG_LEVEL)