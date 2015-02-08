

__author__ = 'Adam Buran'
import heapq

__all__ = ['BinaryHeapBase']

class BinaryHeapBase(object):
    def __init__(self, key, data=()):
        self.key = key
        self.heap = [(self.key(d), d) for d in data]
        heapq.heapify(self.heap)

    def push(self, item):
        decorated = self.key(item), item
        heapq.heappush(self.heap, decorated)

    def pop(self):
        decorated = heapq.heappop(self.heap)
        return decorated[1]

    def pushpop(self, item):
        decorated = self.key(item), item
        dd = heapq.heappushpop(self.heap, decorated)
        return dd[1]

    def replace(self, item):
        decorated = self.key(item), item
        dd = heapq.heapreplace(self.heap, decorated)
        return dd[1]

    def __len__(self):
        return len(self.heap)