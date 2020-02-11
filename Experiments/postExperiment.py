import pickle
import pandas as pd

def readExperimentFromFile(filename):
    readObject = open(filename, 'rb')
    objRestored = pickle.load(readObject)
    return objRestored

def analyseSaccades(experiment):
    aois = self.getAOIs()
    id = participant.getId()
    rawPath = self.rawPath + str(id) + '.csv'
    segments = participant.getSegments()

    parserRawET = ParserRawET(rawPath, segments, self.durationThreshold, self.angleThreshold)
    parserRawET.createFixations()
    for segment in segments:
        print(segment.getScene().getName())
        analyserFix = AnalyserFixations(segment, aois, participant)
        metricsList = analyserFix.getSummary()
        fixationList = analyserFix.getFixationList()
        analyserSac = AnalyserSaccades(segment, aois, participant)
        analyserSac.parseSaccades()



if __name__ == '__main__':
    outputPath = './Objects/'
    experimentPath = outputPath + 'experiment0912_300.obj'
    experiment = readExperimentFromFile(experimentPath)
