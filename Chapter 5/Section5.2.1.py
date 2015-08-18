#!usr/bin/env python
#coding:utf-8

'''
Construct Binary Tree from Preorder and Inorder Traversal
Given preorder and inorder traversal of a tree, construct the binary tree.
Note: You may assume that duplicates do not exist in the tree.
'''

from TreeNode import TreeNode

class Solution:
    def __init__(self):
        pass

    def buildTree(self, preorder, inorder):
        if len(preorder) == 0:
            return

        root = TreeNode(preorder[0])
        left_num = inorder.index(preorder[0])
        right_num = inorder.index(preorder[0])+1
        root.left = self.buildTree(preorder[1:left_num+1], inorder[:left_num])
        root.right = self.buildTree(preorder[right_num:], inorder[right_num:])
        return root

if __name__=='__main__':
    preorder = [7,10,4,3,1,2,8,11]
    inorder = [4,10,3,1,7,11,8,2]

    mSolution = Solution()
    root = mSolution.buildTree(preorder, inorder)
    root.show()
