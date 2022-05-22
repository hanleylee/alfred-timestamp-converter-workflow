#! /usr/bin/env python3
# encoding: utf-8

import pytz
from utils import Filter, output_to_alfred
from variable import *

def default_timezone_list() -> list:
    """Preview all TimeZone"""
    return output_timezone_list(pytz.all_timezones)


def output_timezone_list(timezone_list) -> list:
    """Preview timezone_list"""
    res = []
    for item in timezone_list:
        row = {
            "title": item,
            "subtitle": "Set '" + item + "' as default TimeZone",
            "arg": item,
            "icon": {
                "path": 'resource/ts_icon.png'
            }
        }
        res.append(row)
    return res

def main():
    arg0 = QUERY_STR
    res = []
    if arg0 == '' or arg0 == ' ':
        res = default_timezone_list()
    else:
        filter_res = Filter(pytz.all_timezones, arg0)
        res = output_timezone_list(filter_res)

    output_to_alfred(res)

if __name__ == "__main__":
    main()
