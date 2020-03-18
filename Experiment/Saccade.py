from Experiment.EyeMovement import EyeMovement as parent
from Experiment.Vector import Vector
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

        self.startAOI = None
        self.endAOI = None
        self.vector = None
        self.absAngle = None
        self.relAngle = None
        self.velocity = None
        self.direction = None
        self.setVelocity()
        self.setVector()
        self.setDirection()
        self.setAbsAngle()
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

    def getVelocity(self):
        return self.velocity

    def getVector(self):
        return self.vector

    def getLength(self):
        return self.getVector().getMagnitude()

    def getDirection(self):
        return self.direction


    def setStartAOI(self, aoi):
        self.startAOI = aoi

    def setEndAOI(self, aoi):
        self.endAOI = aoi


    def setAbsAngle(self):
        """
        :param angle: in degrees
        :return:
        """
        angle = self.getVector().getAbsAngle()
        self.absAngle = angle

    def setRelAngleWithNext(self, angle):
        self.relAngle = angle

    def setVector(self):
        '''
        Vector between start and end point
        :param vector:
        :return:
        '''
        start = self.getStartLocation()
        end = self.getEndLocation()
        vector = Vector(start, end)
        self.vector = vector


    def setVelocity(self):
        self.velocity = self.getAmplitude() / self.getDuration()


    def setDirection(self):
        self.direction = self.getVector().getDirection()
