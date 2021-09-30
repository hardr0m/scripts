# -*- coding: utf-8 -*-

import logging
from queue import Queue

log = logging.getLogger('process')

class Process:
    def __init__(self, ip_addr: str):
        self.ip = ip_addr

    def run(self):
        log.info('Test logging => {}'.format(self.ip))
