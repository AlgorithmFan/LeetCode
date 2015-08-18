#!usr/bin/env python
#coding:utf-8

class Queue:
    def __init__(self):
        self.nodes = []

    def push(self, node):
        self.nodes.append(node)

    def pop(self):
        del self.nodes[0]

    def front(self):
        return self.nodes[0]

    def empty(self):
        if len(self.nodes) == 0:
            return True
        else:
            return False