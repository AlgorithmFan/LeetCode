#!usr/bin/env python
#coding:utf-8

'''
Flatten Binary Tree to Linked List
Given a binary tree, flatten it to a linked list in-place.
For example, Given
   1
2     5
3 4      6
The flattened tree should look like:
1 - 2 - 3 - 4
'''

from TreeNode import TreeNode

class Solution:
    def __init__(self):
        pass

    def flatten(self, root):
        if root is None:
            return

        self.flatten(root.left)
        self.flatten(root.right)

        p = root.left
        while p.right is not None:
            p = p.right
        p.right = root.right
        root.right = root.left
        root.left = None


