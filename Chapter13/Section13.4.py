#!usr/bin/env python
#coding:utf-8
'''
Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing all ones and return its area.
分析： 找到面积最大的矩阵

'''
class Solution:
    def __init__(self):
        pass

    def maximumRectangle(self, data):
        n, m = len(data), len(data[0])
        ret = 0
        H = [0 for i in range(n)]
        L = [0 for i in range(n)]
        R = [0 for i in range(n)]


        for i in range(n):
            left ,right = 0, n
            for j in range(m):
                if data[i][j] == '1':
                    H[j] += 1
                    L[j] = max(L[j], left)
                else:
                    left = j+1
                    H[j], L[j], R[j] = 0, 0, n
            for j in range(n-1, -1, -1):
                if data[i][j] == '1':
                    R[j] = min(R[j], right)
                    ret = max(ret, H[j]*(R[j]-L[j]))
                else:
                    right = j

