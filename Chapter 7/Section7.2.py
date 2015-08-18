#!usr/bin/env python
#coding:utf-8

class Solution:
    def __init__(self):
        pass

    def searchInsert(self, A, target):
        left, right = 0, len(A)-1
        if target <= A[0]:
            return left
        if target >= A[-1]:
            return right+1

        while left <= right:
            mid = (left+right)/2
            if target < A[mid]:
                right = mid - 1
            elif target > A[mid]:
                left = mid + 1
            else:
                return mid
        return left

    def searchInsertRecursive(self, A, target):
        if A is None or len(A) == 0:
            return 0

        index = self.searchInsertTargetRecursive(A, 0, len(A)-1, target)
        return index

    def searchInsertTargetRecursive(self, A, left, right, target):
        if left > right:
            return left

        mid = (left+right)/2
        if A[mid] == target:
            return mid
        elif target < A[mid]:
            index = self.searchInsertTargetRecursive(A, left, mid-1, target)
        elif target > A[mid]:
            index = self.searchInsertTargetRecursive(A, mid+1, right, target)
        return index


if __name__ == '__main__':
    A = [7, 8, 9, 10]
    target = 11
    mSolution = Solution()
    index = mSolution.searchInsert(A, target)
    print index

    index = mSolution.searchInsertRecursive(A, target)
    print index
