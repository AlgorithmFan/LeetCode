#!usr/bin/env python
#coding:utf-8
'''
Given two binary trees, write a function to check if they are equal or not.
Two binary trees are considered equal if they are structurally identical and the nodes have the same value.
'''

from TreeNode import TreeNode

class Solution:
    def __init__(self):
        pass

    def isSameTree(self, p_root, q_root):
        if p_root is None and q_root is None:
            return True

        if p_root is None or q_root is None:
            return False

        return p_root.val == q_root.val and self.isSameTree(p_root.left, q_root.left) and self.isSameTree(p_root.right, q_root.right)

if __name__ == '__main__':
    root = TreeNode(3)

    left = TreeNode(9)
    right = TreeNode(20)
    root.left, root.right = left, right

    left = TreeNode(5)
    right = TreeNode(4)
    root.left.left, root.left.right = left, right

    left = TreeNode(15)
    right = TreeNode(7)
    root.right.left, root.right.right = left, right

    temp_root = root.copy()
    temp_root.val = 1
    root.show()
    print '#' * 50
    temp_root.show()

    mSolution = Solution()
    result = mSolution.isSameTree(root, temp_root)
    print result

