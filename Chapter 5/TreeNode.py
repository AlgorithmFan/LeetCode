#!usr/bin/env python
#coding:utf-8
from Queue import Queue

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def copy(self):
        treeNode = TreeNode(self.val)
        if self.left is not None:
            treeNode.left = self.left.copy()
        else:
            treeNode.left = None
        if self.right is not None:
            treeNode.right = self.right.copy()
        else:
            treeNode.right = None
        return treeNode

    def show(self):
        current = Queue()
        current.push(self)
        num = 1
        while not current.empty():
            line = []
            next_num = 0
            for i in range(num):
                node = current.front()
                current.pop()
                if node is None:
                    line.append('#')
                    continue
                else:
                    line.append(node.val)
                if node.left is not None:
                    current.push(node.left)
                else:
                    current.push(None)
                next_num += 1
                if node.right is not None:
                    current.push(node.right)
                else:
                    current.push(None)
                next_num += 1
            num = next_num
            print line

def preOrderTraversal(root, result):
    if root is None:
        return
    result.append(root.val)
    preOrderTraversal(root.left, result)
    preOrderTraversal(root.right, result)

def inOrderTraversal(root, result):
    if root is None:
        return
    inOrderTraversal(root.left, result)
    result.append(root.val)
    inOrderTraversal(root.right, result)

def postOrderTraversal(root, result):
    if root is None:
        return
    postOrderTraversal(root.left, result)
    postOrderTraversal(root.right, result)
    result.append(root.val)

if __name__ == '__main__':
    root = TreeNode(3)
    left = TreeNode(9)
    right = TreeNode(20)
    root.left, root.right = left, right
    # root.left.right = TreeNode(32)
    left = TreeNode(15)
    right = TreeNode(7)
    root.right.left, root.right.right = left, right

    result = []
    root.show()
    preOrderTraversal(root, result)
    print result

    result = []
    inOrderTraversal(root, result)
    print result

    result = []
    postOrderTraversal(root, result)
    print result
