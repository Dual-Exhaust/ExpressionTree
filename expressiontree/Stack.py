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
