#!usr/bin/env python
#coding:utf-8

'''
5、设计可以变更的缓存结构
【题目】
设计一种缓存结构，该结构在构造时确定大小，假设大小为 K，并有两个功能：
1，set(key,value)：将记录(key,value)插入该结构。
2，get(key)：返回key对应的value值。
【要求】
1，set和get方法的时间复杂度为O(1)。
2，某个key的set或get操作一旦发生，认为这个 key 的记录成了最经常使用的。
3，当缓存的大小超过K时，移除最不经常使用的记录，即set或get最久远的。
【举例】
假设缓存结构的实例是cache，大小为3，并依次发生如下行为:
1，cache.set("A",1)。最经常使用的记录为("A",1)。
2，cache.set("B",2)。最经常使用的记录为(“B”,2)，(“A”,1)变为最不经常的。
3，cache.set("C",3)。最经常使用的记录为(“C”,2)，(“A”,1)还是最不经常的。
4，cache.get("A")。最经常使用的记录为(“A”,1)，(“B”,2)变为最不经常的。
5，cache.set("D",4)。大小超过了 3，所以移除此时最不经常使用的记录(“B”,2)，
   加入记录(“D”,4)，并且为最经常使用的记录，然后("C",2)变为最不经常使用的记录。
'''


class DListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.pre = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.curSize = 0
        self.head = DListNode(-1, -1)
        self.tail = DListNode(-1, -1)
        self.head.next = self.tail
        self.tail.pre = self.head
        self.nodes = {}

    def moveToFirst(self, node):
        node.pre = self.head
        node.next = self.head.next
        self.head.next = node
        node.next.pre = node

    def set(self, key, value):
        if key in self.nodes:
            node = self.nodes[key]
            node.val = value
            # 将node两端的节点连接起来
            node.pre.next = node.next
            node.next.pre = node.pre
            self.moveToFirst(node)
        else:
            node = DListNode(key, value)
            self.nodes[key] = node
            self.moveToFirst(node)
            self.curSize += 1
            if self.curSize > self.capacity:
                self.remove_tail()
                self.curSize = self.capacity

    def remove_tail(self):
        node = self.tail.pre
        node.pre.next = self.tail
        self.tail.pre = node.pre
        del self.nodes[node.key]
        del node

    def get(self, key):
        if key in self.nodes:
            node = self.nodes[key]
            self.moveToFirst(node)
            return node.val
        else:
            return -1

if __name__ == '__main__':
    mLRUCache = LRUCache(5)
    for i in range(10):
        mLRUCache.set(i, i+1)
    mLRUCache.set(1, 40)
    for i in range(10):
        print mLRUCache.get(i)
    print mLRUCache.get(1)
    print mLRUCache.head.next.key


