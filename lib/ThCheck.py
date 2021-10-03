# -*- coding: utf-8 -*-

import json
import logging

from threading import Thread
from dns.resolver import resolve as dres
from smtplib import SMTP

log = logging.getLogger('ThCheck')

class ThCheck(Thread):
    def __init__(self, th_num=None, queue=None):
        super(ThCheck, self).__init__()

        self.th_num = th_num
        self.queue = queue

    def do_smtp_check(self, task=None):
        log.debug('Thread => {} | Get MX Record for Domain => {}'.format(self.th_num, task['domain']))
        for mxs in dres(task['domain'], 'MX'):
            mx = mxs.exchange.to_text()[:-1]

            log.info('Thread => {} | Check MX => {}'.format(self.th_num, mx))
            try:
                with SMTP(mx, timeout=3) as smtp:
                    res = smtp.noop()
                    log.info('Thread => {} | MX => {} Result => {}'.format(self.th_num, mx, res[1].decode()))

            except OSError as e:
                log.error('Thread => {} | MX => {} Result => Code: {}, Msg: {}'.format(self.th_num, mx, e.errno, e.strerror))

    def run(self):
        while True:
            try:
                task = self.queue.get()
                self.do_smtp_check(task=task)

            except Exception as e:
                print(e)

            finally:
                self.queue.task_done()
