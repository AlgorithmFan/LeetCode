#!usr/bin/env python
#coding:utf-8

'''
☆☆☆
Given a string s, partition s such that every substring of the partition is a palindrome.
Return the minimum cuts needed for a palindrome partitioning of s.
For example, given s = 'aab',
Return 1 since the palindrome partitioning ['aa', 'b'] could be produced using 1 cut.
分析：给定一个字符串s，将s分成多个回文字符，返回最少的分割次数
最多有n-1次分割，然后从0扫描到n-1，发现可以合并的，就从n-1减去1
'''

class Solution:
    def __init__(self):
        pass

    def minCut(self, s):
        len_str = len(s)
        f = [len_str-1-i for i in range(len_str+1)]
        p = [[False for j in range(len_str)] for i in range(len_str)]
        for i in range(len_str-1, -1, -1):
            for j in range(i, len_str):
                if s[i] == s[j] and (j-i<2 or p[i+1][j-1]):
                    p[i][j] = True
                    f[i] = min(f[i], f[j+1]+1)
        return f[0]

if __name__ == '__main__':
    mSolution = Solution()
    s = 'aatbta'
    result = mSolution.minCut(s)
    print result


