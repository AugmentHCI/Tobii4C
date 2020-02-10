import pickle
from Experiment.Coordinate import Coordinate

co = Coordinate(1,1)
filename = './Objects/100805001.obj'

# fileHandler = open(filename, 'wb+')
# pickle.dump(co, fileHandler)
# fileHandler.close()

readParticipant = open(filename, 'rb')
participant = pickle.load(readParticipant)
segments = participant.getSegments()

for segment in segments:
    print(segment.getAOIList())