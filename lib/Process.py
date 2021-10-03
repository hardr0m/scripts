# -*- coding: utf-8 -*-

import logging
import json
import requests

from queue import Queue

from .ThCheck import ThCheck

log = logging.getLogger('process')

class Process:
    def __init__(self, th_num=None, ip_addr=None):
        self.ip = ip_addr
        self.th_num = th_num

    def run(self):
        log.info('Start SMTP Check for ip => {}'.format(self.ip))

        log.info('Get domain list')
        c_url = 'https://info.dmtaserver.com/api/v1/instances/servers/{}'.format(self.ip)
        res = requests.get(c_url).json()

        log.info('Set thread empty queue')
        queue = Queue()

        log.info('Start {} Threads for multiprocess'.format(self.th_num))
        for i in range(self.th_num):
            log.info('Thread {} start'.format(i))
            thr = ThCheck(th_num=i, queue=queue)
            thr.setDaemon(True)
            thr.start()

        for data in res['response']:
            log.debug('Create Task for domain => {}'.format(data))

            task = {
                'domain': data,
                'smtp': None
            }

            queue.put(task)

        queue.join()
