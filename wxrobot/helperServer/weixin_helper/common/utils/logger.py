# -*- coding: utf-8 -*-
import os
import sys

from twisted.python import log, util
from twisted.python import logfile

__author__ = 'jerry'

TWISTED_LOG_NAME = 'twisted_log.log'
logging_file_root_path = '/home/helperServer/log/'


def start_twisted_logging(sub_path):

    def custom_emit(self, event_dict):
        """Custom emit for FileLogObserver"""
        text = log.textFromEventDict(event_dict)
        if text is None:
            return
        self.timeFormat = '[%Y-%m-%d %H:%M:%S %f]'
        time_str = self.formatTime(event_dict['time'])
        fmt_dict = {'text': text.replace("\n", "\n\t")}
        msg_str = log._safeFormat("%(text)s\n", fmt_dict)
        util.untilConcludes(self.write, time_str + " " + msg_str)
        util.untilConcludes(self.flush)

    total_path = os.path.join(logging_file_root_path, sub_path)

    # reload(sys)
    # sys.setdefaultencoding('utf8')
    # if not os.path.exists(total_path):
    #     os.makedirs(total_path)

    file_path = os.path.join(total_path, TWISTED_LOG_NAME)
    file_path = file_path.replace("\\", "/")
    if not os.path.exists(file_path):
        print("文件不存在")
    f = logfile.LogFile(file_path, "./", rotateLength=1024 * 1024, maxRotatedFiles=3)
    log.FileLogObserver.emit = custom_emit
    log.startLogging(f, setStdout=False)
    log.startLogging(sys.stdout)

    
def smart_log(_msg):
    log.msg(_msg)
