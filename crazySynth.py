
import synthepyzer_utils
from synthepyzer_utils import *

class crazySynthPiece:
    def __init__(self,soundGenerator,centsOffset,phase,volume):
        self.soundGenerator = soundGenerator
        self.centsOffset = centsOffset
        self.phase = phase
        self.volume = volume
        self.instrumentID = -1
    def generator(self, frequency,t,offset):
        return self.soundGenerator(getNewNoteByCents(frequency, self.centsOffset*1000),t,offset + self.phase)*self.volume


class crazySynth:
    def __init__(self):
        self.pieces = []
        self.volume = 1
    def addPiece(self,soundGenerator,centsOffset,phase,volume):
        self.pieces.append(crazySynthPiece(soundGenerator,centsOffset,phase,volume))
    def generator(self,frequency,t,offset):
        volumeSum = 0
        output = 0
        if len(self.pieces) != 0:
            for piece in self.pieces:
                output += piece.generator(frequency,t,offset)
                volumeSum += piece.volume
            output = output/volumeSum*self.volume
        return output
    