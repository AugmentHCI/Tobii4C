import pandas as pd
from Experiment.Coordinate import Coordinate
from Experiment.Aoi import Aoi



class ParserAOI:
    def __init__(self, aoi):
        self.aoi = aoi

    def createAOIs(self):
        df = pd.read_csv(self.aoi, sep=';')
        aois = []
        for index, row in df.iterrows():
            aoi = parseRow(row)
            aois.append(aoi)
        return aois




def parseRow(row):
    x1, y1 = row['p1'].split(',')
    x2, y2 = row['p2'].split(',')
    x3, y3 = row['p3'].split(',')
    x4, y4 = row['p4'].split(',')
    p1 = Coordinate(x1, y1)
    p2 = Coordinate(x2, y2)
    p3 = Coordinate(x3, y3)
    p4 = Coordinate(x4, y4)
    priority = int(row['priority'])
    name = row['name']
    aoi = Aoi(name, p1, p2, p3, p4, priority)
    return aoi





