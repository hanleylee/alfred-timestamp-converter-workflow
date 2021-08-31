#! /usr/bin/env python2
# encoding: utf-8

import pytz
import sys
from workflow import Workflow, ICON_CLOCK, ICON_ERROR
import datetime
import time


def now():
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
    output(timestamp, wf)


def output_for_error(wf):
    """错误输出"""
    wf.add_item(
        title='Please input corret timestamp',
        valid=False,
        icon=ICON_ERROR
    )
    wf.send_feedback()


def output(timestamp, wf):
    ts = str_to_num(timestamp)
    if ts is None:
        output_for_error(wf)
    else:
        # if mode == 'ts': # 时间戳模式
        #     elif mode == 'st': # 字面日期模式
        utc_base1 = datetime.datetime.utcfromtimestamp(ts)
        utc_base = utc_base1.replace(tzinfo=pytz.utc)
        utc_date_time = utc_base.strftime('%Y-%m-%d %H:%M:%S')
        utc_date = utc_base.strftime('%Y-%m-%d')
        cn_base = utc_base.astimezone(pytz.timezone("Asia/Shanghai"))
        cn_date_time = cn_base.strftime('%Y-%m-%d %H:%M:%S')
        cn_date = cn_base.strftime('%Y-%m-%d')

        menu_items = [
            (str(int(ts)), 'Time Stamp'),
            (utc_date_time, 'UTC Date Time'),
            (utc_date, 'UTC Date'),
            (cn_date_time, 'CN Date Time'),
            (cn_date, 'CN Date'),
        ]

        for item in menu_items:
            wf.add_item(
                title=item[0],
                subtitle=item[1],
                valid=True,
                arg=item[0],
                icon='ts_icon.png'
            )

        wf.send_feedback()


# if __name__ == "__main__":
    # wf = Workflow()
    # log = wf.logger
    # sys.exit(wf.run(main))
