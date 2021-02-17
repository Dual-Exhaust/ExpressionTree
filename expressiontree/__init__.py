import math

# Prints the data for the tree
def printdata(expression):
    # Initialize the variable we append output to
    output = ''
    # Removes any spaces from the input expression
    exp = ''.join(expression.split(' '))
    # Add infix expression to output (it is just the input we took and removed spaces from)
    output += ('INFIX: ' + exp)
    # create the interpreter and pass it the expression
    interpreter = Interpreter(exp)
    # adds the postfix expression to output using the interpreter
    output += ('\nPOSTFIX: ' + interpreter.getpostfix())
    # adds the prefix expression to output using the interpreter
    output += ('\nPREFIX:: ' + interpreter.postfixtoprefix(interpreter.getpostfix()))
    # TreeBuilder uses the postfix expression to build the tree, creates treebuilder object
    treebuilder = TreeBuilder(interpreter.getpostfix())

    # data is the root node of the tree
    data = treebuilder.gettreerootnode()
    # checks if the tree is solvable (no letters or symbols were used as operands)
    if data.getsolvable():
        # if it is solvable we want to add the result to the output
        output += '\nRESULT: ' + str(data.calculateresult())
    else:
        # if not solvable we state as such
        output += '\nExpression entered is not solvable.'

    output += '\n============================'
    # actually gets the tree output string and adds it to our output
    output += data.printtreefromroot()
    output += '\n============================\n'
    # return the output that was just built
    return output

