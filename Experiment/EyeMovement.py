
class EyeMovement:

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def getDuration(self):
        return self.end - self.start


    def getStart(self):
        return self.start

    def getEnd(self):
        return self.end