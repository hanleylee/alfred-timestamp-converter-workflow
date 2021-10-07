#! /usr/bin/env python2
# encoding: utf-8

import sys
from workflow import Workflow
from ts_st_utils import output_for_default, main_output

log = None

def main(wf):
    log.debug('Started')

    args = wf.args[0]
    args = args.split(' ')
    if wf.args[0] == '' or wf.args[0] == ' ':
        output_for_default(wf)
    else:
        arg0 = args[0]
        trimmed_timestamp = 0
        level = 1
        if arg0 == 'ms':
            arg1 = args[1] if len(args) > 1 else ''
            trimmed_timestamp = arg1
            level = 1000
        elif arg0 == 's':
            arg1 = args[1] if len(args) > 1 else ''
            trimmed_timestamp = arg1
        else:
            trimmed_timestamp = arg0
        main_output(wf, trimmed_timestamp, level)


if __name__ == "__main__":
    wf = Workflow()
    log = wf.logger
    sys.exit(wf.run(main))
