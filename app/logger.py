import logging
import sys
from functools import lru_cache
from uvicorn.config import LOGGING_CONFIG

format = '%(asctime)s - %(name)s - %(levelname)s: %(message)s'
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
stream_handler = logging.StreamHandler(sys.stdout)
log_formatter = logging.Formatter(format)
stream_handler.setFormatter(log_formatter)
logger.addHandler(stream_handler)
LOGGING_CONFIG["formatters"]["default"]["fmt"] = format

@lru_cache
def get_logger():
    return logger
