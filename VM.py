from Memory import *

"""
Memory segments
"""
LOCAL = 0
ARGUMENT = 1
THIS = 2
THAT = 3
CONSTANT = 4
STATIC = 5
POINTER = 6
TEMP = 7

MEMORY = {
    STATIC  :   MemorySegment(),
    LOCAL   :   MemorySegment(pointerLocation="LCL"),
    CONSTANT:   ConstantMemorySegment()
}

TEMPREG = 13



class VM:
    def __init__(self, memory, stackSize):
        self.memory = memory
        self.stack = Stack(pointerLocation="SP")
    def push(self, segmentName, addr):
        segment = self.memory[segmentName]
        assInst = segment.putToR(addr, TEMPREG)
        assInst += self.stack.getFromR(TEMPREG)
        assInst += self.stack.increasePointer()
        return assInst
    def pop(self, segmentName, addr):
        segment = self.memory[segmentName]
        assInst = self.stack.decreasePointer()
        assInst += self.stack.putToR(TEMPREG)
        assInst += segment.getFromR(addr, TEMPREG)
        return assInst

test = ""
t = VM(MEMORY, 1000)
test += t.push(CONSTANT,17)
test += t.pop(LOCAL,2)
test += t.push(LOCAL,2)
test += t.push(LOCAL,2)
test += t.pop(STATIC,10)
test += t.pop(LOCAL,3)
print(test)