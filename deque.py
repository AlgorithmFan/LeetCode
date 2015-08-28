#!usr/bin/env python
#coding:utf-8

class deque:
    def __init__(self):
        self.data = list()

    def push_front(self, val):
        self.data.insert(0, val)

    def push_back(self, val):
        self.data.append(val)

    def pop_front(self):
        del self.data[0]

    def pop_back(self):
        del self.data[-1]

    def front(self):
        return self.data[0]

    def back(self):
        return self.data[-1]

    def size(self):
        return len(self.data)