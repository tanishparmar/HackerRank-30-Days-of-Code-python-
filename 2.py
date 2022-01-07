# https://www.hackerrank.com/challenges/30-operators/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function accepts following parameters:
#  1. DOUBLE meal_cost
#  2. INTEGER tip_percent
#  3. INTEGER tax_percent
#


def solve(meal_cost, tip_percent, tax_percent):
    # Write your code here
    round(meal_cost, 2)

    tip_percent = (tip_percent/100)*round(meal_cost, 2)
    # print(tip_percent)
    tax_percent = (tax_percent/100)*round(meal_cost, 2)
    # print(tax_percent)
    total_cost = round(meal_cost, 2)+tip_percent+tax_percent
    print(round(total_cost))


if __name__ == '__main__':
    meal_cost = float(input().strip())
    # meal_cost = 10.75

    tip_percent = int(input().strip())
    # tip_percent = 17

    tax_percent = int(input().strip())
    # tax_percent = 5

    solve(meal_cost, tip_percent, tax_percent)
