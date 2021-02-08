class Node:
    def __init__(self, value=None, id=-1):
        self.value = value
        self.left = None
        self.right = None
        # Set to differentiate nodes, only used in __str__()
        self.ID = id

    def getleftchild(self):
        return self.left

    def setleftchild(self, node):
        self.left = node

    def getrightchild(self):
        return self.right

    def setrightchild(self, node):
        self.right = node

    def getvalue(self):
        return self.value

    def setvalue(self, value):
        self.value = value

    # Prints the expression tree horizontally rather than vertically.
    # The deeper the layer is in the tree, the higher the spacemultiplier is when we pass the command.
    # Because the expression tree is being printed horizonally, left to right,
    # we process the tree with a reverse in-order traversal (RIGHT ROOT LEFT).
    # The layer spacing is a tab (4 spaces) multiplied by the layer number itself.
    # The root node is at layer 0.
    # All that is used for is the relational spacing between layers.
    # If the default for spacemultipier is more than zero, the tree will be printed more to the right in the console.
    def printtreefromroot(self, spacemultiplier=0):
        # Two children
        if not (self.getleftchild() is None or self.getrightchild() is None):
            # We print the right-most node first.
            self.getrightchild().printtreefromroot(spacemultiplier + 1)
            # Print the root node value
            print('    ' * spacemultiplier + self.getvalue())
            # Print the left-most node last.
            self.getleftchild().printtreefromroot(spacemultiplier + 1)
        # Base case - no children.
        elif self.getleftchild() is None and self.getrightchild() is None:
            # If the node has no children just print the node's value.
            print('    ' * spacemultiplier + self.getvalue())

    def __str__(self):
        return str(self.getvalue())
