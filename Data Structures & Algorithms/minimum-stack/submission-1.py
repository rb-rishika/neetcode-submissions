class MinStack:

    def __init__(self):
        self.firstStack=[]
        self.secondStack=[]

    def push(self, val: int) -> None:
        self.firstStack.append(val)
        minVal= min(val,self.secondStack[-1] if self.secondStack else val )
        self.secondStack.append(minVal)

    def pop(self) -> None:
        self.firstStack.pop()
        self.secondStack.pop()

    def top(self) -> int:
        return self.firstStack[-1]

    def getMin(self) -> int:
        return self.secondStack[-1]
        
