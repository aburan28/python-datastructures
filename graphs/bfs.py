

from graph import *
from Queue import Queue 


class BFSResults:
    def __init__(self):
        self.level = dict()
        self.parent = dict()

def breadth_first_search(graph, start, goal):
	"""
	
	"""
    level = Queue()
    level.put(start)
    came_from = {}
    came_from[start] = None
    
    while not level.empty():
        current = level.get()
        
        if current == goal:
            break
        
        for next in graph.neighbors(current):
            if next not in came_from:
                level.put(next)
                came_from[next] = current
    
    return came_from
