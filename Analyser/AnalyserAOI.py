
class AnalyserAOI:

    def __init__(self, aoi, segments):
        self.aois = aoi
        self.segments = self.setSegments(segments)

    def setSegments(self, segments):
        for segment in segments:
            self.segments[segment.name] = []

    def setAnalyseSegment(self, segment, analyse):
        self.segments[segment.name] = analyse
