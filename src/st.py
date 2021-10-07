#! /usr/bin/env python2
# encoding: utf-8

import sys
from dateutil.parser import parse
from workflow import Workflow
import time
from ts_st_utils import output_for_default, now_str, main_output


def main(wf):
    log.debug('Started')

    arg0 = wf.args[0]
    if arg0 == '' or arg0 == ' ':
        output_for_default(wf)
    else:
        try:
            dt = parse(arg0)
        except BaseException:
            dt = now_str()
        ts = time.mktime(dt.timetuple())
        main_output(wf, ts, 1)


if __name__ == "__main__":
    wf = Workflow()
    log = wf.logger
    sys.exit(wf.run(main))
