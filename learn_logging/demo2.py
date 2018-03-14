import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger('main')
handler_formatter = logging.Formatter('%(asctime)s %(levelname)s %(filename)s [line:%(lineno)d] %(message)s')
log_file_handler = RotatingFileHandler(filename='logs/server.log', maxBytes=10000, backupCount=7,
                                       encoding='utf-8')
log_file_handler.setFormatter(handler_formatter)
log_file_handler.setLevel(logging.DEBUG)
logger.addHandler(log_file_handler)


if __name__ == '__main__':
    logger.info('12121212')