from Parsers.ParserSegment import ParserSegment
from Parsers.ParserRawET import ParserRawET
from Parsers.ParserAOI import ParserAOI
from Experiment.Participant import Participant
from Experiment.Experiment import Experiment

class ParserExperiment:

    def __init__(self, aoiPath, segPath, rawPath, outPath, idList, durationThreshold, angleThreshold):
        self.aoiPath = aoiPath
        self.segPath = segPath
        self.rawPath = rawPath
        self.outPath = outPath
        self.idList = idList
        self.durationThreshold = durationThreshold
        self.angleThreshold = angleThreshold

    def parseExperiment(self):
        participants = self.parseParticipants()
        aois = self.parseAOIs()
        return Experiment(participants, aois, self.rawPath, self.outPath, self.durationThreshold, self.angleThreshold)

    def parseParticipants(self):
        participants = []
        for id in self.idList:
            segmentPath = self.segPath + 'P' + str(id) + '_Segments.seg'
            parserSegment = ParserSegment(segmentPath)
            segments = parserSegment.createSegment()
            participant = Participant(id, segments)
            participants.append(participant)
        return participants

    def parseAOIs(self):
        aoi = self.aoiPath
        parserAOI = ParserAOI(aoi)
        aois = parserAOI.createAOIs()
        return aois
