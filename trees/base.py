














class Node(object):
    __slots__ = ('left','right','root','key','value')
    def __init__(self,key,value):
        self.root = True
        self.left = None
        self.right = None
        self.value = value



class Graph(object):
    def __init__(self):
        self.nodes = list()


    def preorder(self,node, visitor = printwithspace):
        if node is not None:
            visitor(node.data)
            self.preorder(node.left, visitor)
            self.preorder(node.right, visitor)

    def inorder(self,node, visitor = printwithspace):
        if node is not None:
            inorder(node.left, visitor)
            visitor(node.data)
            inorder(node.right, visitor)

    def postorder(self,node, visitor = printwithspace):
        if node is not None:
            postorder(node.left, visitor)
            postorder(node.right, visitor)
            visitor(node.data)




class Vertex(object):

    def __init__(self):
        self



    def add_edge(self):




    def add_weight(self, weight=0):

