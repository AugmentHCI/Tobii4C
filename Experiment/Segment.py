from Experiment.Fixation import Fixation
from Experiment.Saccade import Saccade

class Segment:

    def __init__(self, scene, start, end):
        self.scene = scene
        self.start = int(start)
        self.end = int(end)
        self.eyemovements = []
        self.fixations = []
        self.saccades = []
        self.metricsList = []
        self.aoilist = []
        self.aoidurationlist = []
        self.features = []
        self.analyser = None

    def getScene(self):
        return self.scene

    def getStart(self):
        return self.start

    def getEnd(self):
        return self.end

    def getDuration(self):
        return self.end - self.start

    def getEyeMovements(self):
        return self.eyemovements

    def getAnalyser(self):
        return self.analyser

    def setEyemovements(self, eyemovements):
        self.eyemovements = eyemovements
        self.fixations = self.setFixations(eyemovements)
        self.saccades = self.setSaccades(eyemovements)

    def setFixations(self, eyemovements):
        return [fix for fix in eyemovements if isinstance(fix, Fixation)]

    def setSaccades(self, eyemovements):
        return [sac for sac in eyemovements if isinstance(sac, Saccade)]

    def getFixations(self):
        return self.fixations

    def getSaccades(self):
        return self.saccades

    def appendMetrics(self, metrics):
        self.metricsList.append(metrics)

    def setAOIList(self, list):
        self.aoilist = list

    def setAOIDurationList(self, list):
        self.aoidurationlist = list

    def getAOIDurationList(self):
        return self.aoidurationlist

    def getAOIList(self):
        return self.aoilist

    def getMetrics(self):
        return self.metricsList

    def appendFeatures(self, feature):
        self.features.append(feature)

    def setAnalyser(self, analyser):
        self.analyser = analyser


