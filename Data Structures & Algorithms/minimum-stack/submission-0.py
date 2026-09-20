class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.min_stack) == 0: # If empty stack
            self.min_stack.append(val) # Append val
        elif val < self.min_stack[-1]: # If val is less than top of min stack, append (new min value)
            self.min_stack.append(val)
        else: # If val is more, push the min value again
            self.min_stack.append(self.min_stack[-1])

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]