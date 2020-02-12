
class EyeMovement:

    def __init__(self, start, end, pupilSize):
        self.start = start
        self.end = end
        self.pupilSize = pupilSize
        self.duration = None
        self.setDuration()



    def setDuration(self):
        self.duration = self.end - self.start


    def getStart(self):
        return self.start

    def getEnd(self):
        return self.end

    def getDuration(self):
        return self.duration

    def getPupilSize(self):
        return self.pupilSize

