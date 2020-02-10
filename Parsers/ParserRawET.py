import pandas as pd
import math
from Parsers.ParserCoordinate import ParserCoordinate
from Parsers.ParserEyeMovement import ParserEyeMovement

class ParserRawET:
    """
    Select data in segment
    Calculate gaze point based on left and right eye
    """

    def __init__(self, pathData, segments, durationThreshold, angleThreshold):
        self.pathData = pathData
        self.segments = segments
        self.durationThreshold = durationThreshold
        self.angleThreshold = angleThreshold

    def createFixations(self):
        df = pd.read_csv(self.pathData, sep=';')
        for segment in self.segments:
            start = segment.getStart()
            end = segment.getEnd()
            segmentData = selectSegmentData(df, start, end)
            parserCoordinate = ParserCoordinate(segmentData)
            gazeData = parserCoordinate.calculateGazePoints()
            parserEyeMovements = ParserEyeMovement(gazeData, self.durationThreshold, self.angleThreshold)
            eyeMovements = parserEyeMovements.createEyeMovements()
            segment.setEyemovements(eyeMovements)



def selectSegmentData(df, start, end):
    """
        Select all the data between start and end
        :param file:
        :param start:
        :param end:
        :return:
    """
    df1 = df.loc[:, ['right_gaze_point_on_display_area', 'left_gaze_point_on_display_area', 'system_time_stamp',
                    'right_gaze_origin_in_user_coordinate_system', 'right_gaze_point_in_user_coordinate_system',
                    'left_gaze_origin_in_user_coordinate_system', 'left_gaze_point_in_user_coordinate_system'
                    ]]
    # drop last lines as they can be invalid
    df1.drop(df1.tail(2).index, inplace=True)
    # convert timestamp to miliseconds
    df1['system_time_stamp'] = df1['system_time_stamp'].astype(float) / 1000
    f3 = df1.loc[(df1['system_time_stamp'] >= start) & (df1['system_time_stamp'] <= end)]
    return f3









