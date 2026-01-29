class MinStack:

    def __init__(self):
        self.stack = []
        self.minValue = None

    def push(self, val: int) -> None:
        if(self.minValue == None):
            self.minValue = val
            self.stack.append(val)
        elif(self.minValue > val):
            NewVal = 2*val - self.minValue
            self.minValue = val
            self.stack.append(NewVal)
        else:
            self.stack.append(val)

    def pop(self) -> None:
        if not self.stack:
            return

        if(self.stack[-1] < self.minValue):
            self.minValue = ((2*self.minValue) - self.stack[-1])
        self.stack.pop()
        
        if not self.stack:
            self.minValue = None

       


    def top(self) -> int:

        if not self.stack:
            return None

        if(self.stack[-1] < self.minValue):
            return self.minValue
        
        return self.stack[-1]

    def getMin(self) -> int:
      
        return self.minValue



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()