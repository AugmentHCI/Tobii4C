from Experiment.Metrics import Metrics

class AnalyserFixations:

    def __init__(self, segment, aois, participant):
        self.segment = segment
        self.aois = aois
        self.participant = participant
        self.setAOIs()

    def getSegment(self):
        return self.segment

    def getAois(self):
        return self.aois

    def getParticipant(self):
        return self.participant

    def getParticipantId(self):
        return self.participant.getId()

    def setAOIs(self):
        fixations = self.segment.getFixations()
        for fix in fixations:
            fixPoint = fix.getFixPoint()
            fixAOI = fixPoint.setAOI(self.getAois())
            fix.setFixAOI(fixAOI)

    def getSummary(self):
        segment = self.getSegment()
        aois = self.getAois()
        nbAOIs = len(aois)
        id = self.getParticipantId()
        durationTotal = segment.getDuration()
        fixationsTotal = len(segment.getFixations())
        count = self.getNbFixations()
        duration = self.getDurationFixations()
        timetofirst = self.getTimeToFirstFixation()

        # create metrics and add to participant, aoi and segment
        metricsList = []
        for i in range(nbAOIs):
            aoi = aois[i]
            if fixationsTotal == 0:
                relCount = 0
            else:
                relCount = count[i]/fixationsTotal
            metrics = Metrics(id, segment, aoi, timetofirst[i],
                              count[i], relCount ,
                              duration[i], duration[i] / durationTotal)
            aoi.appendMetrics(metrics)
            participant = self.getParticipant()
            participant.appendMetrics(metrics)
            segment.appendMetrics(metrics)
            metricsList.append(metrics)
        return metricsList



    def getNbFixations(self):
        nbAOIs = len(self.aois)
        countFixations = [0] * nbAOIs

        for fixation in self.segment.getFixations():
            fixPoint = fixation.getFixPoint()
            for i in range(nbAOIs):
                aoi = self.aois[i]
                if aoi.checkWithinAOI(fixPoint):
                    countFixations[i] += 1

        return countFixations


    def getDurationFixations(self):
        nbAOIs = len(self.aois)
        countFixations = [0] * nbAOIs

        for fixation in self.segment.getFixations():
            fixPoint = fixation.getFixPoint()
            for i in range(nbAOIs):
                aoi = self.aois[i]
                if aoi.checkWithinAOI(fixPoint):
                    countFixations[i] += fixation.getDuration()
        return countFixations

    def getTimeToFirstFixation(self):
        nbAOIs = len(self.aois)
        countFixations = [0] * nbAOIs
        segment = self.getSegment()
        for fixation in segment.getFixations():
            fixPoint = fixation.getFixPoint()
            for i in range(nbAOIs):
                aoi = self.aois[i]
                if aoi.checkWithinAOI(fixPoint):
                    duration = fixation.getStart() - segment.getStart()
                    countFixations[i] += duration
        return countFixations

    def getFixationList(self):
        segment = self.getSegment()
        fixations = segment.getFixations()
        fixationList = []
        durationList = []
        for fixation in fixations:
            aoi = fixation.getFixAOI()
            if aoi is not None:
                fixationList.append(aoi)
                durationList.append(fixation.getDuration())
        segment.setAOIList(fixationList)
        segment.setAOIDurationList(durationList)
        return fixationList


