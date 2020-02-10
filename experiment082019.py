from Parsers.ParserAOI import ParserAOI
from Parsers.ParserSegment import ParserSegment
from Parsers.ParserRawET import ParserRawET
from AnalyserFixations import AnalyserFixations
from AnalyserSaccades import AnalyserSaccades
from Experiment.Participant import Participant
from Experiment.Experiment import Experiment
from Parsers.ParserExperiment import ParserExperiment
import pickle

userList = [100805001, 101057002, 101553005, 101714006, 120904002,
            291203003, 10705005, 20809006, 20939007, 21204008,
            21308009, 51205010, 51602011, 51732012, 60752001,
            60904002, 61500003, 61615004, 71108005, 71540007,
            81010008, 81556009, 90748011, 91316012, 121255014,
            131210015, 190800016, 191204017, 200759018, 201238019]



# userList = [201238019]

# path to all data and to segments
aoiPath = 'Experiment2019.aoi'
rawPath = './Rawdata/'
segmentPath = './Segments/'
outputPath = './Objects/'
durationThreshold = 100
angleThreshold = 0.5


def readExperimentFromFile(filename):
    readObject = open(filename, 'rb')
    objRestored = pickle.load(readObject)
    print(objRestored)
    participants = objRestored.getParticipants()
    for participant in participants:
        print(participant.getId())

if __name__ == '__main__':
    experimentParser = ParserExperiment(aoiPath, segmentPath, rawPath, outputPath, userList, durationThreshold, angleThreshold)
    experiment = experimentParser.parseExperiment()
    experiment.analyseAllParticipants()

    experimentPath = outputPath + 'experiment1301_' + str(durationThreshold) + '.obj'
    experiment.saveExperimentToFile(experimentPath)


