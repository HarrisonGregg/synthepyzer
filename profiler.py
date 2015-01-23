
import pygame
from pygame.locals import *

import random

import math
import numpy
import time

import sys

import cProfile
import globs
from globs import *
import crazySynth
from crazySynth import *
import waveform_visualizer
import keyboard
from keyboard import *
import slider
from slider import *
import sequencer
import mixer
import button
from button import *
import clickable_grid
from clickable_grid import *
import synthepyzer_utils
from synthepyzer_utils import *

pygame.mixer.quit()
pygame.mixer.pre_init(sample_rate, -bits, 1)
pygame.init()

# size = (600, 400)
size = (1024, 600)
screen = pygame.display.set_mode(size, pygame.HWSURFACE | pygame.DOUBLEBUF)
fpsClock = pygame.time.Clock()

def main():

    megaSynth = crazySynth()
    megaSynth.addPiece(whiteNoiseGenerator,0,0,.05)
    megaSynth.addPiece(generators.sinGenerator,0,0,1)
    megaSynth.addPiece(generators.triangleGenerator,0,0,0)
    megaSynth.addPiece(generators.sawtoothGenerator,0,0,1)
    megaSynth.addPiece(generators.squareGenerator,0,0,0)

    megaSynth1 = crazySynth()
    megaSynth1.addPiece(whiteNoiseGenerator,0,0,0)
    megaSynth1.addPiece(generators.sinGenerator,0,0,1)
    megaSynth1.addPiece(generators.triangleGenerator,0,0,1)
    megaSynth1.addPiece(generators.sawtoothGenerator,0,0,0)
    megaSynth1.addPiece(generators.squareGenerator,0,0,0)

    megaSynth2 = crazySynth()
    megaSynth2.addPiece(whiteNoiseGenerator,0,0,0)
    megaSynth2.addPiece(generators.sinGenerator,0,0,.5)
    megaSynth2.addPiece(generators.triangleGenerator,.5,0,.5)
    megaSynth2.addPiece(generators.sawtoothGenerator,0,0,1)
    megaSynth2.addPiece(generators.squareGenerator,0,0,.3)
    
    globMixer = mixer.Mixer()
    globSequencer = sequencer.Sequencer(80,4)
    globMixer.addInstrument(megaSynth,1)
    globMixer.addInstrument(megaSynth1,1)
    globMixer.addInstrument(megaSynth2,1)
    globSequencer.addTrack(globMixer.instruments[0].instrumentID, 32)
    globSequencer.addTrack(globMixer.instruments[1].instrumentID, 32)
    globSequencer.addTrack(globMixer.instruments[2].instrumentID, 32)

    for i in range(40):
        note = getNewNoteBySemitones(16.35, 8)*(2**3)
        sound = bufferNextFrequency(note,.1,globMixer.instruments[0].generator,100,500,.5)
        soundSound = pygame.sndarray.make_sound(sound)
        soundSound.play()

cProfile.run('generators = Generators()')

cProfile.run('main()')

pygame.quit()
