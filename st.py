#! /usr/bin/env python2
# encoding: utf-8

import sys
from dateutil.parser import parse
from workflow import Workflow, ICON_WEB, ICON_WARNING, ICON_INFO
import datetime
import time
from ts_st_utils import *


def main(wf):
    log.debug('Started')

    args = wf.args[0]
    args = args.split(' ')
    if len(wf.args) == 0:
        output_for_default(wf)
    else:
        arg0 = args[0]
        try:
            dt = parse(arg0)
        except BaseException:
            dt = now_ts()
    ts = time.mktime(dt.timetuple())
    output(ts, wf)


if __name__ == "__main__":
    wf = Workflow()
    log = wf.logger
    sys.exit(wf.run(main))
