import pandas as pd
import numpy as np
import math

class ParserCoordinate:
    """
    Parse String coordinates on display area to x,y
    Average Left and Right eye to X,Y
    Must be between 0 and 100, else -1
    Parse String user centered coordinates to x,y,z
    Average Left and Right eye to X,Y,Z
    NaN => -1
    Null => -1
    Parse vector
    """
    def __init__(self, data):
        self.data = data

    def calculateGazePoints(self):
        """
        Add new columns with
        x,y gaze point on display
        x,y,z gaze point in user centered
        x,y,z origin point in user centered
        :return:
        """
        df = self.data
        getGazePoint(df.iloc[0], 0, 2)
        df['x'] = df.apply(lambda row: getGazePoint(row, 0, 2), axis=1)
        df['y'] = df.apply(lambda row: getGazePoint(row, 1, 2), axis=1)
        df['x3'] = df.apply(lambda row: getGazePoint(row, 0, 3), axis=1)
        df['y3'] = df.apply(lambda row: getGazePoint(row, 1, 3), axis=1)
        df['z3'] = df.apply(lambda row: getGazePoint(row, 2, 3), axis=1)
        df['xO'] = df.apply(lambda row: getOrigin(row, 0), axis=1)
        df['yO'] = df.apply(lambda row: getOrigin(row, 1), axis=1)
        df['zO'] = df.apply(lambda row: getOrigin(row, 2), axis=1)
        return df





def averageGazePoint2D(index, left, right):
    """
    Calculate the gaze point based on left and right eye
    If one of the eyes is NaN, the result is -1
    If one of the eyes is negative, the result is -1
    If one of the eyes is bigger than 100, the result is -1
    :param row:
    :param index: wether to return the x (0) or the y (1) coordinate
    :return:
    """

    [x1, y1] = parseCoordinate(right)
    [x2, y2] = parseCoordinate(left)

    if checkValid2D(x1) and checkValid2D(x2):
        x3 = (x1 + x2) / 2
    elif checkValid2D(x1):
        x3 = x1
    elif checkValid2D(x2):
        x3 = x2
    else:
        x3 = -1

    if checkValid2D(y1) and checkValid2D(y2):
        y3 = (y1 + y2) / 2
    elif checkValid2D(y1):
        y3 = y1
    elif checkValid2D(y2):
        y3 = y2
    else:
        y3 = -1

    if index == 0:
        return x3 * 100
    else:
        return y3 * 100


def averageGazePoint3D(index, left, right):
    [x1, y1, z1] = parseCoordinate(right)
    [x2, y2, z2] = parseCoordinate(left)

    if checkValid3D(x1) and checkValid3D(x2):
        x3 = (x1 + x2) / 2
        y3 = (y1 + y2) / 2
        z3 = (z1 + z2) / 2

    elif checkValid3D(x1):
        x3 = x1
        y3 = y1
        z3 = z1
    elif checkValid3D(x2):
        x3 = x2
        y3 = y2
        z3 = z2
    else:
        x3 = -1
        y3 = -1
        z3 = -1

    if index == 0:
        return x3
    elif index == 1:
        return y3
    else:
        return z3


def checkValid2D(value):
    """
    Check if value is between 0 and 100
    :param value:
    :return:
    """
    if value < 0:
        return False
    elif value > 100:
        return False
    elif pd.isnull(value):
        return False
    else:
        return True


def checkValid3D(value):
    """
    Check if value != null
    :param value:
    :return:
    """
    if pd.isnull(value):
        return False
    else:
        return True


def parseCoordinateValue(value):
    """
    Parse value to float
    If value is NaN, return -1
    :param value:
    :return:
    """
    i = float(value)
    if math.isnan(i):
        return -1
    else:
        return i


def parseCoordinate(coordinate):
    stripped = coordinate[1:-1]
    list = stripped.split(',')
    result = []
    for c in list:
        cparsed = parseCoordinateValue(c)
        result.append(cparsed)
    return result


def getGazePoint(row, index, dimension):
    if dimension == 2:
        right = row['right_gaze_point_on_display_area']
        left = row['left_gaze_point_on_display_area']
        result =  averageGazePoint2D(index, left, right)
    elif dimension == 3:
        right = row['right_gaze_point_in_user_coordinate_system']
        left = row['left_gaze_point_in_user_coordinate_system']
        result =  averageGazePoint3D(index, left, right)
    return result


def getOrigin(row, index):
    right = row['right_gaze_origin_in_user_coordinate_system']
    left = row['left_gaze_origin_in_user_coordinate_system']
    return averageGazePoint3D(index, left, right)


