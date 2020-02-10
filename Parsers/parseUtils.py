import pandas as pd

import pandas
import math
import numpy as np
import os




def getUserTimeData(file, id):
    """
    Read the start and end time of a user for a specific interface
    :param file:
    :param id:
    :return:
    """
    f1 = pandas.read_csv(file)
    userData = f1.loc[f1['Id'] == id]
    if id == 100805001:
        start = int(userData.loc[:,"Start"])*1000 - 7200000000
        end = int(userData.loc[:,"End"])*1000 - 7200000000
    else:
        start = int(userData.loc[:, "Start"]) * 1000
        end = int(userData.loc[:, "End"]) * 1000
    return [start, end]


def selectETData(file, start, end):
    """
    Select all the data between start and end
    :param file:
    :param start:
    :param end:
    :return:
    """
    f1 = pandas.read_csv(file, delimiter=";")
    f2 = f1.loc[:, ['right_gaze_point_on_display_area', 'left_gaze_point_on_display_area', 'system_time_stamp',
                    'right_gaze_origin_in_user_coordinate_system', 'right_gaze_point_in_user_coordinate_system',
                    'left_gaze_origin_in_user_coordinate_system', 'left_gaze_point_in_user_coordinate_system'
                    ]]
    # drop last lines as they can be invalid
    f2.drop(f2.tail(2).index, inplace=True)
    f2['system_time_stamp'] = f2['system_time_stamp'].astype(float)
    f3 = f2.loc[(f2['system_time_stamp'] >= start) & (f2['system_time_stamp'] <= end)]
    return f3

def checkValid(value):
    if value < 0:
        return False
    elif value > 100:
        return False
    elif pandas.isnull(value):
        return False
    else:
        return True

def checkValid3D(value):
    if pandas.isnull(value):
        return False
    else:
        return True


def getOrigin(row, index):
    right = row['right_gaze_origin_in_user_coordinate_system']
    left = row['left_gaze_origin_in_user_coordinate_system']
    return averageGazePoint3D(row, index, left, right)

def averageGazePoint2D(row, index):
    """
    Calculate the gaze point based on left and right eye
    If one of the eyes is NaN, the result is -1
    If one of the eyes is negative, the result is -1
    If one of the eyes is bigger than 100, the result is -1
    :param row:
    :param index: wether to return the x (0) or the y (1) coordinate
    :return:
    """
    right = row['right_gaze_point_on_display_area']
    left = row['left_gaze_point_on_display_area']
    [x1, y1] = parse2DCoordinate(right)
    [x2, y2] = parse2DCoordinate(left)

    if checkValid(x1) and checkValid(x2):
        x3 = (x1 + x2)/2
    elif checkValid(x1):
        x3 = x1
    elif checkValid(x2):
        x3 = x2
    else:
        x3 = -1

    if checkValid(y1) and checkValid(y2):
        y3 = (y1 + y2)/2
    elif checkValid(y1):
        y3 = y1
    elif checkValid(y2):
        y3 = y2
    else:
        y3 = -1

    if index == 0:
        return x3 * 100
    else:
        return y3 * 100


def getGazePoint3D(row, index):
    right = row['right_gaze_point_in_user_coordinate_system']
    left = row['left_gaze_point_in_user_coordinate_system']
    return averageGazePoint3D(row, index, left, right)



def averageGazePoint3D(row, index, left, right):
    [x1, y1, z1] = parse3DCoordinate(right)
    [x2, y2, z2] = parse3DCoordinate(left)

    if checkValid3D(x1) and checkValid3D(x2):
        x3 = (x1 + x2)/2
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


def parse3DCoordinate(coordinate):
    """
        Parse both values of the coordinate and return
        :param coordinate:
        :return:
        """
    list = coordinate[1:-1].split(',')
    x = parseCoordinateValue(list[0])
    y = parseCoordinateValue(list[1])
    z = parseCoordinateValue(list[2])

    return [x, y, z]


