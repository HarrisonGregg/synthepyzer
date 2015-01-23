
import globs
from globs import *

waveformPoints = []
waveformLength = 500
    
def addPointToWaveform(amplitude):
    global waveformPoints
    waveformPoints.append(int(amplitude/float(2**(bits - 1) - 1)*400 / 2 + 200))
    if len(waveformPoints) > waveformLength:
        waveformPoints.pop(0)

def drawWaveform(screen):
    for x in range(len(waveformPoints)):
        screen.set_at((x, waveformPoints[x]), [255,255,255])
    pygame.display.flip()
    screen.fill([0,0,0])