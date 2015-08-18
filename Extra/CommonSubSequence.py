#!usr/bin/env python
#coding:utf-8

class Solution:
    def __init__(self):
        pass

    def findCommonSubSequence(self, str1, str2):
        str1_len, str2_len = len(str1), len(str2)
        result = [[0 for j in range(str2_len+1)] for i in range(str1_len+1)]

        for i in range(1, str1_len+1):
            for j in range(1, str2_len+1):
                if str1[i-1] == str2[j-1]:
                    result[i][j] = result[i-1][j-1] + 1
                else:
                    result[i][j] = max(result[i-1][j], result[i][j-1])
        for i, value in enumerate(result):
            print i, value
        sequence = []
        a, b = [], []
        i, j = str1_len, str2_len
        while i>=1 and j>= 1:
            if str1[i-1] == str2[j-1]:
                a.insert(0, str1[i-1])
                b.insert(0, str2[j-1])
                sequence.insert(0, (i-1, j-1))
                i -= 1
                j -= 1
            elif result[i][j] == result[i][j-1]:
                j -= 1
            elif result[i][j] == result[i-1][j]:
                i -= 1
        print a, b
        return sequence

    def findCommonSubSequenceRecursive(self, str1, str2, result):
        len1, len2 = len(str1), len(str2)
        if len1 == 0 or len2 == 0:
            return

        if str1[-1] == str2[-1]:
            result.insert(0, str1[-1])
            self.findCommonSubSequenceRecursive(str1[:-1], str2[:-1], result)
        else:
            r1, r2 = [], []
            self.findCommonSubSequenceRecursive(str1[:-1], str2, r1)
            self.findCommonSubSequenceRecursive(str1, str2[:-1], r2)
            if len(r1) > len(r2):
                for r in r1[::-1]:
                    result.insert(0, r)
            else:
                for r in r2[::-1]:
                    result.insert(0, r)



if __name__ == '__main__':
    str1 = 'ab2c3deg1fg'
    str2 = 'degf23abck'
    mSolution = Solution()
    path = mSolution.findCommonSubSequence(str1, str2)
    print path

    result = []
    mSolution.findCommonSubSequenceRecursive(str1, str2, result)
    print str1
    print str2
    print result