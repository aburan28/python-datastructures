"""Binomial Heap
"""

import sys

class BinomialHeapNode:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.degree = 0
        self.child = None
        self.sibling = None


class BinomialHeap:
    def __init__(self):
        self.head = None



def make_heap():
    return BinomialHeap()

def make_node(key):
    return BinomialHeapNode(key)

def is_empty(H):
    return H.head == None

def minimum(H):
    y = H.head
    if y != None:
        min = y.key
        x = y.sibling
        while x != None:
            if x.key < min:
                min = x.key
                y = x
            x = x.sibling
    return y



def __link(x, y):
    """Link the binomial tree rooted at x to that rooted at y.

    y becomes x's parent.

    """
    x.sibling = y.child
    x.parent = y
    y.child = x
    y.degree = y.degree + 1

def __merge(Hx, Hy):
    """Merge H1 with H2 and return the root of the merged list.

    Binomial Heap Merge merges the root lists of H1 and H2 into a
    single linked list that is sorted by degree into monotonically
    increasing order.

    """
    class SiblingWrapper:
        sibling = None
    x = Hx.head
    y = Hy.head
    h = SiblingWrapper() # head
    t = h        # tail
    while x != None and y != None:
        if x.degree <= y.degree:
            t.sibling = x
            t = x
            x = x.sibling
        else:
            t.sibling = y
            t = y
            y = y.sibling
    if x != None:
        t.sibling = x
    else:
        t.sibling = y
    return h.sibling

def __union(H1, H2):
    H = BinomialHeap()
    H.head = __merge(H1, H2)
    if H.head == None:
        return H
    w = None
    x = H.head
    while x.sibling != None:
        if x.degree != x.sibling.degree or (x.sibling.sibling != None and x.sibling.sibling.degree == x.degree):
            w = x
            x = x.sibling
        else:
            if x.key <= x.sibling.key:
                y = x.sibling
                z = y.sibling
                x.sibling = z
                __link(y, x)
            else:
                y = x.sibling
                if w != None:
                    w.sibling = y
                else:
                    H.head = y
                __link(x, y)
                x = y
    return H

def __print_siblings(x):
    while x != None:
        print x.degree,
        x = x.sibling
    print

def insert(H, x):
    S = BinomialHeap()
    S.head = x
    T = __union(H, S)
    H.head = T.head

def extract(H):
    """Extract the minimum node from H."""
    if H.head == None:
        return None
    # Find the root with min key and remove it.
    prev = None
    min = H.head
    w = min
    x = min.sibling
    while x != None:
        if x.key < min.key:
            prev = w
            min = x
        w = x
        x = x.sibling
    if prev != None:
        assert(prev.sibling == min)
        prev.sibling = min.sibling
    else:
        assert(H.head == min)
        H.head = min.sibling

    # Make S a heap consisting of min's children.  We need to reverse
    # the order of the children as they are stored in decreasing
    # degrees.  This is done by inserting the children to the head of
    # the linked list headed by S.head.
    S = BinomialHeap()
    x = min.child
    while x != None:
        x.parent = None
        y = x.sibling # save the next child
        x.sibling = S.head
        S.head = x
        x = y

    # Union S with H and update H.head.
    T = __union(H, S)
    H.head = T.head

    # Clean up min and return it.
    min.sibling = None
    min.child = None
    min.degree = 0
    min.parent = None
    return min

def decrease_key(H, x, k):
    assert(k <= x.key)
    if k == x.key:
        return # do nothing
    x.key = k
    y = x
    z = y.parent
    while z != None and y.key < z.key:
        #print "Swapping %d and %d." % (y.key, z.key)
        y.key, z.key = z.key, y.key
        y = z
        z = y.parent

def delete(H, x):
    min = minimum(H)
    decrease_key(H, x, min.key-1)
    extract(H)

######################################################################

def print_heap(x, indent='#', char='#'):
    while x != None:
        print "%s %d [%d]" %(indent, x.key, x.degree)
        if x.child != None:
            print_heap(x.child, indent+char, char)
        x = x.sibling

def test():
    #data = [31,40,50,37,45,60,65,73,23,76]
    #data = [10,20,30,40,50,60,70,80,90]
    data = [30,10,90,80,60,70,20,50,40]
    #data = [3,3,2,1,8,3,7]

    print "Input data:", data

    print """
    We print out the state of the heap as each data item is wrapped in
    a node and inserted into the heap.  Depth of the tree is indicated
    by the indentation.  The first number is the key, and the number
    in square brackets the degree of the node.
    """

    min = None
    max = None
    nodes = []
    H = BinomialHeap()
    for d in data:
        print "---------------------------------------- insert (%2d) ---"%(d)
        n = BinomialHeapNode(d)
        if min == None or n.key < min.key:
            min = n
        if max == None or n.key > max.key:
            max = n
        nodes.append(n)
        insert(H, n)
        print_heap(H.head, 'o', '->')

    print "min.key = %d, max.key = %d" % (min.key, max.key)

    print """
    Extract len(data)/2 items from the heap.  As each item is
    extracted, we print the value of the key extracted and the state
    of the heap.
    """

    for i in xrange(len(data)/2):
        n = extract(H)
        d = n.key
        print "---------------------------------------- extracted (%2d) ---"%(d)
        print_heap(H.head, 'o', '->')

    print """
    Now we decrease the key of the max node to that of the original min node.
    """

    decrease_key(H, max, min.key)
    print_heap(H.head, 'o', '->')

    print """
    And then extract the min again.  Which should be %d.
    """ % (min.key)

    n = extract(H)
    d = n.key
    print "---------------------------------------- extracted (%2d) ---"%(d)
    print_heap(H.head, 'o', '->')
    

if __name__ == '__main__':
    test()
