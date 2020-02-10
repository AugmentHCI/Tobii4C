
class Coordinate:

    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)
        self.aoi = None

    def __repr__(self):
        print(self.x , self.y, self.aoi)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getAOI(self):
        return self.aoi

    def setAOI(self, aois):
        """
            Return aois in which point lies
            if there are overlapping aois, return aoi with highest priority
            :param Fixation:
            :param aois:
            :return:
            """
        withinList = []
        for aoi in aois:
            within = aoi.checkWithinAOI(self)
            if within:
                withinList.append(aoi)

        priority = -1
        aoiPriority = None
        for aoi in withinList:
            if aoi.getPriority() > priority:
                priority = aoi.getPriority()
                aoiPriority = aoi
        self.aoi = aoiPriority
        return aoiPriority

