#! /usr/bin/env python2
# encoding: utf-8

import sys
import pytz
from workflow import Workflow


log = None


def default_timezone_list(wf):
    """Preview all TimeZone"""
    output_timezone_list(wf, pytz.all_timezones)


def output_timezone_list(wf, timezone_list):
    """Preview timezone_list"""
    for item in timezone_list:
        wf.add_item(
            title=item,
            subtitle="Set " + item + " as default TimeZone",
            valid=True,
            arg=item,
            icon='resource/ts_icon.png'
        )
    wf.send_feedback()


def main(wf):

    arg0 = wf.args[0]
    if arg0 == '' or arg0 == ' ':
        default_timezone_list(wf)
    else:
        res = wf.filter(arg0, pytz.all_timezones, min_score=20)
        output_timezone_list(wf, res)


if __name__ == "__main__":
    wf = Workflow()
    log = wf.logger
    sys.exit(wf.run(main))
