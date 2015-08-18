#!usr/bin/env python
#coding:utf-8

'''
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level
from leaf to root).
For example: given binary tree {3, 9, 20, #, #, 15, 7},
return its bottom-up level order traversal as:
[[15, 7], [9, 20], [3],]
'''
from TreeNode import TreeNode

class Solution:
    def __init__(self):
        pass

    def reverseLevelOrderRecursive(self, root):
        result = list()
        self.traverse(root, 1, result)
        return result[::-1]

    def traverse(self, root, level, result):
        if root is None:
            return
        if level>len(result):
            result.append(list())
        result[level-1].append(root.val)
        self.traverse(root.left, level+1, result)
        self.traverse(root.right, level+1, result)


if __name__ == '__main__':
    root = TreeNode(3)
    left = TreeNode(9)
    right = TreeNode(20)
    root.left, root.right = left, right
    left = TreeNode(15)
    right = TreeNode(7)
    root.right.left, root.right.right = left, right

    mSolution = Solution()
    result = mSolution.reverseLevelOrderRecursive(root)
    print result
