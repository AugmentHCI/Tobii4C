import math


class Aoi:

    def __init__(self, name, p1, p2, p3, p4, priority):
        self.name = name
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4
        self.priority = priority
        self.scenes = []
        self.metrics = []

    def __repr__(self):
        return self.name

    def setScenes(self, scenes):
        for scene in scenes:
            self.scenes[scene.getName()] = []

    def appendMetrics(self, metrics):
        self.metrics.append(metrics)


    def setAnalyseSegment(self, segment, analyse):
        scene = segment.getScene()
        self.scenes[scene.getName()] = analyse

    def getLimits(self):
        x1 = self.p1.getX()
        x2 = self.p2.getX()
        x3 = self.p3.getX()
        x4 = self.p4.getX()
        minX = min(x1, x2, x3, x4)
        maxX = max(x1, x2, x3, x4)
        y1 = self.p1.getY()
        y2 = self.p2.getY()
        y3 = self.p3.getY()
        y4 = self.p4.getY()
        minY = min(y1, y2, y3, y4)
        maxY = max(y1, y2, y3, y4)
        return [minX, maxX, minY, maxY]

    def checkWithinAOI(self, point):
        x = point.getX()
        y = point.getY()
        [minX, maxX, minY, maxY] = self.getLimits()
        if checkBetweenLimits(minX, maxX, x) and checkBetweenLimits(minY, maxY, y):
            return True

    def getPriority(self):
        return self.priority

    def getName(self):
        return self.name

    def getMetrics(self):
        return self.metrics

    def getScenes(self):
        return self.scenes

def checkBetweenLimits(lower, upper, value):
    return value >= lower and value <= upper