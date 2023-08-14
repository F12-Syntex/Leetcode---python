class MinStack(object):


    def __init__(self):
        self.stack = []
        self.minStack = []
        

    def push(self, val):
        self.stack.append(val)

        if self.minStack:
            curr = self.minStack[-1]
            if val < curr:
                self.minStack.append(val)
            else:
                self.minStack.append(curr)
        else:
            self.minStack.append(val)
        
        print(self.stack)
        print(self.minStack)
        print()

    def pop(self):
        self.stack.pop()
        self.minStack.pop()
        

    def top(self):
        return self.stack[-1]
        

    def getMin(self):
        return self.minStack[-1]
        


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(1)
obj.push(2)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()