# https://www.hackerrank.com/challenges/30-recursion/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
#!/bin/python3

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the factorial function below.


def factorial(n):

    if n == 1:
        return 1
    else:
        n = n * factorial(n-1)
    return n


if __name__ == '__main__':

    n = int(input())
    result = factorial(n)
    print(result)
