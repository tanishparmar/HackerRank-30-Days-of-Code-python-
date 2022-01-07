#!/bin/python3
# https://www.hackerrank.com/challenges/30-conditional-statements/problem?isFullScreen=true&h_r=next-challenge&h_v=zen

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    N = int(input().strip())

if(N % 2 != 0):
    print("Weird")
if(N % 2 == 0):
    if(2 < N < 5):
        print("Not Weird")
if(N % 2 == 0):
    if(6 < N <= 20):
        print("Weird")
if(N % 2 == 0):
    if(N > 20):
        print("Not Weird")
