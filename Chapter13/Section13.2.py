#!usr/bin/env python
#coding:utf-8

'''
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.
For example. given the array [-2, 1, -3, 4, -1, 2, 1, -5, 4], the contiguous subarray [4, -1, 2, 1] has the largest sum = 6.
最大连续子序列和。
'''

class Solution:
    def __init__(self):
        pass

    def maxSubArrayDP(self, A):
        '''Dynamic Programming.'''
        len_A = len(A)
        result = [0 for i in range(len_A)]
        result[0] = A[0]
        max_value, max_index = A[0], 0
        for i in range(1, len_A):
            result[i] = max(result[i-1]+A[i], A[i])
            if result[i] > max_value:
                max_value = result[i]
                max_index = i
        path = []
        for i in range(max_index, -1, -1):
            max_value -= A[i]
            path.insert(0, A[i])
            if max_value == 0:
                break

        return path, result[max_index]

if __name__ == '__main__':
    mSolution = Solution()
    A = [3, -2, 1, 3, 4, -1, 2, 1, -5, 4, 5]
    result = mSolution.maxSubArrayDP(A)
    print result
