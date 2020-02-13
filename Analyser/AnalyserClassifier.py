import math


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
        self.setSaccadeRate()
        self.setAvgSaccadeAmplitude()
        self.setAvgSaccadeVelocity()
        self.setPeakSaccadeVelocity()
        self.setFixationRate()
        self.setAvgFixationDuration()
        self.setRatioSaccadeFixation()
        self.setAvgPupilSize()

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


def safeAdd(a, b):
    if not math.isnan(b):
        a = a+b
    return a

