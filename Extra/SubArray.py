#!usr/bin/env python
#coding:utf-8

'''
2、最大值减去最小值小于或等于num的子数组数量
给定数组arr和整数num，返回有多少个子数组满足如下情况:
max(arr[i..j]) - min(arr[i..j]) <= num
max(arr[i..j])表示子数组arr[i..j]中的最大值，
min(arr[i..j])表示子数组arr[i..j]中的最小值。如果数组长度为 N，请实现时间复杂度为 O(N)的解法。
'''

from deque import deque

class Solution:
    def __init__(self):
        pass

    def getSubArray(self, arr, num):
        result = []
        qmax, qmin = deque(), deque()
        i, j = 0, 0
        while i < len(arr):
            while j < len(arr):

                j += 1

if __name__ == '__main__':
    mSolution = Solution()
    arr = [4,3,5,4,3,3,6,7]
    num = 2
    result = mSolution.getSubArray(arr, num)
    print result