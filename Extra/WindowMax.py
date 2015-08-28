#!usr/bin/env python
#coding:utf-8

'''
1、生成窗口最大值数组
有一个整型数组arr和一个大小为w的窗口从数组的最左边滑到最右边，窗口每次向右边滑一个位置。
例如，数组为[4,3,5,4,3,3,6,7]，窗口大小为3时：

[4 3 5] 4 3 3 6 7 窗口中最大值为5
4 [3 5 4] 3 3 6 7 窗口中最大值为5
4 3 [5 4 3] 3 6 7 窗口中最大值为5
4 3 5 [4 3 3] 6 7 窗口中最大值为4
4 3 5 4 [3 3 6] 7 窗口中最大值为6
4 3 5 4 3 [3 6 7] 窗口中最大值为7

如果数组长度为n，窗口大小为w，则一共产生n-w+1个窗口的最大值。请实现一个函数，给定一个数组arr，窗口大小w。
返回一个长度为n-w+1的数组res,res[i]表示每一种窗口状态下的最大值。以本题为例，结果应该返回[5,5,5,4,6,7]。

分析：使用双队列结构，存储升序序列的索引，并检查双队列的首元素，是否过期。
'''

from deque import deque

class Solution:
    def __init__(self):
        pass

    def getMaxOfWindow(self, arr, w):
        result = [0 for i in range(len(arr)-w+1)]
        i, qmax = 0, deque()
        while i < len(arr):
            while qmax.size() > 0 and arr[qmax.back()] < arr[i]:  # Keep the deque in order
                qmax.pop_back()
            qmax.push_back(i)
            if qmax.front() == i-w:
                qmax.pop_front()
            if i>=w-1:
                result[i-w+1] = arr[qmax.front()]
            i += 1
        return result

if __name__ == '__main__':
    arr = [4,3,5,4,3,3,6,7]
    mSolution = Solution()
    result = mSolution.getMaxOfWindow(arr, 3)
    print result