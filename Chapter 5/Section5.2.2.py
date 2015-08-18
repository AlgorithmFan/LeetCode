#!usr/bin/env python
#coding:utf-8

'''
Construct Binary Tree from Inorder and Postorder Traversal
Given inorder and postorder traversal of a tree, construct the binary tree.
Note: You may assume that duplicates do not exist in the tree.
'''

from TreeNode import TreeNode

class Solution:
    def __init__(self):
        pass

    def buildTree(self, postorder, inorder):
        if len(postorder) == 0:
            return None


        root = TreeNode(postorder[-1])
        left_num = inorder.index(postorder[-1])

        root.left = self.buildTree(postorder[:left_num], inorder[:left_num])
        root.right = self.buildTree(postorder[left_num:-1], inorder[left_num+1:])
        return root

if __name__ == '__main__':
    postorder = [9, 15, 7, 20, 3]
    inorder = [9, 3, 15, 20, 7]

    mSolution = Solution()
    root = mSolution.buildTree(postorder, inorder)
    root.show()
