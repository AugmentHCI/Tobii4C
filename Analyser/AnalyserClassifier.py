import math
import numpy as np


class AnalyserSegmentClassifier:

    def __init__(self, segment, participant):
        self.segment = segment
        self.participant = participant
        self.saccadeRate = None
        self.avgSaccadeAmplitude = None
        self.avgSaccadeVelocity = None
        self.peakSaccadeVelocity = None
        self.fixationRate = None
        self.avgFixationDuration = None
        self.ratioSaccadeFixation = None
        self.avgPupilSize = None
        self.avgSaccadeLength = None
        self.mostFrequentDirection = None
        self.heatMap = None
        self.setSaccadeRate()
        self.setAvgSaccadeAmplitude()
        self.setAvgSaccadeVelocity()
        self.setPeakSaccadeVelocity()
        self.setFixationRate()
        self.setAvgFixationDuration()
        self.setRatioSaccadeFixation()
        self.setAvgPupilSize()
        self.setAvgSaccadeLength()
        self.setMostFrequentDirection()
        self.setHeatmap()

    def getSegment(self):
        return self.segment

    def getSaccadeRate(self):
        return self.saccadeRate

    def getAvgSaccadeAmplitude(self):
        return self.avgSaccadeAmplitude

    def getAvgSaccadeVelocity(self):
        return self.avgSaccadeVelocity

    def getPeakSaccadeVelocity(self):
        return self.peakSaccadeVelocity

    def getFixationRate(self):
        return self.fixationRate

    def getAvgFixationDuration(self):
        return self.avgFixationDuration

    def getRatioSaccadeFixation(self):
        return self.ratioSaccadeFixation

    def getAvgPupilSize(self):
        return self.avgPupilSize

    def getAvgSaccadeLength(self):
        return self.avgSaccadeLength

    def getMostFrequentDirection(self):
        return self.mostFrequentDirection

    def getHeatMap(self):
        return self.heatMap

    def setSaccadeRate(self):
        segment = self.getSegment()
        saccades = segment.getSaccades()
        nbSaccades = len(saccades)
        duration = segment.getDuration()
        self.saccadeRate = nbSaccades / duration

    def setAvgSaccadeAmplitude(self):
        segment = self.getSegment()
        saccades = segment.getSaccades()
        sum = 0
        for saccade in saccades:
            sum = safeAdd(sum, saccade.getAmplitude())
        if len(saccades) > 0:
            avg = sum / len(saccades)
            self.avgSaccadeAmplitude = avg
        else:
            print("No Saccades")
            self.avgSaccadeAmplitude = -1

    def setAvgSaccadeVelocity(self):
        segment = self.getSegment()
        saccades = segment.getSaccades()
        sum = 0
        for saccade in saccades:
            sum = safeAdd(sum, saccade.getVelocity())
        if len(saccades) > 0:
            avg = sum / len(saccades)
            self.avgSaccadeVelocity = avg
        else:
            print("No Saccades")
            self.avgSaccadeVelocity = -1

    def setPeakSaccadeVelocity(self):
        segment = self.getSegment()
        saccades = segment.getSaccades()
        peak = 0
        for saccade in saccades:
            current = saccade.getPeakVelocity()
            if current > peak:
                peak = current
        self.peakSaccadeVelocity = peak

    def setFixationRate(self):
        segment = self.getSegment()
        fixations = segment.getFixations()
        nbFixations = len(fixations)
        duration = segment.getDuration()
        rate = nbFixations / duration
        self.fixationRate = rate

    def setAvgFixationDuration(self):
        segment = self.getSegment()
        fixations = segment.getFixations()
        sum = 0
        for fixation in fixations:
            sum = safeAdd(sum,fixation.getDuration())

        if len(fixations) > 0:
            avg = sum / len(fixations)
            self.avgFixationDuration = avg
        else:
            print("No Fixations")
            self.avgFixationDuration = -1



    def setRatioSaccadeFixation(self):
        segment = self.getSegment()
        fixations = segment.getFixations()
        saccades = segment.getSaccades()
        durationSaccades = 0
        for saccade in saccades:
            durationSaccades = safeAdd(durationSaccades, saccade.getDuration())

        durationFixations = 0
        for fix in fixations:
            durationFixations = safeAdd(durationFixations, fix.getDuration())

        if durationFixations > 0:
            ratio = durationSaccades / durationFixations
            self.ratioSaccadeFixation = ratio
        else:
            print("No Fixations")
            self.ratioSaccadeFixation = -1


    def setAvgPupilSize(self):
        segment = self.getSegment()
        eyeMovements = segment.getEyeMovements()
        sum = 0
        for eyeMove in eyeMovements:
            sum = safeAdd(sum, eyeMove.getPupilSize())
        if len(eyeMovements) > 0:
            avg = sum / len(eyeMovements)
            self.avgPupilSize = avg
        else:
            print("No eye movements")
            self.avgPupilSize = -1

    def setAvgSaccadeLength(self):
        segment = self.getSegment()
        saccades = segment.getSaccades()
        nbSaccades = len(saccades)
        sum = 0
        for saccade in saccades:
            sum += saccade.getLength()
        if nbSaccades != 0:
            avg = sum / nbSaccades
            self.avgSaccadeLength = avg
        else:
            self.avgSaccadeLength = 0

    def setMostFrequentDirection(self):
        segment = self.getSegment()
        saccades = segment.getSaccades()
        directions = [0, 0, 0, 0, 0, 0, 0, 0]
        for saccade in saccades:
            direction = saccade.getDirection()
            curr = directions[direction]
            directions[direction] = curr + 1
        maxIndex = directions.index(max(directions))
        self.mostFrequentDirection = maxIndex

    def setHeatmap(self):
        gridSize = 4
        matrix = [[0 for x in range(gridSize + 1)] for y in range(gridSize + 1)]
        segment = self.getSegment()
        fixations = segment.getFixations()
        xValues = []
        yValues = []
        for fix in fixations:
            fixPoint = fix.getFixPoint()
            x = fixPoint.getX()
            y = fixPoint.getY()
            xValues.append(x)
            yValues.append(y)
        binnedX = getBins(gridSize, xValues)
        binnedY = getBins(gridSize, yValues)
        for x in range(0, len(binnedX)):
            for y in range(0, len(binnedY)):
                row = binnedX[x]
                column = binnedY[y]
                curr = matrix[row][column]
                matrix[row][column] = curr + 1
        self.heatMap = matrix

def getBins(nbBins, data):
    bins = np.linspace(0, 100, nbBins)
    binned = np.digitize(data, bins)
    return binned


def safeAdd(a, b):
    if not math.isnan(b):
        a = a+b
    return a

