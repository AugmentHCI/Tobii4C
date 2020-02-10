import pickle

class Participant:

    def __init__(self, id, segments):
        self.id = id
        self.segments = segments
        self.metrics = []

    def __repr__(self):
        return self.id

    def getId(self):
        return self.id

    def getSegments(self):
        return self.segments

    def appendMetrics(self, metrics):
        self.metrics.append(metrics)

    def saveParticipantToFile(self, filename):
        fileHandler = open(filename, 'wb+')
        pickle.dump(self, fileHandler)
        fileHandler.close()

