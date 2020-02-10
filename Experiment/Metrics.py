
class Metrics:
    '''
    Metrics for one aoi
    '''

    def __init__(self, participant=None, segment=None, aoi=None, ttf = None, nbFix = None, nbRelFix = None,
                 duration = None, relDuration = None):
        self.participant = participant
        self.segment = segment
        self.aoi = aoi
        self.timeToFirstFixation = ttf
        self.nbFixations = nbFix
        self.relNbFixations = nbRelFix
        self.duration = duration
        self.relDuration = relDuration

    def __repr__(self):
        return str(self.aoi.getName()) + " " + \
               str(self.timeToFirstFixation) + " " + \
                str(self.nbFixations)+ " " +\
                str(self.relNbFixations) + " " +\
                str(self.duration) + " " +\
                str(self.relDuration)

    def getAoi(self):
        return self.aoi

    def getTimeToFirstFixation(self):
        return self.timeToFirstFixation

    def getNbFixations(self):
        return self.nbFixations

    def getNbFixationRel(self):
        return self.relNbFixations

    def getDuration(self):
        return self.duration

    def getRelDuration(self):
        return self.relDuration

    def setParticipant(self, participant):
        self.participant = participant

    def setSegment(self, segment):
        self.segment = segment

    def setAOI(self, aoi):
        self.aoi = aoi

    def setTimeToFirstFixation(self, ttf):
        self.timeToFirstFixation = ttf

    def setNbFixations(self, int):
        self.nbFixations = int

    def setRelNbFixations(self, float):
        self.relNbFixations = float

    def setDuration(self, int):
        self.duration = int

    def setRelDuration(self, float):
        self.relDuration = float
