

import heapq




class MinHeap(object):
    def __init__(self,key,data=()):
        self.key = key
        self.heap = [(self.key(d),d) for d in data]
        heapq.heapify(self.heap)


    def push (self,item):


    def pop (self):
        value = heapq.heappop(self.heap)
        return value[1]



