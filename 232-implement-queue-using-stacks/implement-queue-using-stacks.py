class MyQueue:

    def __init__(self):
        self.a=[]
        self.b=[]

    def push(self,x:int)->None:
        self.a.append(x)

    def pop(self)->int:
        self.top()
        return self.b.pop()

    def peek(self)->int:
        self.top()
        return self.b[-1]

    def top(self):
        if not self.b:
            while self.a:
                self.b.append(self.a.pop())

    def empty(self)->bool:
        return not self.a and not self.b