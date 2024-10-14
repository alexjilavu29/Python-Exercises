#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getPotentialOfWinner' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY potential
#  2. LONG_INTEGER k
#

def getPotentialOfWinner(potential, k):
    winner_count = 0
    while winner_count <= k:
        if len(potential) == 1:
            return potential[0]
        aux = 0
        while aux < len(potential) - 1:
            if potential[0] < potential[aux + 1]:
                break
            aux += 1
            if aux == k:
                return potential[0]
        if potential[0] > potential[1]:
            winner_count += 1
            loser = potential.pop(1)
            potential.append(loser)
        elif potential[0] > potential[1]:
            winner_count += 1
            loser = potential.pop(1)
            potential.append(loser)
        elif potential[0] < potential[1]:
            loser = potential.pop(0)
            potential.append(loser)
            winner_count = 1

        if winner_count == k:
            return potential[0]

    # Write your code here


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    potential_count = int(input().strip())

    potential = []

    for _ in range(potential_count):
        potential_item = int(input().strip())
        potential.append(potential_item)

    k = int(input().strip())

    result = getPotentialOfWinner(potential, k)

    fptr.write(str(result) + '\n')

    fptr.close()




####


# !/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getPotentialOfWinner' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY potential
#  2. LONG_INTEGER k
#

def getPotentialOfWinner(potential, k):
    winner_count = 0
    alt_potential = []
    alt_potential.extend(potential)
    alt_potential.sort()
    if k > len(potential):
        return alt_potential[-1]
    while winner_count <= k:
        if len(potential) == 1:
            return potential[0]
        aux = 0
        while aux < len(potential) - 1:
            if potential[0] < potential[aux + 1]:
                break
            aux += 1
            if aux == k:
                return potential[0]
        if potential[0] > potential[1]:
            winner_count += 1
            loser = potential.pop(1)
            potential.append(loser)
        else:
            loser = potential.pop(0)
            potential.append(loser)
            winner_count = 1

        if winner_count == k:
            return potential[0]

    # Write your code here


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    potential_count = int(input().strip())

    potential = []

    for _ in range(potential_count):
        potential_item = int(input().strip())
        potential.append(potential_item)

    k = int(input().strip())

    result = getPotentialOfWinner(potential, k)

    fptr.write(str(result) + '\n')

    fptr.close()
