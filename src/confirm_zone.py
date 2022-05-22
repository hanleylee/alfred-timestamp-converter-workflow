#! /usr/bin/env python3
# encoding: utf-8

import sys
from keychain import setpassword
from variable import *

file_name = sys.argv[0]
picked_zone = sys.argv[1]

def main():

    setpassword(SERVICE, TIMEZONE_ID, picked_zone)

if __name__ == "__main__":
    main()
