#! /usr/bin/env python3
# encoding: utf-8

import pytz
import datetime
import time
import json
import re
from keychain import getpassword
from variable import *

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


def res_for_default() -> list:
    """默认输出"""
    timestamp = now_ts()
    return res_for_general(timestamp, 1)


def res_for_no_timezone() -> list:
    return [
        {
            "title": "No timezone set",
            "subtitle": 'Please use setzone to set your default TimeZone',
            # "arg": item["links"]["npm"],
            # "autocomplete": item["name"],
            "icon": {
                "path": ICON_ERROR
            }
        }
    ]


def res_for_error() -> list:
    """错误输出"""
    return [
        {
            "title": "Please input correct String/TimeStamp",
            "icon": {
                "path": ICON_ERROR
            }
        }
    ]


def res_for_general(timestamp, level) -> list:
    """main output"""

    ts_timezone = getpassword(SERVICE, TIMEZONE_ID)
    if ts_timezone is None:
        return res_for_no_timezone()

    ts = str_to_num(timestamp)
    if ts is None:
        return res_for_error()
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

        res = []
        for item in menu_items:
            single = {
                "title": item[0],
                "subtitle": item[1],
                "arg": item[0],
                # "autocomplete": item["name"],
                "icon": {
                    "path": "./resource/ts_icon.png"
                }
            }
            res.append(single)

        return res

# Declare the filter function
def Filter(datalist, regex):
    # Search data based on regular expression in the list
    return [val for val in datalist
        if re.search(regex, val, flags=re.IGNORECASE)]

def output_to_alfred(res: list):
    alfred_json = json.dumps({
        "items": res
    }, indent=2)
    sys.stdout.write(alfred_json)


# if __name__ == "__main__":
