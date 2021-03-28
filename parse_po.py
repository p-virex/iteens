from logger import logger

logger.info('!')
logger.debug('!')
logger.error('!')
logger.warning('!')

try:
    2/0
except ZeroDivisionError as e:
    logger.exception(e)