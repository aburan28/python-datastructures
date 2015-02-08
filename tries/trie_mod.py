#!/usr/local/cpython-3.4/bin/python

'''A pure python Trie class'''


UNSPECIFIED = object()


def is_char(thing):
    '''Return True iff thing is a string of length 1'''
    if isinstance(thing, str) and len(thing) == 1:
        return True
    else:
        return False


class Trie(object):
    '''A pure python Trie class'''

    __slots__ = ('path', 'value', 'terminal')

    def __init__(self):
        '''
        Construct a Trie.
        Other suitable containers include treaps and red-black trees.
        '''
        self.path = dict()
        self.value = None
        self.terminal = False

    def __setitem__(self, key, value):
        head = key[0]
        if head in self.path:
            node = self.path[head]
        else:
            node = Trie()
            self.path[head] = node

        if len(key) > 1:
            remains = key[1:]
            node.__setitem__(remains, value)
        else:
            node.value = value
            node.terminal = True

    def __delitem__(self, key):
        head = key[0]
        if head in self.path:
            node = self.path[head]
            if len(key) > 1:
                remains = key[1:]
                node.__delitem__(remains)
            else:
                node.terminal = False
                node.value = None
            if len(node) == 0:
                del self.path[head]

    def __getitem__(self, key):
        head = key[0]
        if head in self.path:
            node = self.path[head]
        else:
            raise KeyError(key)
        if len(key) > 1:
            remains = key[1:]
            try:
                return node.__getitem__(remains)
            except KeyError:
                raise KeyError(key)
        elif node.terminal:
            return node.value
        else:
            raise KeyError(key)

    def __contains__(self, key):
        try:
            self.__getitem__(key)
        except KeyError:
            return False
        return True

    def __len__(self):
        #number = 1 if self.terminal else 0
        if self.terminal:
            number = 1
        else:
            number = 0
        for key in self.path.keys():
            number = number + len(self.path[key])
        return number

    def __bool__(self):
        if self.path:
            return True
        else:
            return False

    __nonzero__ = __bool__

    def get(self, key, default=None):
        '''Just like dict_.get()'''
        try:
            return self.__getitem__(key)
        except KeyError:
            return default

    def node_count(self):
        '''Count the nodes in self'''
        number = 0
        for key in self.path.keys():
            number += 1 + self.path[key].node_count()
        return number

    def keys(self, prefix=UNSPECIFIED):
        '''Return the keys in the trie'''
        if prefix is UNSPECIFIED:
            prefix = []
        return self.internal_keys(prefix)

    def in_order(self, prefix=UNSPECIFIED):
        '''Return the keys in the trie'''
        if prefix is UNSPECIFIED:
            prefix = []
        return self.internal_keys(prefix, ordered=True)

    def internal_keys(self, prefix=UNSPECIFIED, seen=UNSPECIFIED, ordered=False):
        '''List keys of trie'''
        if prefix is UNSPECIFIED:
            prefix = []
        if seen is UNSPECIFIED:
            seen = []
        result = []
        if self.terminal:
            is_str = all(is_char(element) for element in seen)
            if is_str:
                val = ''.join(seen)
            else:
                val = seen
            result.append(val)
        if len(prefix) > 0:
            head = prefix[0]
            prefix = prefix[1:]
            if head in self.path:
                nextpaths = [head]
            else:
                nextpaths = []
        else:
            nextpaths = self.path.keys()
            if ordered:
                nextpaths = list(nextpaths)
                nextpaths.sort()
        for key in nextpaths:
            nextseen = []
            nextseen.extend(seen)
            nextseen.append(key)
            result.extend(self.path[key].internal_keys(prefix, nextseen))
        return result

    def __iter__(self):
        # This should be made lazy; the yield is, but the self.keys isn't
        for key in self.keys():
            yield key
        #raise StopIteration

    def __add__(self, other):
        result = Trie()
        result += self
        result += other
        return result

    def __sub__(self, other):
        result = Trie()
        result += self
        result -= other
        return result

    def __iadd__(self, other):
        for key in other:
            self[key] = other[key]
        return self

    def __isub__(self, other):
        for key in other:
            del self[key]
        return self

    def find_min(self):
        '''Find the minimum element of the trie: return its key'''
        list_ = []
        node = self
        while not node.terminal:
            if hasattr(node.path, 'find_min'):
                method = getattr(node.path, 'find_min')
                min_key = method()
            else:
                keys = list(node.path)
                min_key = min(keys)
            list_.append(min_key)
            node = node.path[min_key]
        if all(is_char(element) for element in list_):
            return ''.join(list_)
        else:
            return list_

    def find_max(self):
        '''Find the maximum element of the trie: return its key'''
        list_ = []
        node = self
        while not node.terminal:
            if hasattr(node.path, 'find_max'):
                method = getattr(node.path, 'find_max')
                max_key = method()
            else:
                keys = list(node.path)
                max_key = max(keys)
            list_.append(max_key)
            node = node.path[max_key]
        if all(is_char(element) for element in list_):
            return ''.join(list_)
        else:
            return list_
