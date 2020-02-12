from Experiment.EyeMovement import EyeMovement as parent
import math


class Saccade(parent):

    def __init__(self, startLocation, endLocation, startTime, endTime, amplitude, peakVelocity, pupilSize):
        '''
        :param startLocation: Coordinate
        :param endLocation: Coordinate
        :param startTime:
        :param endTime:
        '''
        parent.__init__(self, startTime, endTime, pupilSize)
        self.startLocation = startLocation
        self.endLocation = endLocation
        self.amplitude = amplitude
        self.peakVelocity = peakVelocity
        self.distance = None
        self.startAOI = None
        self.endAOI = None
        self.absAngle = None
        self.relAngle = None
        self.vector = None
        self.setDistance()
        self.setVelocity()


    def getStartLocation(self):
        return self.startLocation

    def getEndLocation(self):
        return self.endLocation

    def getStartAOI(self):
        return self.startAOI

    def getEndAOI(self):
        return self.endAOI

    def getAmplitude(self):
        return self.amplitude

    def getPeakVelocity(self):
        return self.peakVelocity



    def setDistance(self):
        x1 = self.startLocation.getX()
        x2 = self.endLocation.getX()
        y1 = self.startLocation.getY()
        y2 = self.endLocation.getY()
        dX = abs(x2 - x1)
        dY = abs(y2 - y1)
        distance = math.sqrt(math.pow(dX, 2) + math.pow(dY, 2))
        self.distance = distance


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

    def getLength(self):
        return self.getVector().getMagnitude()

    def setVelocity(self):
        self.velocity = self.getAmplitude() / self.getDuration()
