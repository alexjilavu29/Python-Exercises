#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getInaccurateProcesses' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY processOrder
#  2. INTEGER_ARRAY executionOrder
#

def getInaccurateProcesses(processOrder, executionOrder):
    # Write your code here
    # print(processOrder)
    # print(executionOrder)
    requirements = set()
    executions = set()
    errors = 0
    reqMap = {}

    for i in range(len(processOrder)):
        # print(requirements)
        reqMap[processOrder[i]] = set(list(requirements))
        # print(reqMap[processOrder[i]])
        requirements.add(processOrder[i])
    # print(reqMap)
    for i in range(len(executionOrder)):
        if executions.issuperset(reqMap[executionOrder[i]]) is False:
            errors += 1
        executions.add(executionOrder[i])
    return errors

    '''
    for i in range(len(executionOrder)):
        #print(executionOrder[i])
        #print(processOrder.index(executionOrder[i]))
        if processOrder.index(executionOrder[i]) > i:
            errors+=1
        else:
            for j in range(processOrder.index(executionOrder[i])):
                if processOrder[j] not in executions:
                    errors+=1
        executions.add(executionOrder[i])
    return errors
    '''


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    processOrder_count = int(input().strip())

    processOrder = []

    for _ in range(processOrder_count):
        processOrder_item = int(input().strip())
        processOrder.append(processOrder_item)

    executionOrder_count = int(input().strip())

    executionOrder = []

    for _ in range(executionOrder_count):
        executionOrder_item = int(input().strip())
        executionOrder.append(executionOrder_item)

    result = getInaccurateProcesses(processOrder, executionOrder)

    fptr.write(str(result) + '\n')

    fptr.close()

# !/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getOutlierValue' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

# The sum has to be bigger than n-2 numbers.

def getOutlierValue(arr):
    # Write your code here
    arr.sort()
    target = sum(arr) - arr[-2] - arr[-1]
    target2 = sum(arr) - arr[-1]
    outlier = 0

    numbers = []
    numbers.extend(arr)
    numbers.pop(-1)
    numbers.pop(-1)

    if arr[-2] == target:
        if outlier < arr[-1]:
            outlier = arr[-1]
    elif arr[-1] == target:
        if outlier < arr[-2]:
            outlier = arr[-2]

    if abs(arr[-1] - target2) in numbers:
        if outlier < abs(arr[-1] - target2):
            outlier = abs(arr[-1] - target2)

    return outlier


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = getOutlierValue(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
