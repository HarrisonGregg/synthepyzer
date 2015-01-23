
import globs
from globs import *
import pygame
import synthepyzer_utils
from synthepyzer_utils import *

class Mixer:
    def __init__(self):
        self.instruments = []
        self.instrumentData = []
        self.currentlyActiveChannels = []
        self.instrumentSoundBuffer = []
    def addInstrument(self,instrument,volume):
        instrument.instrumentID = len(self.instruments)
        self.instruments.append(instrument)
        self.instrumentData.append([volume])
        self.instrumentSoundBuffer.append(0)
    def update(self,event):
        if event.type == SEQUENCER_NOTE_EVENT:
            if len(event.notes) > 0 and self.instrumentSoundBuffer[event.instrument] != 0:
                self.instrumentSoundBuffer[event.instrument].play()
            if len(event.next_notes) > 0:
                note = event.next_notes[0]
                sound = bufferNextFrequency(note.frequency,note.duration,self.instruments[event.instrument].generator,100,500,note.velocity)
                self.instrumentSoundBuffer[event.instrument] = pygame.sndarray.make_sound(sound)


