import math
import numpy as np

class Vector:

    def __init__(self, p1, p2):
        """

        :param p1: Coordinate
        :param p2: Coordinate
        """
        self.startPoint = p1
        self.endPoint = p2
        self.vector = self.calculateVector()
        self.direction = None
        self.setDirection()

    def calculateVector(self):
        x1 = self.startPoint.getX()
        x2 = self.endPoint.getX()
        y1 = self.startPoint.getY()
        y2 = self.endPoint.getY()
        vector = [x2 - x1, y2 - y1]
        return vector

    def getVector(self):
        return self.vector

    def getMagnitude(self):
        return np.linalg.norm(self.getVector())

    def getDeltaX(self):
        return self.vector[0]

    def getDeltaY(self):
        return self.vector[1]

    def getAbsAngle(self):
        '''
        Angle in degrees
        :return:
        '''
        dx = self.getDeltaX()
        dy = self.getDeltaY()
        if dx != 0:
            radAngle = math.atan(dy / dx)
            degAngle = math.degrees(radAngle)
        else:
            degAngle = 90
        return degAngle

    def getAngleBetween(self, v1):
        radAngle = angle_between(self.getVector(), v1.getVector())
        degAngle = math.degrees(radAngle)
        return degAngle

    def getDirection(self):
        return self.direction

    def setDirection(self):
        angle = self.getAbsAngle()
        direction = 0
        if angle < 45:
            direction = 0
        elif angle < 90:
            direction = 1
        elif angle < 135:
            direction = 2
        elif angle < 180:
            direction = 3
        elif angle < 225:
            direction = 4
        elif angle < 270:
            direction = 5
        elif angle < 315:
            direction = 6
        elif angle < 360:
            direction = 7
        else:
            direction = 8

        self.direction = direction



def unit_vector(vector):
    """ Returns the unit vector of the vector.  """
    if np.linalg.norm(vector) == 0:
        return vector
    else:
        return vector / np.linalg.norm(vector)

def angle_between(v1, v2):
    """ Returns the angle in radians between vectors 'v1' and 'v2'::
    """
    v1_u = unit_vector(v1)
    v2_u = unit_vector(v2)
    angle =  np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0))
    return angle



