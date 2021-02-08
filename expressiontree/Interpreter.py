from expressiontree.Stack import Stack


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
