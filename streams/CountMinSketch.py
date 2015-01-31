# -*- Mode: Python -*-

# estimate top k from a stream using a 'count-min' sketch and heap.
# based on https://github.com/ezyang/ocaml-cminsketch

# also, compare to the 'space saving' algorithm.
# see: http://dimacs.rutgers.edu/~graham/pubs/papers/freqvldbj.pdf

import math
import random
import sys

int_size = len (bin (sys.maxint)) - 1
int_mask = (1 << int_size) - 1

# strange that although C has a log2 in libm, neither python or ocaml does.
def log2 (x):
    return math.log (x) / math.log (2.0)

# hah, in ocaml this *needs* to overflow the int
def multiply_shift (m, a, x):
    return ((a * x)&int_mask) >> (int_size - m)

def random_odd_int():
    n = int (random.getrandbits (int_size-2))
    return n<<1|1

class sketch:
    def __init__ (self, k, depth, width):
        # round up the width to a power of 2
        m = int (math.ceil (log2 (float (width))))
        rounded_width = 1 << m
        self.k = k
        self.lg_width = m
        self.count = [ [0] * rounded_width for x in range (depth) ]
        self.hash_functions = [ random_odd_int() for x in range (depth) ]
        self.heap = []
        self.map = {}

    def update (self, key, c):
        ix = abs (hash (key))
        est = sys.maxint
        for i in range (len (self.hash_functions)):
            hf = self.hash_functions[i]
            j = multiply_shift (self.lg_width, hf, ix)
            x = self.count[i][j]
            est = min (est, x)
            self.count[i][j] = (x + c)
        self.update_heap (key, est)

    def update_heap (self, key, est):
        if not self.heap or self.heap[0][0] < est:
            probe = self.map.get (key, None)
            if probe is None:
                if len(self.map) < self.k:
                    # still growing...
                    entry = [est, key]
                    heapq.heappush (self.heap, entry)
                    self.map[key] = entry
                else:
                    # push this guy out
                    entry = [est, key]
                    [oest, okey] = heapq.heappushpop (self.heap, entry)
                    del self.map[okey]
                    self.map[key] = entry
            else:
                probe[0] = est
                heapq.heapify (self.heap)
        else:
            pass

    def get (self, key):
        ix = abs (hash (key))
        r = sys.maxint
        for i in range (len (self.hash_functions)):
            hf = self.hash_functions[i]
            j = multiply_shift (self.lg_width, hf, ix)
            r = min (r, self.count[i][j])
        return r

    def get_ranking (self):
        vals = self.map.values()
        vals.sort()
        vals.reverse()
        r = {}
        for i in range (len (vals)):
            r[vals[i][1]] = i
        return r

def make_sketch (epsilon, delta):
    assert (epsilon > 0.0)
    assert (delta < 1.0)
    assert (delta > 0)
    depth = int_ceil (log (1.0 / delta))
    width = int_ceil (math.e / epsilon)
    return sketch (depth, width)

import heapq
class space_saver:
    def __init__ (self, n):
        self.size = n
        self.heap = []
        self.map = {}

    def update (self, key, val):
        probe = self.map.get (key, None)
        if probe is None:
            if len (self.map) < self.size:
                # still growing...
                entry = [val, key, 0]
                self.map[key] = entry
                heapq.heappush (self.heap, entry)
            else:
                # ok, not monitored, so evict the smallest element
                # also, lie about the value for entry.
                [vs, ks, e] = heapq.heappop (self.heap)
                entry = [val + vs, key, vs]
                heapq.heappush (self.heap, entry)
                del self.map[ks]
                self.map[key] = entry
        else:
            probe[0] += val
            heapq.heapify (self.heap)

# make a sketch of a squid log file
def test_squid (path):
    check = {}
    s = sketch (200, 20, 500)
    ss = space_saver (200)
    f = open (path, 'rb')
    n = 1000
    while 1:
        n -= 1
        line = f.readline()
        if not line:
            break
        parts = line.split()
        bytes = int (parts[4])
        ip = parts[2]
        check.setdefault (ip, 0)
        if count_bytes:
            s.update (ip, bytes)
            ss.update (ip, bytes)
            check[ip] += bytes
        else:
            s.update (ip, 1)
            ss.update (ip, 1)
            check[ip] += 1
    return s, ss, check

def compare (s, ss, check):
    l = check.items()
    l = [ (y, x) for (x, y) in l ]
    l.sort()
    s_rank = s.get_ranking()
    for bytes, ip in l:
        n0 = s.get (ip)
        n = check[ip]
        if ss.map.has_key (ip):
            entry = ss.map[ip]
            n1 = entry[0] - entry[2]
        else:
            n1 = 0
        if s.map.has_key (ip):
            n2 = s_rank[ip] + 1
        else:
            n2 = 0
        print '%20s %10d %10d %.2f %10d %4d' % (ip, n, n0, (n0 - n)/float(n), n1, n2)

if __name__ == '__main__':
    import sys
    if '-b' in sys.argv:
        sys.argv.remove ('-b')
        count_bytes = 1
    else:
        count_bytes = 0
    path = sys.argv[1]
    s, ss, c = test_squid (path)
    compare (s, ss, c)
