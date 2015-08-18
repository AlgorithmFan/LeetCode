#!usr/bin/env python
#coding:utf-8

'''
Given two strings, find the common substring of these two strings.
Note: Be careful for the difference between common substring and common sequences.
'''

class Solution:
    def __init__(self):
        pass

    def findCommonSubString(self, str1, str2):
        result = [[0 for j in range(len(str2)+1)] for i in range(len(str1)+1)]
        max_value, max_i, max_j = 0, 0, 0

        for i in range(len(str1)):
            for j in range(len(str2)):
                if str1[i] == str2[j]:
                    result[i+1][j+1] = result[i][j] + 1
                else:
                    result[i+1][j+1] = 0
                if result[i+1][j+1] > max_value:
                    max_value = result[i+1][j+1]
                    max_i = i
                    max_j = j

        path = []
        while max_i>=0 and max_j>=0:
            path.insert(0, str1[max_i])
            max_i -= 1
            max_j -= 1
        return path

if __name__ == '__main__':
    str1 = 'ab2c3deg1fg'
    str2 = 'degf23abck'
    mSolution = Solution()
    path = mSolution.findCommonSubString(str1, str2)
    print path