# The node object that the tree holds, represents individual values
class Node:
    # initialize with default values
    def __init__(self, value=None, id=-1, solve=True):
        # value of node
        self.value = value
        # node - left child
        self.left = None
        # node - right child
        self.right = None
        # Set to differentiate nodes, only used in __str__()
        self.ID = id
        # if the node serves as a root of a tree, is the expression solvable
        # this is only used as a check for the real root of the tree
        # probably does not function correctly if checked from any other node in the tree
        # it is only solvable if the operands are not symbols or letters
        self.solvable = solve
    
    # used to set if the node as a root of the tree, has a tree that is solvable
    def setsolvable(self, solve):
        self.solvable = solve

    # return if solvable
    def getsolvable(self):
        return self.solvable

    # return the left child as a node or None
    def getleftchild(self):
        return self.left

    # sets the left child as a given node
    def setleftchild(self, node):
        self.left = node

    # return the right child as a node or None
    def getrightchild(self):
        return self.right

    # sets the right child as a given node
    def setrightchild(self, node):
        self.right = node

    # returns the value of this node
    def getvalue(self):
        return self.value

    # sets the value of this node
    def setvalue(self, value):
        self.value = value

    # Prints the expression tree horizontally rather than vertically.
    # The deeper the layer is in the tree, the higher the spacemultiplier is when we pass the command.
    # Because the expression tree is being printed horizonally, left to right,
    # we process the tree with a reverse in-order traversal (RIGHT ROOT LEFT).
    # The layer spacing is a tab (4 spaces) multiplied by the layer number itself.
    # The root node is at layer 0.
    # All that is used for is the relational spacing between layers.
    # If the default for spacemultipier is more than zero, the tree will be printed more to the right in the console, 
    # it is just the space offset of the whole tree
    # method is recursive and base case is a node with no children
    def printtreefromroot(self, spacemultiplier=0):
        output = ''
        # Two children
        if not (self.getleftchild() is None or self.getrightchild() is None):
            # We add the right-most node first
            output += self.getrightchild().printtreefromroot(spacemultiplier + 1)
            # add the root node value
            output += ('\n' + '    ' * spacemultiplier + self.getvalue())
            # add the left-most node last
            output += self.getleftchild().printtreefromroot(spacemultiplier + 1)
        # No children
        elif self.getleftchild() is None and self.getrightchild() is None:
            # If the node has no children just add the node's value to output
            output += ('\n' + '    ' * spacemultiplier + self.getvalue())
        # return the tree as a string value
        return output

    # calculates the results of an expression if it was solvable
    # recursive method with base case that both children are operands, returns float values
    # if node is an operator we call calculateresult on it
    # if node is an operand we call getvalue instead
    def calculateresult(self):
        # operators we support, used to check if a nodes value is an operator or not
        operators = ['+', '-', '/', '*', '^']
        # if the equation is solvable, redundant check (we check in the printdata method from earlier)
        if self.solvable:
            # Two children
            # Demorgan's wooo
            if not (self.getleftchild() is None or self.getrightchild() is None):
                # If both children are operands
                if not (self.getleftchild().getvalue() in operators or self.getrightchild().getvalue()  in operators):
                    if self.getvalue() == '+':
                        return float(self.getleftchild().getvalue()) + float(self.getrightchild().getvalue())
                    if self.getvalue() == '-':
                        return float(self.getleftchild().getvalue()) - float(self.getrightchild().getvalue())
                    if self.getvalue() == '/':
                        return float(self.getleftchild().getvalue()) / float(self.getrightchild().getvalue())
                    if self.getvalue() == '*':
                        return float(self.getleftchild().getvalue()) * float(self.getrightchild().getvalue())
                    if self.getvalue() == '^':
                        return math.pow(float(self.getleftchild().getvalue()), float(self.getrightchild().getvalue()))
                # If left child is operand and right is operator
                if self.getleftchild().getvalue() not in operators and self.getrightchild().getvalue() in operators:
                    if self.getvalue() == '+':
                        return float(self.getleftchild().getvalue()) + float(self.getrightchild().calculateresult())
                    if self.getvalue() == '-':
                        return float(self.getleftchild().getvalue()) - float(self.getrightchild().calculateresult())
                    if self.getvalue() == '/':
                        return float(self.getleftchild().getvalue()) / float(self.getrightchild().calculateresult())
                    if self.getvalue() == '*':
                        return float(self.getleftchild().getvalue()) * float(self.getrightchild().calculateresult())
                    if self.getvalue() == '^':
                        return math.pow(float(self.getleftchild().getvalue()),
                                        float(self.getrightchild().calculateresult()))
                # If left child is operator and right is operand
                if self.getleftchild().getvalue() in operators and self.getrightchild().getvalue() not in operators:
                    if self.getvalue() == '+':
                        return float(self.getleftchild().calculateresult()) + float(self.getrightchild().getvalue())
                    if self.getvalue() == '-':
                        return float(self.getleftchild().calculateresult()) - float(self.getrightchild().getvalue())
                    if self.getvalue() == '/':
                        return float(self.getleftchild().calculateresult()) / float(self.getrightchild().getvalue())
                    if self.getvalue() == '*':
                        return float(self.getleftchild().calculateresult()) * float(self.getrightchild().getvalue())
                    if self.getvalue() == '^':
                        return math.pow(float(self.getleftchild().calculateresult()),
                                        float(self.getrightchild().getvalue()))
                # If left child is operator and right is operator
                if self.getleftchild().getvalue() in operators and self.getrightchild().getvalue() in operators:
                    if self.getvalue() == '+':
                        return float(self.getleftchild().calculateresult()) + float(
                            self.getrightchild().calculateresult())
                    if self.getvalue() == '-':
                        return float(self.getleftchild().calculateresult()) - float(
                            self.getrightchild().calculateresult())
                    if self.getvalue() == '/':
                        return float(self.getleftchild().calculateresult()) / float(
                            self.getrightchild().calculateresult())
                    if self.getvalue() == '*':
                        return float(self.getleftchild().calculateresult()) * float(
                            self.getrightchild().calculateresult())
                    if self.getvalue() == '^':
                        return math.pow(float(self.getleftchild().calculateresult()),
                                        float(self.getrightchild().calculateresult()))
    # override
    # forces str casting to return a string containing the node value
    def __str__(self):
        return str(self.getvalue())

# a stack class that we can use for interpreting expressions
class Stack:
    def __init__(self):
        # Keeps track of the top of the stack
        self.top = -1
        # A standard python list object we are writing methods to adapt it as a stack
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
        # increase size
        self.top += 1
        # add element
        self.stack.append(element)


