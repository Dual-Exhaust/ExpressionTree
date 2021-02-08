
def printdata(expression):
    exp = ''.join(expression.split(' '))
    print('INFIX: ' + exp)
    interpreter = Interpreter(exp)
    print('POSTFIX: ' + interpreter.getpostfix())
    treebuilder = TreeBuilder(interpreter.getpostfix())
    print('============================')
    data = treebuilder.getrootnode()
    data.printtreefromroot()



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


class Stack:
    def __init__(self):
        # Keeps track of the top of the stack
        self.top = -1
        # A list object we are writing methods to adapt it as a stack
        self.stack = []

    # check if the stack is empty
    def isempty(self):
        return self.top == -1

    # Return the value of the top of the stack
    def peek(self):
        return self.stack[-1]

    # Pop the element from the stack
    def pop(self):
        if not self.isempty():
            self.top -= 1
            # Calls the pop function from the list class, not self.pop()
            return self.stack.pop()

    # Push the element to the stack
    def push(self, element):
        self.top += 1
        self.stack.append(element)


class Interpreter:
    def __init__(self, expression):
        # join statement removes all blankspace in the expression passed in
        self.infix = ''.join(expression.split(' '))
        self.postfix = None
        # Operators and their precedences in a dict
        self.operators = {'+': 0, '-': 0, '/': 1, '*': 1, '^': 2}
        self.output = ''
        # Stack is a modified list
        self.stack = Stack()

        self.infixtopostfix()

    def getpostfix(self):
        return self.postfix

    # Check if the precedence of operator is less than top of stack or not
    def notgreater(self, char):
        try:
            a = self.operators[char]
            b = self.operators[self.stack.peek()]
            return a <= b
        except KeyError:
            return False

    def infixtopostfix(self):
        # Cycle through each character in the expression
        for char in self.infix:
            # If the character is an operand, add it to output.
            if char not in self.operators and not char == '(' and not char == ')':
                self.output += char

            # If the character is an '(', push it to stack.
            elif char == '(':
                self.stack.push(char)

            # If the character is a ')', add output from the stack until its pairing '(' is found
            elif char == ')':
                while not self.stack.isempty() and self.stack.peek() != '(':
                    a = self.stack.pop()
                    self.output += a
                else:
                    self.stack.pop()

            # If an operator is found, add stack values to the output as long as the precendence allows
            # Then push the operator to the stack
            else:
                while not self.stack.isempty() and self.notgreater(char):
                    self.output += self.stack.pop()
                self.stack.push(char)

        # pop all the remaining elements from the stack and add it to the output
        while not self.stack.isempty():
            self.output += self.stack.pop()

        self.postfix = self.output


class TreeBuilder:
    def __init__(self, expression):
        self.postfix = expression
        self.root = None
        self.operators = ['+', '-', '/', '*', '^']
        # build the tree and set the treerootnode on initialization
        self.buildexpressiontree()


    def gettreerootnode(self):
        return self.root

    def buildexpressiontree(self):
        tempstack = Stack()
        for each in self.postfix:
            if each not in self.operators:
                tempstack.push(Node(value=each))
            else:
                tmpnode = Node(value=each)
                tmpnode.setrightchild(tempstack.pop())
                tmpnode.setleftchild(tempstack.pop())
                tempstack.push(tmpnode)
        self.root = tempstack.pop()

    def printbreadthfirst(self):
        currentlvl = []
        nextlvl = []

        nodestack = Stack()

        depth = self.getdepth(self.root)
        # print(depth)

        if self.root is not None:
            nodestack.push(self.root)

            for x in range(depth):
                while not nodestack.isempty():
                    currentlvl.append(nodestack.pop())

                for node in currentlvl:
                    if node.getleftchild() is not None:
                        nextlvl.append(node.getleftchild())

                    if node.getrightchild() is not None:
                        nextlvl.append(node.getrightchild())

                for char in currentlvl:
                    print('\t'*(depth-x+1) + str(char), end='')

                print()
                currentlvl = nextlvl
                nextlvl = []

    def getdepth(self, node):
        if node is None:
            return 0
        elif node.getleftchild() is not None and node.getrightchild() is not None:
            return max(self.getdepth(node.getleftchild()), self.getdepth(node.getrightchild())) + 1;
        else:
            return 1


