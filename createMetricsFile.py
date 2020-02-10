import pickle
import pandas as pd
import collections, functools, operator

outputPath = './Objects/'



def readExperimentFromFile(filename):
    dfPC = pd.read_csv('./RawData/PersonalCharacteristics.csv')
    readObject = open(filename, 'rb')
    objRestored = pickle.load(readObject)
    participants = objRestored.getParticipants()
    dataExperiment = []
    for participant in participants:
        pid = participant.getId()
        rowPC = dfPC[dfPC['Id'] == pid]
        segments = participant.getSegments()
        dataParticipant = []
        for segment in segments:
            scene = segment.getScene().getName()
            metricsList = segment.getMetrics()
            dataSegment = summarySegment(pid, scene, metricsList, rowPC)
            dataParticipant.extend(dataSegment)
        dataExperiment.extend(dataParticipant)
    return dataExperiment

def chechAOI(aoi, target):
    begin = aoi[0:3]
    if begin == target:
        return True
    else:
        return False


def summarySegment(id, scene, metrics, rowPC):
    aois = ['rec', 'exp', 'art', 'sli']
    data = []
    for aoi in aois:
        ttf = 100000000
        nbFix = 0
        relNbFix = 0
        duration = 0
        durationRel = 0
        for metric in metrics:
            aoiName = metric.getAoi().getName()
            if chechAOI(aoiName, aoi):
                ttfCurrent = metric.getTimeToFirstFixation()
                nbFix += metric.getNbFixations()
                relNbFix += metric.getNbFixationRel()
                duration += metric.getDuration()
                durationRel += metric.getRelDuration()
                if ttfCurrent < ttf and ttfCurrent != 0:
                    ttf = ttfCurrent
        if ttf == 100000000:
            ttf = 0
        row = {
            'Person': id,
            'Scene': scene,
            'AOI': aoi,
            'ttf': ttf,
            'nbFix': nbFix,
            'nbFixRel': relNbFix,
            'duration': duration,
            'durationRel': durationRel,
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
    recTotal = createRowRecTotal(data[0], data[1])
    data.append(recTotal)
    return data

def createRowRecTotal(rec, exp):
    row = {
        'Person': rec['Person'],
        'Scene': rec['Scene'],
        'AOI': 'reT',
        'ttf': min(rec['ttf'], exp['ttf']),
        'nbFix': rec['nbFix'] + exp['nbFix'],
        'nbFixRel': rec['nbFixRel'] + exp['nbFixRel'],
        'duration': rec['duration'] + exp['duration'],
        'durationRel': rec['durationRel'] + exp['durationRel'],
        'VWM': rec['VWM'],
        'MS': rec['MS'],
        'LOC': rec['LOC'],
        'NFC': rec['NFC'],
        'Vigilance': rec['Vigilance'],
        'Buckpassing': rec['MS'],
        'Procrastination': rec['Procrastination'],
        'Hypervigilance': rec['Hypervigilance'],
        'Extraversion': rec['Extraversion'],
        'Agreeableness': rec['Agreeableness'],
        'Consientiousness': rec['Consientiousness'],
        'Neuroticism': rec['Neuroticism'],
        'Openess': rec['Openess']
    }
    return row


def writeMetrics(id, scene, metrics, dfPC):
    data = []
    rowPC = dfPC[dfPC['Id'] == id]
    dataRec = []
    for metric in metrics:
        aoiName = metric.getAoi().getName()
        ttf = metric.getTimeToFirstFixation()
        nbFix = metric.getNbFixations()
        relNbFix = metric.getNbFixationRel()
        duration = metric.getDuration()
        durationRel = metric.getRelDuration()
        row = {
            'Person': id,
            'Scene': scene,
            'AOI': 'reT',
            'ttf': ttf,
            'nbFix': nbFix,
            'nbFixRel': relNbFix,
            'duration': duration,
            'durationRel': durationRel,
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




if __name__ == '__main__':
    experimentPath = outputPath + 'experiment1301_100.obj'
    data = readExperimentFromFile(experimentPath)
    dfParsed = pd.DataFrame(data)
    print(dfParsed['ttf'])
    dfParsed.to_csv('data/metrics.csv' )
