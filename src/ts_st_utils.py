#! /usr/bin/env python2
# encoding: utf-8

import pytz
from workflow import Workflow, ICON_ERROR, PasswordNotFound
import datetime
import time


def now_str():
    """当前时间"""
    return datetime.datetime.utcnow()


def now_ts():
    """当前时间戳"""
    return time.time()


def str_to_num(s):
    """字符串转数字"""
    """Convert string to either int or float."""
    if s == '':
        return now_ts()

    try:
        ret = int(s)
    except BaseException:
        try:
            ret = float(s)
        except BaseException:
            ret = None
    return ret


def output_for_default(wf):
    """默认输出"""
    timestamp = now_ts()
    main_output(wf, timestamp, 1)


def output_for_no_timezone(wf):
    """未设置时区的输出"""
    wf.add_item('No timezone set.',
                'Please use setzone to set your default TimeZone.',
                valid=False,
                icon=ICON_ERROR)
    wf.send_feedback()
    return 0


def output_for_error(wf):
    """错误输出"""
    wf.add_item(
        title='Please input corret String/TimeStamp',
        valid=False,
        icon=ICON_ERROR
    )
    wf.send_feedback()
    return 0


def main_output(wf, timestamp, level):
    """main output"""

    try:
        ts_timezone = wf.get_password('ts_timezone')
    except PasswordNotFound:  # API key has not yet been set
        output_for_no_timezone(wf)

    ts = str_to_num(timestamp)
    if ts is None:
        output_for_error(wf)
    else:
        utc_base1 = datetime.datetime.utcfromtimestamp(ts / level)
        utc_base = utc_base1.replace(tzinfo=pytz.utc)
        utc_date_time = utc_base.strftime('%Y-%m-%d %H:%M:%S')
        utc_date = utc_base.strftime('%Y-%m-%d')
        # local_base = utc_base.astimezone(pytz.timezone("Asia/Shanghai"))
        local_base = utc_base.astimezone(pytz.timezone(ts_timezone))
        local_date_time = local_base.strftime('%Y-%m-%d %H:%M:%S')
        local_date = local_base.strftime('%Y-%m-%d')

        menu_items = [
            (str(int(ts)), 'Time Stamp'),
            (local_date_time, ts_timezone + ' Date Time'),
            (local_date, ts_timezone + ' Date'),
            (utc_date_time, 'UTC Date Time'),
            (utc_date, 'UTC Date'),
        ]

        for item in menu_items:
            wf.add_item(
                title=item[0],
                subtitle=item[1],
                valid=True,
                arg=item[0],
                icon='resource/ts_icon.png'
            )

        wf.send_feedback()


# if __name__ == "__main__":
    # wf = Workflow()
    # log = wf.logger
    # sys.exit(wf.run(main))
