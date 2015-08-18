#!usr/bin/env python
#coding:utf-8

'''
Given a sorted array of integers, find the starting and ending position of a given target value.
Your algorithm's runtime complexity must be in the order of O(logn).
If the target is not found in the array, return [-1, -1].
For example, Given [5, 7, 7, 8, 8, 10] and target value 8, return [3, 4]
'''

class Solution:
    def __init__(self):
        pass

    def findTargetNumber(self, A, target):
        index = []
        left, right = 0, len(A)-1
        while left<right:
            mid = (left + right) / 2
            if target < A[mid] and target > A[left]:
                right = mid
            elif target > A[mid] and target < A[right]:
                left = mid
            elif target == A[mid]:
                for i in range(mid, left-1, -1):
                    if target == A[i]:
                        index.insert(0, i)
                    else:
                        break
                left = mid
                for i in range(mid+1, right+1):
                    if target == A[i]:
                        index.append(i)
                    else:
                        break
                right = mid
            else:
                break
        if len(index) == 0:
            index = [-1, -1]
        return index

    def findTargetNumberRecursive(self, A, target):
        result = []
        self.findTarget(A, 0, len(A)-1, target, result)
        if len(result) == 0:
            result = [-1, -1]
        return result

    def findTarget(self, A, left, right, target, result):
        if left >= right:
            return

        mid = (left+right)/2
        if target > A[left] and target < A[mid]:
            self.findTarget(A, left, mid, target, result)
        elif target < A[right] and target > A[mid]:
            self.findTarget(A, mid, right, target, result)
        elif target == A[mid]:
            for i in range(mid, left-1, -1):
                if target == A[i]:
                    result.insert(0, i)
                else:
                    break
            for i in range(mid+1, right+1):
                if target == A[i]:
                    result.append(i)
                else:
                    break

if __name__ == '__main__':
    A = [7, 8, 8, 8, 8, 8]
    target = 8
    mSolution = Solution()
    index = mSolution.findTargetNumber(A, target)
    print index

    index = mSolution.findTargetNumberRecursive(A, target)
    print index
