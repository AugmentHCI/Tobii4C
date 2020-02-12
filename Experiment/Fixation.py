from Experiment.EyeMovement import EyeMovement as parent


class Fixation(parent):
    def __init__(self, FixPoint, startTime, endTime, durationThreshold, angleThreshold, pupilSize):
        parent.__init__(self, startTime, endTime, pupilSize)
        self.fixpoint = FixPoint
        self.durationThreshold = durationThreshold
        self.angleThreshold = angleThreshold
        self.fixAOI = None

    def getFixPoint(self):
        return self.fixpoint

    def setFixAOI(self, aoi):
        self.fixAOI = aoi

    def getFixAOI(self):
        return self.fixAOI
