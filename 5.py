# https://www.hackerrank.com/challenges/30-loops/problem?isFullScreen=true&h_r=next-challenge&h_v=zen

#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input().strip())
    for i in range(1, 11):
        print("{} x {} = {}".format(n, i, (n*i)))
