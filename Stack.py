from queue import LifoQueue
class Stack(LifoQueue):
    def __init__(self, startLocation):
        """
        startLocation - initial RAM location as int
        """
        super(Stack,self).__init__()
        self.startLocation = startLocation
        self.pointer = startLocation
    def getPointer(self):
        return super()._qsize() + self.startLocation
    def put(self, value):
        super(Stack,self).put(value)
        

stack = Stack(256)
print(stack.getPointer())
stack.put(1)
stack.put(2)
print(stack.getPointer())
print(stack.get())
print(stack.getPointer())