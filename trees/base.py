



__all__ = ['TreeNode','BaseBinaryTree','BinarySearchTree']
def height(node):
  if node is None:
    return -1 
  else:
    return node.height

class BaseBinaryTree(object):


	def __init__(self):
		




	def insert(self,data):
	    if self.data:
	        if data < self.data:
	            if self.leftChild is None:
	                self.leftChild = Node(data)
	            else:
	                self.leftChild.insert(data)
	        elif data > self.data:
	            if self.rightChild is None:
	                self.rightChild = Node(data)
	            else:
	                self.rightChild.insert(data)

	    else:
	        self.data = data

    def lookup(self,data,parent=None):
        """
        Lookup a node containing data and return a node and that node's parent
        :param data:
        :param parent:
        :return:
        """
        if data < self.data:
            if self.leftChild is None:
                return None, None
            return self.leftChild.lookup(data,self)
        elif data > self.data:
            if self.rightChild is None:
                return None,None
            return self.rightChild.lookup(data,self)
        else:
            return self,parent


class 





class TreeNode(object):
    __slots__ = ('leftChild','rightChild','root','key','data','parent')
    def __init__(self,key,data):
        self.parent = None
        self.leftChild = None
        self.rightChild = None
        self.data = data
        self.children = []
    
    def __getitem__(self,key):
    	return self.left if key == 0 else self.right


    def __setitem__(self,key,value):
    	if key == 0:
    		self.left = value
    	else:
    		self.right = value




    @property
    def hasLeftChild(self):
        return self.leftChild

    @property
    def hasRightChild(self):
        return self.rightChild

    @property
    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild (self):
        return self.parent and self.parent.rightChild

    @property
    def isRoot (self):
        return not self.parent

    def isLeaf


   
    def free(self):
    	"""
		"""
    	self.leftChild = None
    	self.rightChild = None
    	self.value = None
    	self.key = None
    def prev_item(self,key):

    	return

    def succ_item(self, key):
    	return 

    def ceiling_item(self,key):

    	return 
    def floor_item(self,key):
    	return





    @property
    def children_count(self):
        return len(self.children)


    def delete(self,data):
        node,parent = self.lookup(data)
        if node is not None:
            children_count = node.children_count()

 def isBinarySearchTree(root):
   numbers = []
   f = lambda node: numbers.append(node.value)

   inorder(root, f)

   for i in range(1, len(numbers)):
      if numbers[i-1] > numbers[i]:
         return False

   return True



def inorder(root, f):
   ''' traverse the tree "root" in-order calling f on the
       associated node (i.e. f knows the name of the field to
       access). '''
   if root.leftChild != None:
      inorder(root.leftChild, f)

   f(root)

   if root.rightChild != None:
      inorder(root.rightChild, f)

def preorder(root, f):
   f(root)
   if root.leftChild != None:
      preorder(root.leftChild, f)

   if root.rightChild != None:
      preorder(root.rightChild, f)

def postorder(root, f):
   if root.leftChild != None:
      postorder(root.leftChild, f)

   if root.rightChild != None:
      postorder(root.rightChild, f)

   f(root)
