#!usr/bin/env python
#coding:utf-8

'''
Section 5.1.4 Binary Tree Inorder Traversal
Given a binary tree, return the inorder traversal of its nodes' values.
For example: Given binary tree {1, #, 2, 3},
return [1, 3, 2]
中序遍历
'''

from TreeNode import TreeNode
from stack import stack

class Solution:
    def __init__(self):
        pass

    def inOrderTraversalRecursive(self, root):
        result = list()
        self.traversal(root, result)
        return result

    def traversal(self, root, result):
        if root is None:
            return

        self.traversal(root.left, result)
        result.append(root.val)
        self.traversal(root.right, result)

    def inOrderTraversalIteration(self, root):
        result = list()
        s = stack()
        p = root
        while(p is not None or not s.empty()):
            if p is not None:
                s.push(p)
                p = p.left
            else:
                node = s.top()
                s.pop()
                result.append(node.val)
                p = node.right
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
    result = mSolution.inOrderTraversalRecursive(root)
    print result

    result = mSolution.inOrderTraversalIteration(root)
    print result

