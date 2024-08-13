#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    # Write your code here
    right = 0
    left = 0
    highest_count = 0
    current_count = 0
    sort_a = sorted(a)
    while right < len(sort_a):
        if abs(sort_a[left]-sort_a[right]) <= 1:
            current_count += 1
            if current_count > highest_count:
                highest_count = current_count
            right +=1
        else:
            current_count -= 1
            left +=1
            
    return highest_count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
