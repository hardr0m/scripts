# -*- coding: utf-8 -*-

import json
import logging

from threading import Thread

log = logging.getLogger('ThCheck')

class ThCheck(Thread):
    def __init__(self, th_num=None, queue=None):
        super(ThCheck, self).__init__()

        self.th_num = th_num
        self.queue = queue

    def run(self):
        while True:
            try:
                task = self.queue.get()

            except Exception as e:
                print(e)

            finally:
                self.queue.task_done()
