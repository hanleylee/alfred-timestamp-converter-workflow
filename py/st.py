#! /usr/bin/env python3
# encoding: utf-8

from dateutil.parser import parse
import time
from variable import *
from utils import res_for_default, now_str, res_for_general, output_to_alfred

def main():

    args = QUERY_STR
    res = []
    if args == '' or args == ' ':
        res = res_for_default()
    else:
        try:
            dt = parse(args)
        except BaseException:
            dt = now_str()
        ts = time.mktime(dt.timetuple())
        res = res_for_general(ts, 1)

    output_to_alfred(res)

if __name__ == "__main__":
    main()
