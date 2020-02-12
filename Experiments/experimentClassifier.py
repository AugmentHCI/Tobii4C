from Parsers.ParserExperiment import ParserExperiment

userList = [100805001, 101057002, 101553005, 101714006, 120904002,
            291203003, 10705005, 20809006, 20939007, 21204008,
            21308009, 51205010, 51602011, 51732012, 60752001,
            60904002, 61500003, 61615004, 71108005, 71540007,
            81010008, 81556009, 90748011, 91316012, 121255014,
            131210015, 190800016, 191204017, 200759018, 201238019]



# userList = [90748011, 91316012, 121255014]
offset = 15000
# path to all data and to segments
aoiPath = 'Experiment2019.aoi'
rawPath = './Rawdata/'
segmentPath = './Segments/' + str(offset) + '/'
outputPath = './Objects/Classifier'
durationThreshold = 100
angleThreshold = 0.5


if __name__ == '__main__':
    experimentParser = ParserExperiment(aoiPath, segmentPath, rawPath, outputPath, userList, durationThreshold, angleThreshold)
    experiment = experimentParser.parseExperiment()
    experiment.analyseAllParticipantsClassifier()

    experimentPath = outputPath + 'experimentClassifier_' +str(offset) + str(durationThreshold) + '.obj'
    experiment.saveExperimentToFile(experimentPath)