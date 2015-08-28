#!usr/bin/env python
#coding:utf-8

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class DListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.pre = None
