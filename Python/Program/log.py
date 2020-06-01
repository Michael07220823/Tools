import logging


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M',
                    handlers=[logging.FileHandler('my.log', 'w', 'utf-8'), ])


logging.debug('Hello debug!')
logging.info('Hello info!')
logging.warning('Hello warning!')
logging.error('Hello error!')
logging.critical('Hello critical!')