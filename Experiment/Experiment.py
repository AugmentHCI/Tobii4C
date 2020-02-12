from Parsers.ParserRawET import ParserRawET
from Analyser.AnalyserSaccades import AnalyserSaccades
from Analyser.AnalyserFixations import AnalyserFixations
from Analyser.AnalyserClassifier import AnalyserSegmentClassifier

import pandas as pd
import pickle

class Experiment:

    def __init__(self, participants, aois, rawPath, outputPath, durationThreshold, angleThreshold):
        self.participants = participants
        self.aois = aois
        self.rawPath = rawPath
        self.outputPath = outputPath
        self.durationThreshold = durationThreshold
        self.angleThreshold = angleThreshold

    def getParticipants(self):
        return self.participants

    def getNbParticipants(self):
        return len(self.participants)

    def getAOIs(self):
        return self.aois

    def analyseAllParticipantsSaccades(self):
        participants = self.getParticipants()
        for participant in participants:
            id = participant.getId()
            print(id)
            aois = self.getAOIs()
            self.analyseParticipantSaccades(participant, aois)

    def analyseParticipantSaccades(self, participant, aois):
        segments = participant.getSegments()
        for segment in segments:
            analyserSac = AnalyserSaccades(segment, aois, participant)
            analyserSac.parseSaccades()

    def analyseAllParticipants(self):
        participants = self.getParticipants()
        for participant in participants:
            id = participant.getId()
            print(id)
            self.analyseParticipant(participant)
            participant.saveParticipantToFile(self.outputPath + str(id) + '.obj')

    def analyseParticipant(self, participant):
        aois = self.getAOIs()
        id = participant.getId()
        rawPath = self.rawPath + str(id) + '.csv'
        segments = participant.getSegments()

        parserRawET = ParserRawET(rawPath, segments, self.durationThreshold, self.angleThreshold)
        parserRawET.createEyeMovements()
        for segment in segments:
            print(segment.getScene().getName())
            analyserFix = AnalyserFixations(segment, aois, participant)
            metricsList = analyserFix.getSummary()
            fixationList = analyserFix.getFixationList()
            analyserSac = AnalyserSaccades(segment, aois, participant)
            analyserSac.parseSaccades()

    def analyseAllParticipantsClassifier(self):
        participants = self.getParticipants()
        for participant in participants:
            id = participant.getId()
            print(id)
            self.analyseParticipantClassifier(participant)

    def analyseParticipantClassifier(self, participant):
        aois = self.getAOIs()
        id = participant.getId()
        rawPath = self.rawPath + str(id) + '.csv'
        segments = participant.getSegments()
        parserRawET = ParserRawET(rawPath, segments, self.durationThreshold, self.angleThreshold)
        # create fixations
        parserRawET.createEyeMovements()
        for segment in segments:
            analyser = AnalyserSegmentClassifier(segment, participant)
            segment.setAnalyser(analyser)







    def saveExperimentToFile(self, filename):
        fileHandler = open(filename, 'wb+')
        pickle.dump(self, fileHandler)
        fileHandler.close()

    def writeAllAnalysisToCSV(self):
        participants = self.getParticipants()
        headers = [
            'userId', 'sceneName', 'AOIName', 'timeToFirstFixation', 'nbFix', 'nbFixRel',
            'duration', 'durationRel'
        ]
        data = []
        for participant in participants:
            print(participant.getId())
            self.analyseParticipant(participant)
            segments = participant.getSegments()
            dataParticipant = []
            for segment in segments:
                rows = self.writeAnalysis(participant, segment)
                dataParticipant.extend(rows)
            dfParticipant = pd.DataFrame(data=dataParticipant, columns=headers)
            dfParticipant.to_csv(self.outputPath + str(participant.getId()) + '_analyse.csv')
            data.extend(dataParticipant)
        df = pd.DataFrame(data=data, columns=headers)
        df.to_csv(self.outputPath + 'analyse.csv')

    def writeAnalysis(self, participant, segment):
        userId = participant.getId()
        sceneName = segment.getScene().getName()
        metrics = segment.getMetrics()
        rowList = []
        for metric in metrics:
            row = {
                'userId': userId,
                'sceneName': sceneName,
                'AOIName': metric.getAoi().getName(),
                'timeToFirstFixation': metric.getTimeToFirstFixation(),
                'nbFix': metric.getNbFixations(),
                'nbFixRel': metric.getNbFixationRel(),
                'duration': metric.getDuration(),
                'durationRel': metric.getRelDuration(),
            }
            rowList.append(row)
        return rowList



