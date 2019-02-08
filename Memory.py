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
        put it to register
        """
        return self.point(address) + f"R{register}=M;\n"
    def getFromR(self, address, register):
        return self.point(address) + f"M=R{register};\n"
    def point(self, address):
        """
        generates assembler instruction 
        to set memory pointer to current address
        """
        if address==0:
            assemblerInstruction = f"@{self.pointerLocation};\n"
        else:
            assemblerInstruction = (f"@{self.pointerLocation};\n"
                                    "D=A;\n"
                                    f"@{address};\n"
                                    "D=D+A;\n"
                                    "A=D;\n")
        return assemblerInstruction

class StaticMemorySegment(MemorySegment):
    def __init__(self, pointerLocation=None, addressDomain = None):
        super(StaticMemorySegment,self).__init__()

class ConstantMemorySegment(MemorySegment):
    def __init__(self, pointerLocation=None, addressDomain = None):
        super(ConstantMemorySegment,self).__init__()
    def putToR(self,address,register):
        assemblerInstruction = (f"@{address};\n"
                                "D=A;\n"
                                f"@R{register};\n"
                                "M=D;\n")
        return assemblerInstruction
    def getFromR(self,address,register):
        raise Exception("Can't write to CONSTANT")

class Stack(MemorySegment):
    def __init__(self, pointerLocation=None, addressDomain = None):
        super(Stack,self).__init__(pointerLocation, addressDomain)
    def increasePointer(self):
        return self.point(0) + "M=M+1;\n"
    def decreasePointer(self):
        return self.point(0) + "M=M-1;\n"
    def putToR(self, register):
        return super(Stack,self).putToR(0,register)
    def getFromR(self, register):
        return super(Stack,self).getFromR(0,register)
        