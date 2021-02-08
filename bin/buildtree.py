#!/usr/bin/python
import sys
from expressiontree import Interpreter, TreeBuilder

try:
    expression = ''.join(sys.argv[1:])
    print('INFIX: ' + expression)
    interpreter = Interpreter(expression)
    print('RESULT: ' + interpreter.getpostfix())
    treebuilder = TreeBuilder(interpreter.getpostfix())
    print('=========================')
    data = treebuilder.gettreerootnode()
    data.printtreefromroot()
except:
    print('The expression entered caused some problems.')
