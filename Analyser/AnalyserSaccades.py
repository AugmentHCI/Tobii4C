from Experiment.Transition import Transition
from Experiment.Saccade import Saccade
from Experiment.Fixation import Fixation
from Experiment.Vector import Vector

class AnalyserSaccades:

    def __init__(self, segment, aois, participant):
        self.segment = segment
        self.aois = aois
        self.participant = participant

    def getSegment(self):
        return self.segment

    def getAois(self):
        return self.aois

    def parseSaccades(self):
        self.parseAOISaccades()
        self.calculateRelAngles()
        self.parseLengthSaccades()

    def parseLengthSaccades(self):
        segment = self.getSegment()
        saccades = segment.getSaccades()
        cumulativeLength = 0
        for saccade in saccades:
            cumulativeLength += saccade.getLength()
        segment.appendFeatures(cumulativeLength)

    def parseAOISaccades(self):
        """
        If you have overlapping AOI, look to the priority
        :return:
        """
        segment = self.getSegment()
        aois = self.getAois()
        saccades = segment.getSaccades()
        for saccade in saccades:
            startPoint = saccade.getStartLocation()
            endPoint = saccade.getEndLocation()
            startPoint.setAOI(aois)
            endPoint.setAOI(aois)
            vector = Vector(startPoint, endPoint)
            angle = vector.getAbsAngle()
            saccade.setAbsAngle(angle)

    def calculateRelAngles(self):
        segment = self.getSegment()
        saccades = segment.getSaccades()
        cumulativeAngle = 0
        for i in range(len(saccades) -2):
            currentSac = saccades[i]
            nextSac = saccades[i+1]
            currentVec = currentSac.getVector()
            nextVec = nextSac.getVector()
            relAngle = currentVec.getAngleBetween(nextVec)
            currentSac.setRelAngleWithNext(relAngle)
            cumulativeAngle += relAngle
        segment.appendFeatures(cumulativeAngle)


