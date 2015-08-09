class Queue:
    # initialize your data structure here.
    def __init__(self):
        self.stack = []

    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.stack.append(x)

    # @return nothing
    def pop(self):
        self.stack.pop(0)


    # @return an integer
    def peek(self):
        return self.stack[0]


    # @return an boolean
    def empty(self):
        return len(self.stack) == 0
