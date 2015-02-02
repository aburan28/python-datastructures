# -*- coding:utf-8 -*-



class Stack(object):
    __slots__ = ('items')
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self,item):
        self.items.append(item)


    def pop(self):
        return self.items.pop()

    def peeks(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return lem(self.items)