class Interpreter:
    def __init__(self, expression):
        # join statement removes all blankspace in the expression passed in, redundant (we do this in printdata as well)
        self.infix = ''.join(expression.split(' '))
        # postfix is None to start
        self.postfix = None
        # Operators and their precedences in a dict
        self.operators = {'+': 0, '-': 0, '/': 1, '*': 1, '^': 2}
        # output starts as nothing
        self.output = ''
        # Stack is a modified list
        self.stack = Stack()
        
        # on initialization set self.postfix
        self.infixtopostfix()

    # return postfix expression
    def getpostfix(self):
        return self.postfix

    # Check if the precedence of operator is less than top of stack or not
    def notgreater(self, char):
        try:
            # a is the integer prepresentation of the precedence for the operator we have
            a = self.operators[char]
            # b is the integer representation of the precedence for the operator at the top of the stack
            b = self.operators[self.stack.peek()]
            return a <= b
        except KeyError:
            return False

    def infixtopostfix(self):
        # Cycle through each character in the expression
        for char in self.infix:
            # If the character is an operand, add it to output
            if char not in self.operators and not char == '(' and not char == ')':
                self.output += char

            # If the character is an '(', push it to stack
            elif char == '(':
                self.stack.push(char)

            # If the character is a ')', add output from the stack until its pairing '(' is found
            elif char == ')':
                # while the stack has elements and the next item at the top of the stack is not the other parenthese
                while not self.stack.isempty() and self.stack.peek() != '(':
                    # remove the element and add it to the output
                    a = self.stack.pop()
                    self.output += a
                # if we hit the '(' we just pop it from the stack as it is no longer needed
                # if the stack is empty nothing happens because pop does not return if the stack is empty
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

        # our postifx expression is set equal to the output we just created
        self.postfix = self.output

    def postfixtoprefix(self, expression):
        # normal list object, we don't need the extra stack methods for this algorithm
        stack = []

        # maybe use a for each loop here? might be less cluttered
        # cycles through indexes of the expression (represented with a string)
        for x in range(len(expression)):
            # if the char is an operator
            if expression[x] in self.operators:
                # temporary int = top of stack
                # tmp1 and tmp2 are operands
                # use tmp1 = stack.pop()???? why add extra steps?
                # -1 is the last item in the list (aka the top of stack)
                tmp1 = stack[-1]
                # remove item
                stack.pop()
                # temporary int = top of stack
                tmp2 = stack[-1]
                # remove that item
                stack.pop()
                # append to the stack the tiny prefix expression
                stack.append(expression[x] + tmp2 + tmp1)
            # char is an operand, just add it to the stack
            else:
                stack.append(expression[x])
        # initialize output
        out = ''
        # stack now just holds the prefix expression, each element is just a char in the expression 
        for char in stack:
            # add the char to the output
            out += char
        # return the output
        return out

# actually builds the tree, sets the nodes and relationships between them etc
class TreeBuilder:
    # initialize necessary vars
    def __init__(self, expression):
        # postfix expression we need to use to create the tree
        self.postfix = expression
        # root of the tree is None to start
        self.root = None
        # operators we support
        self.operators = ['+', '-', '/', '*', '^']
        # build the tree and set the treerootnode on initialization
        self.buildexpressiontree()

    # returns a node object that is the root of the tree
    def gettreerootnode(self):
        return self.root

    # does the work to build the tree
    def buildexpressiontree(self):
        # stack we use to build the tree
        tempstack = Stack()
        # variable for if it is solvable or not
        solve = True
        # cycle through each char in the postfix expression
        for each in self.postfix:
            # if its an operand
            if each not in self.operators:
                # if the char is not a digit
                if not each.isdigit():
                    # we set solve to False because the expression cannot be solved if the char is a letter or symbol
                    solve = False
                # push a new node to the stack with the value of the operand we checked
                tempstack.push(Node(value=each))
            # if its an operator
            else:
                # create temporary node with the value of the operator
                tmpnode = Node(value=each)
                # pop two operand nodes from the stack and set them as the operator node's children
                # right child is set first because we are popping the children nodes off the back end of the stack
                tmpnode.setrightchild(tempstack.pop())
                tmpnode.setleftchild(tempstack.pop())
                # then we push the new operator node to the stack
                tempstack.push(tmpnode)
        # at the end of the loop the only node left in the stack is the root node of the expression
        # all children are accessible through recursion
        self.root = tempstack.pop()
        # set if the expression is solvable or not, only sets the setting on the root node itself
        # all children nodes will have the default boolean set still
        self.root.setsolvable(solve)
        
    # the following two methods are broken and remain unused
    # they were initially for printing the tree using a breadth first search but the spacing between nodes was not working properly and the horizontal approach was adopted
    '''
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
                    print('\t' * (depth - x + 1) + str(char), end='')

                print()
                currentlvl = nextlvl
                nextlvl = []

    def getdepth(self, node):
        if node is None:
            return 0
        elif node.getleftchild() is not None and node.getrightchild() is not None:
            return max(self.getdepth(node.getleftchild()), self.getdepth(node.getrightchild())) + 1
        else:
            return 1
    '''
