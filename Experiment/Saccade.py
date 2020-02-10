from Experiment.EyeMovement import EyeMovement as parent


class Saccade(parent):

    def __init__(self, startLocation, endLocation, startTime, endTime):
        '''
        :param startLocation: Coordinate
        :param endLocation: Coordinate
        :param startTime:
        :param endTime:
        '''
        parent.__init__(self, startTime, endTime)
        self.startLocation = startLocation
        self.endLocation = endLocation
        self.startAOI = None
        self.endAOI = None
        self.absAngle = None
        self.relAngle = None
        self.vector = None

    def getStartLocation(self):
        return self.startLocation

    def getEndLocation(self):
        return self.endLocation

    def getStartAOI(self):
        return self.startAOI

    def getEndAOI(self):
        return self.endAOI

    def setStartAOI(self, aoi):
        self.startAOI = aoi

    def setEndAOI(self, aoi):
        self.endAOI = aoi

    def setAbsAngle(self, angle):
        """
        :param angle: in degrees
        :return:
        """
        self.absAngle = angle

    def setRelAngleWithNext(self, angle):
        self.relAngle = angle

    def setVector(self, vector):
        self.vector = vector

    def getVector(self):
        return self.vector

    def getLenght(self):
        return self.getVector().getMagnitude()
