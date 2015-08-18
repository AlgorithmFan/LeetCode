#!usr/bin/env python
#coding:utf-8
'''
Given two binary trees, write a function to check if they are equal or not.
Two binary trees are considered equal if they are structurally identical and the nodes have the same value.
'''

from TreeNode import TreeNode
from stack import stack

class Solution:
    def __init__(self):
        pass

    def isSymmetric(self, root):

        return self.childrenAreSymmetric(root.left, root.right)

    def childrenAreSymmetric(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        return left.val == right.val and self.childrenAreSymmetric(left.left, right.right) and self.childrenAreSymmetric(left.right, right.left)

    def isSymmetricIteration(self, root):
        s = stack()
        s.push(root.left)
        s.push(root.right)
        while(not s.empty()):
            p = s.top()
            s.pop()
            q = s.top()
            s.pop()

            if p is None and q is None:
                continue
            if p is None or q is None:
                return False
            if p.val != q.val:
                return False
            s.push(p.left)
            s.push(q.right)
            s.push(p.right)
            s.push(q.left)
        return True


if __name__ == '__main__':
    root = TreeNode(3)

    left = TreeNode(9)
    right = TreeNode(9)
    root.left, root.right = left, right

    left = TreeNode(5)
    right = TreeNode(4)
    root.left.left, root.left.right = left, right

    left = TreeNode(4)
    right = TreeNode(5)
    root.right.left, root.right.right = left, right

    mSolution = Solution()
    result = mSolution.isSymmetric(root)
    print result

    result = mSolution.isSymmetricIteration(root)
    print result
