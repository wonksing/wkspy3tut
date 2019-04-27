#!/bin/python3

import os
import sys

#
# Complete the equalStacks function below.
#

def equalStacksBak(h1, h2, h3):


    while True:
        h1Sum = sum(h1)
        h2Sum = sum(h2)
        h3Sum = sum(h3)
        if h1Sum == h2Sum and h2Sum == h3Sum:
            return h1Sum

        if len(h1) == 0 or len(h2) == 0 or len(h3) == 0:
            return 0
            
        if len(h1) == 1 and len(h2) == 1 and len(h3) == 1:
            return 0

        stacks = []
        if len(h1) > 1:
            stacks.append(h1)
            
        if len(h2) > 1:
            stacks.append(h2)
            
        if len(h3) > 1:
            stacks.append(h3)
            

        maxI = 0
        maxV = 0
        ind = 0

        if len(stacks) > 1:
            
            while ind < len(stacks):
                if ind == 0:
                    maxV = sum(stacks[ind])
                    maxI = ind
                
                if sum(stacks[ind]) > maxV:
                    maxV = sum(stacks[ind])
                    maxI = ind
                
                ind += 1

        if len(stacks) > 0:
            stacks[maxI].pop(0)


def equalStacks(h1, h2, h3):

    stacks = [h1, h2, h3]
    sumArr = [sum(h1), sum(h2), sum(h3)]
    lenArr = [len(h1), len(h2), len(h3)]
    while True:

        if sumArr[0] == sumArr[1] == sumArr[2]:
            return sumArr[0]

        if lenArr[0] == 0 or lenArr[1] == 0 or lenArr[2] == 0:
            return 0

        if lenArr[0] == 1 and lenArr[1] == 1 and lenArr[2] == 1:
            return 0
            
        ind = 0
        maxI = ind
        maxV = sumArr[maxI]
        while ind < len(lenArr):
            if lenArr[ind] > 1 and sumArr[ind] > maxV:
                maxV = sumArr[ind]
                maxI = ind
            
            ind += 1

        if len(stacks) -1 >= maxI:
            popped = stacks[maxI].pop(0)
            sumArr[maxI] = sumArr[maxI] - popped
            lenArr[maxI] = lenArr[maxI] - 1


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # n1N2N3 = input().split()
    f = open("testdata/equalstack-tc4.txt", 'r')
    line = f.readline()
    # print(line)
    n1N2N3 = line.split()

    n1 = int(n1N2N3[0])

    n2 = int(n1N2N3[1])

    n3 = int(n1N2N3[2])


    line = f.readline()
    # print(line)
    h1 = list(map(int, line.rstrip().split()))

    line = f.readline()
    # print(line)
    h2 = list(map(int, line.rstrip().split()))

    line = f.readline()
    # print(line)
    h3 = list(map(int, line.rstrip().split()))

    result = equalStacks(h1, h2, h3)

    print(result)

    f.close()
    # fptr.write(str(result) + '\n')

    # fptr.close()
