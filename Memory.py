class MemorySegment:
    def __init__(self, pointerLocation=None, addressDomain = None):
        """
        pointerLocation as string or int
        addressDomain as range()
        """
        self.pointerLocation = pointerLocation
        self.data = {}
        self.range = addressDomain
    def putToR(self,address,register):
        """
        generates assembler instruction 
        to read value in address and
        put it to R-register
        """

        assemblerInstruction = self.point(address)
        assemblerInstruction += ("D=M\n"
                                f"@R{register}\n"
                                "M=D\n")
        return assemblerInstruction
    def putToD(self,address):
        """
        generates assembler instruction 
        to read value in address and
        put it to D-register
        """
        return self.point(address) + "D=M\n"
    def getFromR(self, address, register):
        assemblerInstruction = (f"@R{register}\n"
                                "D=M\n")
        assemblerInstruction += self.point(address)
        assemblerInstruction += "M=D\n"
        return assemblerInstruction
    def point(self, address=0):
        """
        generates assembler instruction 
        to set memory pointer to current address
        """
        if address==0:
            assemblerInstruction = (f"@{self.pointerLocation}\n"
                                    "A=M\n")
        else:
            assemblerInstruction = (f"@{self.pointerLocation}\n"
                                    "D=A\n"
                                    f"@{address}\n"
                                    "D=D+A\n"
                                    "A=D\n")
        return assemblerInstruction

class StaticMemorySegment(MemorySegment):
    def __init__(self, pointerLocation=None, addressDomain = None):
        super(StaticMemorySegment,self).__init__()

class ConstantMemorySegment(MemorySegment):
    def __init__(self, pointerLocation=None, addressDomain = None):
        super(ConstantMemorySegment,self).__init__()
    def putToR(self,address,register):
        assemblerInstruction = (f"@{address}\n"
                                "D=A\n"
                                f"@R{register}\n"
                                "M=D\n")
        return assemblerInstruction
    def getFromR(self,address,register):
        raise Exception("Can't write to CONSTANT")

class Stack(MemorySegment):
    def __init__(self, pointerLocation=None, addressDomain = None):
        super(Stack,self).__init__(pointerLocation, addressDomain)
    def increasePointer(self):
        return (f"@{self.pointerLocation}\n"
                "M=M+1\n")
    def decreasePointer(self):
        return (f"@{self.pointerLocation}\n"
                "M=M-1\n")
    def putToR(self, register):
        return super(Stack,self).putToR(0,register)
    def putToD(self):
        return super(Stack,self).putToD(0)
    def getFromR(self, register):
        return super(Stack,self).getFromR(0,register)
        