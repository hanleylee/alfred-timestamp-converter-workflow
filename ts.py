#! /usr/bin/env python2
# encoding: utf-8

import sys
import datetime
import time
from ts_st_utils import *

log = None

def main(wf):
    log.debug('Started')

    args = wf.args[0]
    args = args.split(' ')
    if len(wf.args) == 0:
        output_for_default(wf)
    else:
        arg0 = args[0]
        trimmed_timestamp = 0
        if arg0 == 'ms':
            arg1 = args[1] if len(args) > 1 else ''
            trimmed_timestamp = arg1
        elif arg0 == 's':
            arg1 = args[1] if len(args) > 1 else ''
            trimmed_timestamp = arg1[:10]
        else:
            trimmed_timestamp = arg0[:10]
        output(trimmed_timestamp, wf)


if __name__ == "__main__":
    wf = Workflow()
    log = wf.logger
    sys.exit(wf.run(main))
