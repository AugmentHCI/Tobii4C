import pickle
import pandas as pd
outputPath = './Objects/'


def readParticipantFromFile(filename):
    readObject = open(filename, 'rb')
    objRestored = pickle.load(readObject)
    participants = objRestored.getParticipants()
    for participant in participants:
        print(participant.getId())

def readExperimentFromFile(filename):
    dfPC = pd.read_csv('./RawData/PersonalCharacteristics.csv')

    readObject = open(filename, 'rb')
    objRestored = pickle.load(readObject)
    participants = objRestored.getParticipants()
    dataExperiment = []
    for participant in participants:
        pid = participant.getId()
        segments = participant.getSegments()
        dataParticipant = []
        for segment in segments:
            scene = segment.getScene().getName()
            AOIList = segment.getAOIList()
            aoiDurationList = segment.getAOIDurationList()
            dataSegment = writeAOIList(AOIList,aoiDurationList, pid, scene, dfPC)
            dataParticipant.extend(dataSegment)
        dataExperiment.extend(dataParticipant)
    return dataExperiment


def writeAOIList(AOIList, aoiDurationList, id, scene, dfPC):
    rowPC = dfPC[dfPC['Id'] == id]
    length = len(AOIList)
    if length == 0:
        print(id, scene)
        width = 0
    else:
        width = 1 / length
    totalDuration = sum(aoiDurationList)
    data = []
    xDuration = 0
    for i in range(length):
        aoi = AOIList[i]
        durationFix = aoiDurationList[i]
        widthDuration = durationFix / totalDuration
        aoiName = aoi.getName()
        x = i * width
        row = {
            'Person': id,
            'Scene': scene,
            'AOI': aoiName,
            'x': x,
            'xDuration': xDuration,
            'width': width,
            'widthDuration': widthDuration,
            'index': i,
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
        xDuration += widthDuration
        data.append(row)
    return data




if __name__ == '__main__':
    experimentPath = outputPath + 'experiment0912_300.obj'
    data = readExperimentFromFile(experimentPath)
    dfParsed = pd.DataFrame(data)
    dfParsed.to_csv('data/aoi.csv' )
