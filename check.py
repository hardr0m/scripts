#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import colorlog

from os import isatty
from sys import argv
from getopt import getopt

from lib.Process import Process

""" setup logger """
def log_setup():
    root = logging.getLogger()
    root.setLevel(logging.DEBUG)
    format = '[ %(asctime)s ] - [ %(levelname)-8s ] - %(message)s'
    date_format = '%Y-%m-%d %H:%M:%S'
    if isatty(2):
        cformat = '%(log_color)s' + format
        f = colorlog.ColoredFormatter(
            cformat,
            date_format,
            log_colors={
                'DEBUG': 'bold_blue',
                'INFO': 'bold_green',
                'WARNING': 'bold_yellow',
                'ERROR': 'bold_red',
                'CRITICAL': 'red'
            }
        )
    else:
        f = logging.Formatter(format, date_format)
    ch = logging.StreamHandler()
    ch.setFormatter(f)
    root.addHandler(ch)

def main_proc():
    log = logging.getLogger('Main process')
    opt, args = getopt(argv[1:], 't:a:', ['thread=', 'ipaddr='])

    thread = None
    ip = None

    for key, val in opt:
        if key in ('-t', '--thread'):
            thread = int(val)
        elif key in ('-a', '--ipaddr'):
            ip = val
        else:
            log.error('Something Wrong')

    proc = Process(th_num=thread, ip_addr=ip)
    proc.run()

if __name__ == '__main__':
    log_setup()
    main_proc()
