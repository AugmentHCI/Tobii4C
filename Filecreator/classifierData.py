import pickle
import pandas as pd

def readExperimentFromFile(filename):
    readObject = open(filename, 'rb')
    objRestored = pickle.load(readObject)
    return objRestored

def getClassifierData(experiment):
    dfPC = pd.read_csv('../RawData/PersonalCharacteristics.csv')
    participants = experiment.getParticipants()
    dataExperiment = []
    for participant in participants:
        pid = participant.getId()
        rowPC = dfPC[dfPC['Id'] == pid]
        dataParticipant = getClassifierDataParticipant(participant, rowPC)
        dataExperiment.extend(dataParticipant)
    return dataExperiment

def appendHeatMap(analyser, row):
    matrix = analyser.getHeatMap()
    rows = len(matrix)
    columns = len(matrix[0])
    for x in range(0,rows):
        for y in range(0, columns):
            key = 'heatmap_' + str(x) + str(y)
            row[key] = matrix[x][y]
    return row

def getClassifierDataParticipant(participant, rowPC):
    pid = participant.getId()
    segments = participant.getSegments()
    dataParticipant = []
    for segment in segments:
        analyser = segment.getAnalyser()
        scene = segment.getScene().getName()
        row = {
            'Person': pid,
            'Scene': scene,
            'saccadeRate': analyser.getSaccadeRate(),
            'avgSaccadeAmplitude': analyser.getAvgSaccadeAmplitude(),
            'avgSaccadeVelocity': analyser.getAvgSaccadeVelocity(),
            'peakSaccadeVelocity': analyser.getPeakSaccadeVelocity(),
            'fixationRate': analyser.getFixationRate(),
            'avgFixationDuration': analyser.getAvgFixationDuration(),
            'ratioSaccadeFixation': analyser.getRatioSaccadeFixation(),
            'avgPupilSize': analyser.getAvgPupilSize(),
            'avgSaccadeLength': analyser.getAvgSaccadeLength(),
            'mostFrequentDirection': analyser.getMostFrequentDirection(),
            'VWM': rowPC['VWM'].values[0],
            'MS': rowPC['MS'].values[0],
            'LOC': rowPC['LOC'].values[0],
            'NFC': rowPC['NFC'].values[0],
            'Vigilance': rowPC['Vigilance'].values[0],
            'Buckpassing': rowPC['MS'].values[0],
            'Procrastination': rowPC['Procrastination'].values[0],
            'Hypervigilance': rowPC['Hypervigilance'].values[0],
            'Extraversion': rowPC['Extraversion'].values[0],
            'Agreeableness': rowPC['Agreeableness'].values[0],
            'Consientiousness': rowPC['Conscientiousness'].values[0],
            'Neuroticism': rowPC['Neuroticism'].values[0],
            'Openess': rowPC['Openess'].values[0]
        }
        row = appendHeatMap(analyser, row)
        dataParticipant.append(row)
    return dataParticipant




if __name__ == '__main__':
    for x in range(10, 100, 10):
        experimentPath = '../Objects/Classifier/experimentClassifierPercentace_' + str(x) + '.obj'
        experiment = readExperimentFromFile(experimentPath)
        data = getClassifierData(experiment)
        dfParsed = pd.DataFrame(data)
        dfParsed.to_csv('../data/classifier/' + str(x) + '.csv', index=False)



