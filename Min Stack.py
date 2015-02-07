class MinStack:
    def __init__ (self) :
        self.stack = []
        self.min = []
    # @param x, an integer
    # @return an integer
    def push(self, x):
        self.stack.append(x)
        if self.min == [] :
            self.min.append(x)
        elif self.min[-1] >= x :
            self.min.append(x)

    # @return nothing
    def pop(self):
        tmp = self.stack.pop()
        if tmp == self.min[-1] :
            self.min.pop()

    # @return an integer
    def top(self):
        return self.stack[-1]

    # @return an integer
    def getMin(self):
        return self.min[-1]
