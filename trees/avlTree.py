from trees.base import BinaryTree, TreeNode


class AVLNode(TreeNode):
    def update_height (self):
        self.height =  max(height(self.left), height(self.right)) + 1
        TreeNode.update_height(self)


class AVLTree(BinaryTree):
    def __init__(self):
        """
        """
        self.root = 1
        BinaryTree.__init__(self, AVLTree)




    def height(self,node):
        """

        """
        if node is None:
            return -1
        else:
            return node.height
    def update_height(self,node):
        """

        """
        node.heigh = max(self.height(node.left), self.height(node.right)) + 1


        
    def rebalance(self,node):
        """

        """
        while node is not None:
            self.update_height(node)
            if self.height(node.left) >= 2 + self.height(node.right):
                if self.height(node.left.left) >= self.height(node.left.right):
                    self.right_rotate(node)
                else:
                    self.left_rotate(node.left)
                    self.right_rotate(node)
            elif self.height(node.right) >= 2 + self.height(node.left):
                if self.height(node.right.right) >= self.height(node.right.left):
                    self.left_rotate(node)
                else:
                    self.right_rotate(node.right)
                    self.left_rotate(node)
            node = node.parent

    def left_rotate(self, x):
        """

        """
        y = x.right
        y.value = x.value
        if y.value is None:
            self.root = y
        else:
            if y.value.left is x:
                y.value.left = y
            elif y.value.right is x:
                y.value.right = y
                x.right = y.left
        if x.right is not None:
            x.right.value = x
            y.left = x
            x.value = y
    def right_rotate(self, x):
        """

        """
        y = x.left
        y.value = x.value
        if y.value is None:
            self.root = y
        else:
            if y.value.left is x:
                y.value.left = y
            elif y.value.right is x:
                y.value.right = y
                x.left = y.right
        if x.left is not None:
            x.left.value = x
            y.right = x
            x.value = y
    def _new_node(self,key,value):
        self._count += 1
        return Node(key, value)

    def insert(self, key,value):
        """

        """
        if self.__root is None:
            self.__root = self._new_node(key,value)
        else:
            node_stack = []
            dir_stack = array('I')
            done = False
            top = 0
            node = self._root

            while True:
                if key == node.key:
                    node.value = value
                    return
                direction = 1 if key > node.key else 0
                dir_stack.append(direction)
                node_stack.append(node)
                if node[direction] is None:
                    break
                node = node[direction]
                top = len(node_stack) - 1
                while (top >= 0) and not done:
                    direction = dir_stack[top]
                    other_side = 1 - direction
                    top_node = node_stack[top]
                    left_height = height(top_node[direction])


                right_height = height(top_node[other_side])
                if left_height - right_height == 0:
                    done = True
                if left_height - right_height >= 2:
                    a = top_node[direction][direction]
                    b = top_node[direction][other_side]
                    if height(a) >= height(b):
                        node_stack[top] = jsw_single(top_node, other_side)
                    else:
                        node_stack[top] = jsw_double(top_node, other_side)


                    if top != 0:
                        node_stack[top - 1][dir_stack[top - ]] = node_stack[top]
                    else:
                        self._root = node_stack[0]
                    done = True


                top_node = node_stack[top]
                left_height = height(top_node[direction])
                right_height = height(top_node[other_side])
                top_node.balance = max(left_height, right_height) + 1
                top -= 1



    def remove(self,key):




                

