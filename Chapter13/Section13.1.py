#!usr/bin/env python
#coding:utf-8

'''
Given a triangle, find the minimum path from top to bottom. Each step you may move to adjacent numbers on the row below.
'''

class Solution:
    def __init__(self):
        pass

    def minimumTotal(self, triangle):
        sum_triangle = [[0 for j in range(len(triangle[i]))] for i in range(len(triangle))]
        for j in range(len(triangle[-1])):
            sum_triangle[-1][j] = triangle[-1][j]
        for i in range(len(triangle)-2, -1, -1):
            for j in range(len(triangle[i])):
                sum_triangle[i][j] = min(sum_triangle[i+1][j], sum_triangle[i+1][j+1]) + triangle[i][j]
        return sum_triangle[0][0]

if __name__ == '__main__':
    mSolution = Solution()
    triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
    total = mSolution.minimumTotal(triangle)
    print total