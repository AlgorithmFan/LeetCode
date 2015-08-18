#!usr/env/python
#coding:utf-8

class stack:
    def __init__(self):
        self.nodes = list()

    def empty(self):
        if len(self.nodes):
            return False
        else:
            return True

    def push(self, node):
        self.nodes.append(node)

    def pop(self):
        del self.nodes[-1]

    def top(self):
        return self.nodes[-1]

