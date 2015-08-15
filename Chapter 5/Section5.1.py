#usr/bin/evn python
#coding:utf-8

from TreeNode import TreeNode

isTreeNode = lambda x: x is not None

class Solution:
    def __init__(self):
        pass

    def levelOrderRecursive(self, root):
        result = list()
        self.traverse(root, 1, result)
        return result

    def traverse(self, root, level, result):
        if root is None:
            return
        if level > len(result):
            result.append(list())
        result[level-1].append(root.val)
        self.traverse(root.left, level+1, result)
        self.traverse(root.right, level+1, result)


    def levelOrderIteration(self, root):
        result = list()
        if root is None:
            return
        current, next = list(), list()
        current.append(root)
        while len(current):
            result.append(list())
            for node in current:
                if not isTreeNode(node):
                    continue
                result[-1].append(node.val)
                if isTreeNode(node.left):
                    next.append(node.left)
                if isTreeNode(node.right):
                    next.append(node.right)
            current = next
            next = list()
        return result

if __name__ == '__main__':
    root = TreeNode(3)
    left = TreeNode(9)
    right = TreeNode(20)
    root.left, root.right = left, right
    left = TreeNode(15)
    right = TreeNode(7)
    root.right.left, root.right.right = left, right

    mSolution = Solution()
    result = mSolution.levelOrderRecursive(root)
    print result

    result = mSolution.levelOrderIteration(root)
    print result
