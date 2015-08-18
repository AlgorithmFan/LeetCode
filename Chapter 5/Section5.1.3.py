#!usr/bin/env python
#coding:utf-8

'''
5.1.3 Binary Tree Zigzag level order traversal
Given a binary level, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left
for the next level and alternate between).
For example: Given binary tree {3, 9, 20, #, #, 15, 7}
return its zigzag level order traversal as:
[
 [3],
 [20, 9],
 [15, 7],
]
'''
from TreeNode import TreeNode
class Solution:
    def __init__(self):
        pass

    def levelOrderZigZagRecursive(self, root):
        result = list()
        self.traversal(root, 1, result, False)
        return result

    def traversal(self, root, level, result, left_to_right):
        if root is None:
            return

        if level > len(result):
            result.append(list())

        if not left_to_right:
            result[level-1].append(root.val)
        else:
            result[level-1].insert(0, root.val)
        self.traversal(root.left, level+1, result, not left_to_right)
        self.traversal(root.right, level+1, result, not left_to_right)

        return result

    def levelOrderZigZagIteration(self, root):
        result = list()
        left_to_right = True
        current, next = list(), list()
        current.append(root)
        while len(current):
            level = []
            for node in current:
                level.append(node.val)
                if node.left is not None:
                    next.append(node.left)
                if node.right is not None:
                    next.append(node.right)
            if left_to_right:
                result.append(level)
            else:
                result.append(level[::-1])
            left_to_right = not left_to_right
            current = next
            next = list()
        return result


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

    mSolution = Solution()
    result = mSolution.levelOrderZigZagRecursive(root)
    print result

    result = mSolution.levelOrderZigZagIteration(root)
    print result