#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import colorlog

from os import isatty
from sys import argv

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

log_setup()

proc = Process(ip_addr='192.168.0.1')

if __name__ == '__main__':
    proc.run()
