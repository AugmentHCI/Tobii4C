from Parsers.ParserAOI import ParserAOI
from Parsers.ParserSegment import ParserSegment
from Parsers.ParserRawET import ParserRawET
from Analyser.AnalyserFixations import AnalyserFixations
from Analyser.AnalyserSaccades import AnalyserSaccades
from Experiment.Participant import Participant

if __name__ == '__main__':
    all = './SampleData/123456.csv'
    seg = './SampleData/P123456_Segments.seg'
    aoi = './SampleData/Experiment2019.aoi'


    parserAOI = ParserAOI(aoi)
    aois = parserAOI.createAOIs()

    parserSegment = ParserSegment(seg)
    segments = parserSegment.createSegment()

    participant = Participant(123456,segments)


    parserRawET = ParserRawET(all, segments)
    parserRawET.createEyeMovements()


    for segment in segments:
        analyserFix = AnalyserFixations(segment, aois, participant)
        metricsList = analyserFix.getSummary()
        fixationList = analyserFix.getFixationList()
        analyserSac = AnalyserSaccades(segment, aois, participant)
        analyserSac.parseSaccades()
        print(segment.getMetrics())

