# -*- coding:utf-8 -*-

__author__ = 'Adam Buran'

__all__ = []





class ALDirectedGraph(object):
    def __init__(self):
        self.Adj = {}
    def itervertices(self):
        """Iterate all vertices in the graph in arbitrary order."""
        return self.Adj.iterkeys()

    def add_vertex(self, u):
        """Add a vertex to the graph.

        A vertex can be any hashable object, e.g., an integer or a tuple.

        Time: O(1).
        """
        if u in self.Adj: raise 'vertex %r already in graph' % u
        self.Adj[u] = set()

    def remove_vertex(u):
        """Remove specified vertex from the graph.

        This operation removes all outgoing edges from the vertex,
        but does not remove incoming edges to the vertex.
        (In this data structure, there is no fast way to find them.)
        You should remove such edges before removing the vertex.

        Time: O(1).
        """
        del self.Adj[u]

    def add_edge(self, u, v):
        """Add an edge from vertex u to vertex v.

        Adds the vertices to the graph if they are not already in it.

        Time: O(1).
        """
        if u not in self.Adj:
            self.add_vertex(u)
        self.Adj[u].add(v)
        if v not in self.Adj:
            self.add_vertex(v)
    def remove_edge(self, u, v):
        """Remove the edge from u to v.

        Time: O(1).
        """
        self.Adj[u].remove(v)
    def neighbors(self, u):
        """Return the set of neighbors of (vertices adjacent to) u.

        Time: O(1).
        """
        return self.Adj[u]


class Graph:

    def __init__(self,edges,weights):
        self.edges = {}
        self.weights = {}


class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedTo[nbr]





class Vertex:



