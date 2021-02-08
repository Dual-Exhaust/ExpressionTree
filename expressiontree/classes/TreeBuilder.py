from Classes.Node import Node
from Classes.Stack import Stack
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


