#!usr/bin/env python
#coding:utf-8

'''
Given a binary tree, determine if it is height-balanced.
For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every
node never differ by more than 1.
平衡二叉树：它是一棵空树或它的左右两个子树的高度差的绝对值不超过1，并且左右两个子树都是一棵平衡二叉树，常用算法有红黑树、AVL、Treap
伸展树等。
'''

from TreeNode import TreeNode

class Solution:
    def __init__(self):
        pass

    def isBalanced(self, root):
        return self.balancedHeight(root) >= 0

    def balancedHeight(self, root):
        if root is None:
            return 0

        left = self.balancedHeight(root.left)
        right = self.balancedHeight(root.right)

        if left<0 or right<0 or abs(left-right) > 1:
            return -1
        return max(left, right) + 1


if __name__ == '__main__':
    root = TreeNode(3)

    left = TreeNode(19)
    right = None    #TreeNode(9)
    root.left, root.right = left, right

    left = TreeNode(5)
    right = TreeNode(4)
    root.left.left, root.left.right = left, right

    # left = TreeNode(4)
    # right = TreeNode(5)
    # root.right.left, root.right.right = left, right

    mSolution = Solution()
    result = mSolution.isBalanced(root)
    print result
