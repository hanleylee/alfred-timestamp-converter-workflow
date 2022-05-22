#! /usr/bin/env python3
# encoding: utf-8

from utils import res_for_default, res_for_general, output_to_alfred
from variable import *

def main():

    res = []
    args = QUERY_STR.split(' ')
    if args[0] == '' or args[0] == ' ':
        res = res_for_default()
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
        res = res_for_general(trimmed_timestamp, level)

    output_to_alfred(res)

if __name__ == "__main__":
    main()
