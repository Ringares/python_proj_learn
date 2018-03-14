"""
默认情况下，logging将日志打印到屏幕，日志级别为WARNING；
日志级别大小关系为：CRITICAL > ERROR > WARNING > INFO > DEBUG > NOTSET，当然也可以自己定义日志级别。

%(levelno)s: 打印日志级别的数值
 %(levelname)s: 打印日志级别名称
 %(pathname)s: 打印当前执行程序的路径，其实就是sys.argv[0]
 %(filename)s: 打印当前执行程序名
 %(funcName)s: 打印日志的当前函数
 %(lineno)d: 打印日志的当前行号
 %(asctime)s: 打印日志的时间
 %(thread)d: 打印线程ID
 %(threadName)s: 打印线程名称
 %(process)d: 打印进程ID
 %(message)s: 打印日志信息
datefmt: 指定时间格式，同time.strftime()
level: 设置日志级别，默认为logging.WARNING
stream: 指定将日志的输出流，可以指定输出到sys.stderr,sys.stdout或者文件，默认输出到sys.stderr，当stream和filename同时指定时，stream被忽略
"""
import logging
import logging.config
# import sys

logging.config.fileConfig('logging.conf')

logger = logging.getLogger('main')

if __name__ == '__main__':
    # logging.basicConfig(level=logging.DEBUG,
    #                     format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
    #                     datefmt='%a, %d %b %Y %H:%M:%S',
    #                     filename='myapp.log',
    #                     filemode='w')

    # while True:
    #     time.sleep(2)
    logger.debug('debug msg')
    logger.info('debug msg')
    logger.warning('debug msg')
    logger.warning('X 投影位置 %s' % 'as')
