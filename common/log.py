# encoding:utf-8

import logging
import sys

SWITCH = True

def _get_logger():
    log = logging.getLogger('log')
    log.setLevel(logging.INFO)
    console_handle = logging.StreamHandler(sys.stdout)
    # [%(filename)s:%(lineno)d]
    console_handle.setFormatter(logging.Formatter('[%(levelname)s][%(asctime)s][=%(thread)d=] - %(message)s',
                                                  datefmt='%Y-%m-%d %H:%M:%S'))
    log.addHandler(console_handle)

    file_handler = logging.FileHandler('log/log.txt')
    formatter = logging.Formatter('[%(levelname)s][%(asctime)s][=%(thread)d=] - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    file_handler.setFormatter(formatter)
    log.addHandler(file_handler)

    return log

def close_log():
    global  SWITCH
    SWITCH = False


def debug(arg, *args):
    if SWITCH:
        if len(args) == 0:
            logger.debug(arg)
        else:
            logger.debug(arg.format(*args))

def info(arg, *args):
    if SWITCH:
        if len(args) == 0:
            logger.info(arg)
        else:
            logger.info(arg.format(*args))


def warn(arg, *args):
    if len(args) == 0:
        logger.warning(arg)
    else:
        logger.warning(arg.format(*args))

def error(arg, *args):
    if len(args) == 0:
        logger.error(arg)
    else:
        logger.error(arg.format(*args))

def exception(e):
    logger.exception(e)


# 日志句柄
logger = _get_logger()
