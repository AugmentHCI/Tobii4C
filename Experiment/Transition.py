
class Transition:
    """
    Similar to a Saccade, but with a
    """

    def __init__(self, startAOI, endAOI, length, absAngle, relAngle):
        self.startAOI = startAOI
        self.endAOI = endAOI
        self.length = length
        self.absAngle = absAngle
        self.relAngle = relAngle
        self.velocity = self.getVelocity()

