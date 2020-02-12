


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
            sum += saccade.getAmplitude()
        if len(saccades) > 0:
            avg = sum / len(saccades)
            self.avgSaccadeAmplitude = avg



    def setAvgSaccadeVelocity(self):
        segment = self.getSegment()
        saccades = segment.getSaccades()
        sum = 0
        for saccade in saccades:
            sum += saccade.getVelocity()
        if len(saccades) > 0:
            avg = sum / len(saccades)
            self.avgSaccadeVelocity = avg

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
        return nbFixations / duration

    def setAvgFixationDuration(self):
        segment = self.getSegment()
        fixations = segment.getFixations()
        sum = 0
        for fixation in fixations:
            sum += fixation.getDuration()

        if len(fixations) > 0:
            avg = sum / len(fixations)
            self.avgFixationDuration = avg



    def setRatioSaccadeFixation(self):
        segment = self.getSegment()
        fixations = segment.getFixations()
        saccades = segment.getSaccades()
        if len(fixations) > 0:
            ratio = len(saccades) / len(fixations)
            self.ratioSaccadeFixation = ratio


    def setAvgPupilSize(self):
        segment = self.getSegment()
        eyeMovements = segment.getEyeMovements()
        sum = 0
        for eyeMove in eyeMovements:
            sum += eyeMove.getPupilSize()
        if len(eyeMovements) > 0:
            avg = sum / len(eyeMovements)
            self.avgPupilSize = avg




