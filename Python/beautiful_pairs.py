#question link: https://www.hackerrank.com/challenges/beautiful-pairs/

#!/bin/python3

import math
import os
import random
import re
import sys

from collections import Counter
def beautifulPairs(A, B):

    a = Counter(A)
    b = Counter(B)
    b_set = 0
    
    for val in a:
        if val in b:
            b_set += min(a[val] , b[val])
            
    if b_set == len(A):
        return b_set-1
    else:
        return b_set+1
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    A = list(map(int, input().rstrip().split()))

    B = list(map(int, input().rstrip().split()))

    result = beautifulPairs(A, B)

    fptr.write(str(result) + '\n')

    fptr.close()
