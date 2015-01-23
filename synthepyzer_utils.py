

import numpy
import random
import math
import globs
from globs import *

class Generators:

    def __init__(self):
        self.sinLookupTable = generateLookupTableForWave(slowSinGenerator)
        self.squareLookupTable = generateLookupTableForWave(slowSquareGenerator)
        self.sawtoothLookupTable = generateLookupTableForWave(slowSawtoothGenerator)
        self.triangleLookupTable = generateLookupTableForWave(slowTriangleGenerator)

    def sinGenerator(self,frequency,t,offset):
        return getSampleFromWaveLookupTable(frequency,t,offset,self.sinLookupTable)

    def squareGenerator(self,frequency,t,offset):
        return getSampleFromWaveLookupTable(frequency,t,offset,self.squareLookupTable)

    def sawtoothGenerator(self,frequency,t,offset):
        return getSampleFromWaveLookupTable(frequency,t,offset,self.sawtoothLookupTable)

    def triangleGenerator(self,frequency,t,offset):
        return getSampleFromWaveLookupTable(frequency,t,offset,self.triangleLookupTable)

def generateLookupTableForWave(waveGenerator):
    lookupTable = []
    n_samples = sample_rate
    for s in range(n_samples):
        t = float(s)/sample_rate
        lookupTable.append(waveGenerator(1,t,0))
    # print len(lookupTable)
    return lookupTable

def getSampleFromWaveLookupTable(frequency,t,offset,table):
    index = int(t*frequency*sample_rate)
    index = index%len(table)
    return table[index]

def getNewNoteBySemitones(frequency,semitones):
    return frequency * (2 ** (float(semitones)/12))

def getNewNoteByCents(frequency,cents):
    return frequency * (2 ** (cents/1200))

def whiteNoiseGenerator(frequency,t,offset):
    return 2*random.random() - 1

def slowSinGenerator(frequency, t, offset):
    return math.sin(2*math.pi*frequency*t + offset)
    
def slowSquareGenerator(frequency, t, offset):
    if(math.sin(2*math.pi*frequency*t + offset) > 0):
        return 1
    else:
        return -1

def slowSawtoothGenerator(frequency,t,offset):
    # return 2*(t*frequency - math.floor(t*frequency)) - 1
    return 2 * (t * frequency)%1 - 1

def slowTriangleGenerator(frequency,t,offset):
    return 2*abs(slowSawtoothGenerator(frequency/2,t,offset)) - 1

def randomFrequency(scale):
    randomNote = 0
    modifier = random.randint(0,3)+1
    
    if(random.randint(0,2) == 0):
        if(randomNote + modifier > 7):
            randomNote = randomNote - modifier
        else:
            randomNote = randomNote + modifier
    else:
        if(randomNote - modifier <= 1):
            randomNote = randomNote + modifier
        else:
            randomNote = randomNote - modifier
            
    return scale[randomNote]

def bufferNextFrequency(frequency, duration, function, fadeinThreshold, fadeOutThreshold,volume):
    if(volume != 0):
        n_samples = int(round(duration*sample_rate))

        buf = numpy.zeros((n_samples), dtype = numpy.int16)
        max_sample = (2**(bits - 1) - 1)*volume

        offset = 0
        
        clampThreshold = 50

        for s in range(n_samples):
            t = float(s)/sample_rate

            buf[s] = int(round(max_sample*function(frequency,t,offset)))
            if s < fadeinThreshold:
                buf[s] = buf[s] * s / fadeinThreshold
            if n_samples - s < fadeOutThreshold:
                buf[s] = buf[s] * (float(n_samples - s) / fadeOutThreshold)
            if n_samples - s < clampThreshold:
                buf[s] = buf[s]*(float(n_samples - s)/clampThreshold)**2
        return buf