import logging
logging.basicConfig(level=logging.DEBUG,filename='runlog.log',
                    format='%(asctime)s %(filename)s[line:%(lineno)d]%(levelname)s %(message)s')
logging.debug('debug info')
logging.info('hello ')
logging.warning('warning info')
logging.error('error info')
logging.critical('critical info')