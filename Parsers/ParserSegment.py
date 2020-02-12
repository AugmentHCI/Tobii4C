import pandas as pd
from Experiment.Segment import Segment
from Experiment.Scene import Scene

class ParserSegment:

    def __init__(self, segmentPath):
        self.segmentPath = segmentPath

    def createSegment(self):
        df = pd.read_csv(self.segmentPath)
        segments = []
        for index, row in df.iterrows():
            segment = parseRow(row)
            segments.append(segment)
        return segments


def parseRow(row):
    sceneName = row['Name']
    scene = Scene(sceneName)
    start = row['Start']
    end = row['End']
    segment = Segment(scene, start, end)
    return segment