def parse2DCoordinate(coordinate):
    """
    Parse both values of the coordinate and return
    :param coordinate:
    :return:
    """
    list = coordinate[1:-1].split(',')
    x = parseCoordinateValue(list[0])
    y = parseCoordinateValue(list[1])
    return [x, y]


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


def calculateGazePoints(df):
    df['x'] = df.apply(lambda row: averageGazePoint2D(row, 0), axis=1)
    df['y'] = df.apply(lambda row: averageGazePoint2D(row, 1), axis=1)
    df['x3'] = df.apply(lambda row: getGazePoint3D(row, 0), axis=1)
    df['y3'] = df.apply(lambda row: getGazePoint3D(row, 1), axis=1)
    df['z3'] = df.apply(lambda row: getGazePoint3D(row, 2), axis=1)
    return df

def calculateFixationTime(df):
    """
    Calculate the fixation time in miliseconds
    :param df:
    :return:
    """
    # tobii return in microseconds
    df['fixationTime'] = ((df['system_time_stamp'].shift(periods=-1) - df['system_time_stamp'])/1000).fillna(0)
    return df

def getVector(row):
    [xR, yR, zR] = parse3DCoordinate(row['right_gaze_origin_in_user_coordinate_system'])
    [x2R, y2R, z2R] = parse3DCoordinate(row['right_gaze_point_in_user_coordinate_system'])
    [xL, yL, zL] = parse3DCoordinate(row['left_gaze_origin_in_user_coordinate_system'])
    [x2L, y2L, z2L] = parse3DCoordinate(row['left_gaze_point_in_user_coordinate_system'])
    if xR == -1 and x2R == -1:
        return [xL - x2L, yL - y2L, zL - z2L]
    else:
        return [xR - x2R, yR - y2R, zR - z2R]

def getDistance(row):
    [xR, yR, zR] = parse3DCoordinate(row['right_gaze_origin_in_user_coordinate_system'])
    [x2R, y2R, z2R] = parse3DCoordinate(row['right_gaze_point_in_user_coordinate_system'])
    [xL, yL, zL] = parse3DCoordinate(row['left_gaze_origin_in_user_coordinate_system'])
    [x2L, y2L, z2L] = parse3DCoordinate(row['left_gaze_point_in_user_coordinate_system'])
    if xR == -1 and x2R == -1:
        dX = (xL - x2L) ** 2
        dY = (yL - y2L) ** 2
        dZ = (zL - z2L) ** 2

    else:
        dX = (xR - x2R) ** 2
        dY = (yR - y2R) ** 2
        dZ = (zR - z2R) ** 2

    totDelta = dX + dY + dZ
    return math.sqrt(totDelta)

def calculateVectors(df):
    df['vector'] = df.apply(lambda row: getVector(row), axis=1)
    df['vectorNext'] = df['vector'].shift(periods=-1)
    df['vectorNext'].iloc[-1] = df['vectorNext'].iloc[-2]
    return df

def calculateDistance(df):
    '''
    Calculates distance in mm
    :param df:
    :return:
    '''
    df['distance'] = df.apply(lambda row: getDistance(row), axis=1)
    return df

def selectValidPoints(df):
    return df.loc[(df['x'] > 0) & (df['y'] > 0)]


def cleanData(file, userId):
    """
    Calculate the gaze point based on the left and the right eye
    Calculate the fixation time
    Out of bounds and NaN coordinates are parsed to -1
    :param file:
    :param userId:
    :return:
    """
    print(os.getcwd())
    filename = '../data/' + str(userId) + '.csv'
    [start, end] = getUserTimeData(file, userId)
    ETData = selectETData(filename, start, end)
    gazePoint = calculateGazePoints(ETData)
    fixation = calculateFixationTime(gazePoint)
    vectors = calculateVectors(fixation)
    distance = calculateDistance(vectors)
    # valid = selectValidPoints(vectors)
    # return valid
    return distance



# only for test purposes
# inputBase = "baseline.csv"
# clean = cleanData(inputBase, 20809006)
# print(clean['x3'])