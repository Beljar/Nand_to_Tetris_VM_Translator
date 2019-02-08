class MemorySegment:
    def __init__(self, locationPointer):
        self.locationPointer = locationPointer
        self.data = {}
    def read(self,address):
        pass
    def write(self,address, value):
        pass