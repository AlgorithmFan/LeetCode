#!usr/bin/env python
#coding: utf-8

'''
Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2.
编辑距离，百度常考
Insert a character
Delete a character
Replace a character
分析：设状态f[i][j]， 表示A[0,i] 和 B[0, j] 之间的最小编辑距离，设A[0,i]的形式是stric, B[0,j]的形式是str2d，
1. 如果 c==d， 则f[i][j] = f[i-1][j-1];
2. 如果 c!=d,
    （1）如果将c替换成d，则f[i][j] = f[i-1][j-1]+1;
    (2) 如果将c后面增加一个d，即将d后移一个位置，则f[i][j] = f[i][j-1] + 1;
    (3) 如果将c删除，则f[i][j] = f[i-1][j] + 1;

'''

class Solution:
    def __init__(self):
        pass

    def minDistrance(self, word1, word2):
        len_word1, len_word2 = len(word1), len(word2)
        f = [[0 for j in range(len_word2+1)] for i in range(len_word1+1)]
        for i in range(len_word1+1):
            f[i][0] = i
        for j in range(len_word2+1):
            f[0][j] = j

        for i in range(1, len_word1+1):
            for j in range(1, len_word2+1):
                if word1[i-1] == word2[j-1]:
                    f[i][j] = f[i-1][j-1]
                else:
                    f[i][j] = min([f[i-1][j-1], f[i-1][j], f[i][j-1]]) + 1
        return f[len_word1][len_word2]

if __name__ == '__main__':
    mSolution = Solution()
    str1, str2 = '23diwces', 'adiwk'
    distance = mSolution.minDistrance(str1, str2)
    print distance