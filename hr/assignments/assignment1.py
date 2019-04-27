#!/bin/python

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    sum_of_each_hourglass = []  # 각 모래시계 합을 보관할 배열 선언
    for row in range(0,4):      
        for col in range(0,4):

            values = []         # 한개 모래시계의 값들을 보관할 배열 선언
            for hg_row in range(0,3):       # 모래시계는 3x3배열에서 옆구리 2개를 뺀것이니 0, 1, 2번 행만 보면 됨
                for hg_col in range(0,3):   # 모래시계는 3x3배열에서 옆구리 2개를 뺀것이니 0, 1, 2번 열만 보면 됨
                    if (hg_row==1 and hg_col==0):   # 3x3배열의 왼쪽 옆구리는 항상 0으로 지정
                        values.append(0)
                    elif (hg_row==1 and hg_col==2): # 3x3배열의 오른쪽 옆구리는 항상 0으로 지정
                        values.append(0)
                    else:                           # 나머지 값들은 사용
                        values.append(arr[hg_row + row][hg_col + col])
            
            sum_of_each_hourglass.append(sum(values))   # 모래시계 합을 보관(나중에 최대값 찾기 위해)
    return max(sum_of_each_hourglass)


if __name__ == '__main__':

    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    '''
    1. 테스트 입력 데이터
        1 1 1 0 0 0
        0 1 0 0 0 0
        1 1 1 0 0 0
        0 0 2 4 4 0
        0 0 0 2 0 0
        0 0 1 2 4 0
    
    2. 함수설명 
        - input() : 사용자의 입력을 콘솔로 입력 받음
        - rstrip() : 문자열 끝의 빈칸을 없앰. 
          예) "test string     ".rstrip() = "test string"
        - split() : 문자열을 빈칸(구분자)으로 쪼개기
        - list(map(int, input().rstrip().split())) : "1 1 1 0 0 0" 문자열을 [1, 1, 1, 0, 0, 0] 형태의 정수 배열로 만들어줌
        - arr.append() - arr란 배열에 [1, 1, 1, 0, 0, 0] 를 추가
    '''
    for _ in range(6):  # 입력을 6번 받음 엔터키(Carriage Return 6번)
        arr.append(list(map(int, input().rstrip().split())))    # 1 1 1 0 0 0   < 이런 형태의 문자열을 6번 입력하여 각각의 숫자를 arr에 assign

    '''
    hourglass 최대값 구하는 함수 
    위에 선언/구현 됨
    '''
    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
