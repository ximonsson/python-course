class BinarySearchTree():
    """
    Binary Search Tree data structure.
    """

    class Node():
        """
        Node class. Defines a node in the tree.

        Points to a value and two children, left and right, that default to
        None. Left child has a smaller value than the node, and the right
        has a larger.
        """

        def __init__(self, value):
            self.value = value
            self.right = None
            self.left  = None

        def __str__(self):
            return """[{}]
  |-- {}
  `-- {}""".format(self.value, self.left, self.right)


        def insert(self, value):
            """
            Insert a value to the node.
            This function is recursive by first trying to inserting the value
            as a child node to this one. If the corresponding child already
            exists it tries to insert at the child instead.
            """
            if value < self.value:
                if self.left is None:
                    self.left = BinarySearchTree.Node(value)
                else:
                    self.left.insert(value)
            elif value > self.value:
                if self.right is None:
                    self.right = BinarySearchTree.Node(value)
                else:
                    self.right.insert(value)


    def __init__(self):
        self.root = None

    def __str__(self):
        return str(self.root)

    def search(self, value):
        """
        Find the node with the given value.
        Returns None is not found.
        """
        node = self.root
        while not node is None and node.value != value:
            if value < node.value:
                node = node.left
            else:
                node = node.right
        return node

    def insert(self, value):
        """
        Insert a value as a new node in the tree.
        """
        if self.root is None:
            self.root = self.Node(value)
        else:
            self.root.insert(value)
