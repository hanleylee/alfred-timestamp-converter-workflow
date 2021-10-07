#! /usr/bin/env python2
# encoding: utf-8

import sys
from workflow import Workflow

def main(wf):

    arg0 = wf.args[0]
    wf.save_password('ts_timezone', arg0)

if __name__ == "__main__":
    wf = Workflow()
    log = wf.logger
    sys.exit(wf.run(main))
