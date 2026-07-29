import sys
import datetime
import time
import pytz
import re
 
# Declare the list contains subject code
sublist = ['CSE-407', 'PHY-101', 'CSE-101', 'ENG-102', 'MAT-202']

# Declare the filter function
def Filter(datalist, regex):
    # Search data based on regular expression in the list
    return [val for val in datalist
        if re.search(regex, val, flags=re.IGNORECASE)]

# Print the filter data
if __name__ == "__main__":
    print(Filter(sublist, 'cse'))
