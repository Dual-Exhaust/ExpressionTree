# ExpressionTree

ExpressionTree builds the postfix and prefix expressions from the entered infix expression and then outputs a binary tree representation of the expression.

# Requirements

 - Python 3.7.x
 - Any Unix installation/virtual environment should work
 - It is the user's responsibility to ensure that Python 3.7.x is installed properly accessible to the environment running ExpressionTree.

# Installation

Make a temporary directory and clone this directory directly into it. You can delete this directory later.

`mkdir tmpdir`
`git clone https://github.com/Dual-Exhaust/expressiontree`

Once you've made sure that the clone was successful, you can install the package directly with pip.

`pip install ./expressiontree`

# buildtree
The package comes with one command, 'buildtree'.
**Usage** :
`buildtree "<expression>"`
\<expression> is an infix expression provided by the user. Spaces and parentheses are allowed in the expression, but it is required that the expression is surrounded by quotation marks.
**Supported Operations**:

 - Multiplication: *
 - Division: /
 - Addition: +
 - Subtraction: -
 - Powers: ^

As long as the expression that is passed by the user is a proper expression, buildtree will return results.

**Output**:
The command outputs the original infix expression provided, the postfix and prefix equivalents of the expression, the binary expression tree that represents the expression and also the result (if the operands passed were single digit integers). If any character is included in the expression that is not an operator and not a single digit integer, buildtree will not be able to calculate a result and only the equations and binary tree will be printed. 

The binary tree prints sideways, with the right-most node at the top and the left-most node at the bottom.

> Written with [StackEdit](https://stackedit.io/).
