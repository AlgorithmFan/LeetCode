#!usr/bin/env python
#coding:utf-8

'''
描述
    Reverse a linked list from position m to n. Do it in-place and in one-pass.
    For example: Given 1->2->3->4->5->nullptr, m = 2 and n = 4,
    return 1->4->3->2->5->nullptr.
    Note: Given m, n satisfy the following condition: 1  m  n  length of list.
分析
    这题非常繁琐，有很多边界检查，15 分钟内做到bug free 很有难度！
'''

from ListNode import ListNode

class Solution:
    def __init__(self):
        pass

    def reverseBetween(self, head, m, n):
        i = 1
        p1, p2 = head, head
        while i<m-1:
            p1 = p1.next
            p2 = p2.next
            i += 1
        p2 = p2.next
        i += 1
        while i <= n:
            p1.next.next = p2.next
            p2.next = p1.next
            p1.next = p2
            i += 1

if __name__ == '__main__':
    mSolution = Solution()
    arr = [1, 2, 3, 4, 5]
    node = ListNode(-1)
    head = node
    for i in range(len(arr)):
        node.next = ListNode(arr[i])

    head = head.next
    node = head
    while node is not None:
        print node.val
        node = node.next

