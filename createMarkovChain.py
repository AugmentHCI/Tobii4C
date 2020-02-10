import pickle
import pandas as pd

def readExperimentFromFile(filename):
    readObject = open(filename, 'rb')
    objRestored = pickle.load(readObject)
    return objRestored



def getMarkovChainExperiment(experiment):
    dfPC = pd.read_csv('./RawData/PersonalCharacteristics.csv')
    participants = experiment.getParticipants()
    dataExperiment = []
    for participant in participants:
        pid = participant.getId()
        rowPC = dfPC[dfPC['Id'] == pid]
        dataParticipant = getMarkovChainParticipant(participant, rowPC)
        dataExperiment.extend(dataParticipant)
    return dataExperiment

def getMarkovChainParticipant(participant, rowPC):
    sources = ['art', 'sli', 'rec', 'exp']
    pid = participant.getId()
    segments = participant.getSegments()
    dataParticipant = []
    for segment in segments:
        scene = segment.getScene().getName()
        markovList = getMarkovChainSegment(segment)
        for i in range(0, len(markovList)):
            source = sources[i]
            list = markovList[i]
            dataSegment = writeMarkovChain(pid, scene, source, list, rowPC)
            dataParticipant.extend(dataSegment)
    return dataParticipant


def getMarkovChainSegment(segment):
    scene = segment.getScene().getName()
    saccades = segment.getSaccades()

    aoiList = []
    for saccade in saccades:
        startLocation = saccade.getStartLocation().getAOI()
        if startLocation != None:
            begin = startLocation.getName()[0:3]
            aoiList.append(begin)

    aoisString = ['art', 'sli', 'rec', 'exp']
    art = [0, 0, 0, 0]
    sli = [0, 0, 0, 0]
    rec = [0, 0, 0, 0]
    exp = [0, 0, 0, 0]
    aois = [art, sli, rec, exp]

    for i in range(0, len(aoiList)-1):
        aoiStart = aoiList[i]
        aoiEnd = aoiList[i+1]
        index1 = aoisString.index(aoiStart)
        index2 = aoisString.index(aoiEnd)
        if scene == 'P':
            if index1 == 3:
                index1 = 2
            if index2 == 3:
                index2 = 2
        aois[index1][index2] += 1
    aoisNormalised = []

    for list in aois:
        normalised = normaliseList(list)
        aoisNormalised.append(normalised)
    return aoisNormalised

def writeMarkovChain(pid, scene, source, list,  rowPC):
    targets = ['art', 'sli', 'rec', 'exp']
    data = []
    for i in range(0, len(list)):
        target = targets[i]
        value = list[i]

        row = {
            'Person': pid,
            'Scene': scene,
            'Source': source,
            'Target': target,
            'Value': value,
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
        data.append(row)
    return data

def normaliseList(list):
    sumList = sum(list)
    result = list
    if sumList != 0:
        result = [x/sumList for x in list]
    return result

if __name__ == '__main__':
    outputPath = './Objects/'
    experimentPath = outputPath + 'experiment1301_100.obj'
    experiment = readExperimentFromFile(experimentPath)
    # experiment.analyseAllParticipantsSaccades()
    # experiment.saveExperimentToFile(outputPath + 'experiment1212_300.obj')
    data = getMarkovChainExperiment(experiment)
    dfParsed = pd.DataFrame(data)
    filter = dfParsed[(dfParsed['Scene'] == 'PX') & (dfParsed['Source'] == 'exp') ]
    print(filter['Value'])
    dfParsed.to_csv('data/markov.csv')

