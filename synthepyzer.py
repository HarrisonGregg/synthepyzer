
import pygame
from pygame.locals import *

import random

import math
import numpy
import time

import sys

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

    generators = Generators()

    last = time.time()
    
    static = pygame.image.load('static.png')
    sine = pygame.image.load('sine.png')
    triangle = pygame.image.load('triangle2.png')
    sawtooth = pygame.image.load('sawtooth.png')
    square = pygame.image.load('square.png')
    audio = pygame.image.load('audio.png')
    
    # key_list = [key for key in SCALES.keys()]
    # scale_key = random.choice(key_list)
    # scale = globs.SCALES[scale_key]
    # toPlay = [scale[0]] + [randomFrequency(scale) for i in range(12)] + [scale[0]]
    # toPlay2 = [scale[5]] + [randomFrequency(scale) for i in range(12)] + [scale[5]]

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

    tab = 'instruments'
    activeInstrument = 0
    onInstTab = 1

    instrumentButtons = []
    instrumentButtons.append(Button(0,10,110,90,"Inst 0",0))
    instrumentButtons.append(Button(0,120,110,90,"Inst 1",1))
    instrumentButtons.append(Button(0,230,110,90,"Inst 2",2))

    tabButtons = []
    tabButtons.append(Button(0,420,110,90,"Seq",3))
    tabButtons.append(Button(0,520,110,90,"Inst",4))

    play = Button(0, 330, 110, 30,"Play",5, 20)
    playAll = Button(0, 360, 110, 30,"Play All",6, 20)
    stop = Button(0, 390, 110, 30,"Stop",7, 20)

    rectY = instrumentButtons[activeInstrument].y
    rect2Y = 520

    k = keyboard(150, 50)
    sliders = [Slider((80+90*i - (i%2)*30, 300 + (i%2)*10), 150 - (i%2)*10) for i in range(1,10)]
    sliders.append(Slider((940,240),210))
    sliders[0].set_value(globMixer.instruments[activeInstrument].pieces[0].volume)
    sliders[1].set_value(globMixer.instruments[activeInstrument].pieces[1].volume)
    sliders[2].set_value(globMixer.instruments[activeInstrument].pieces[1].centsOffset)
    sliders[3].set_value(globMixer.instruments[activeInstrument].pieces[2].volume)
    sliders[4].set_value(globMixer.instruments[activeInstrument].pieces[2].centsOffset)
    sliders[5].set_value(globMixer.instruments[activeInstrument].pieces[3].volume)
    sliders[6].set_value(globMixer.instruments[activeInstrument].pieces[3].centsOffset)
    sliders[7].set_value(globMixer.instruments[activeInstrument].pieces[4].volume)
    sliders[8].set_value(globMixer.instruments[activeInstrument].pieces[4].centsOffset)
    sliders[9].set_value(globMixer.instruments[activeInstrument].volume)
    grid = []
    for i in range(3):
        grid.append(Grid())
    while(True):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            for ib in instrumentButtons:
                ib.update(event)
            for tb in tabButtons:
                tb.update(event)
            globMixer.update(event)
            globSequencer.update(event)
            play.update(event)
            playAll.update(event)
            stop.update(event)
            if event.type == SLIDER_MOTION:
                globMixer.instruments[activeInstrument].pieces[0].volume = sliders[0].get_value()
                globMixer.instruments[activeInstrument].pieces[1].volume = sliders[1].get_value()
                globMixer.instruments[activeInstrument].pieces[1].centsOffset = sliders[2].get_value()
                globMixer.instruments[activeInstrument].pieces[2].volume = sliders[3].get_value()
                globMixer.instruments[activeInstrument].pieces[2].centsOffset = sliders[4].get_value()
                globMixer.instruments[activeInstrument].pieces[3].volume = sliders[5].get_value()
                globMixer.instruments[activeInstrument].pieces[3].centsOffset = sliders[6].get_value()
                globMixer.instruments[activeInstrument].pieces[4].volume = sliders[7].get_value()
                globMixer.instruments[activeInstrument].pieces[4].centsOffset = sliders[8].get_value()
                globMixer.instruments[activeInstrument].volume = sliders[9].get_value()
            if event.type == BUTTON_DEPRESSED:
                if event.id < 3:
                    activeInstrument = event.id
                    sliders[0].set_value(globMixer.instruments[activeInstrument].pieces[0].volume)
                    sliders[1].set_value(globMixer.instruments[activeInstrument].pieces[1].volume)
                    sliders[2].set_value(globMixer.instruments[activeInstrument].pieces[1].centsOffset)
                    sliders[3].set_value(globMixer.instruments[activeInstrument].pieces[2].volume)
                    sliders[4].set_value(globMixer.instruments[activeInstrument].pieces[2].centsOffset)
                    sliders[5].set_value(globMixer.instruments[activeInstrument].pieces[3].volume)
                    sliders[6].set_value(globMixer.instruments[activeInstrument].pieces[3].centsOffset)
                    sliders[7].set_value(globMixer.instruments[activeInstrument].pieces[4].volume)
                    sliders[8].set_value(globMixer.instruments[activeInstrument].pieces[4].centsOffset)
                    sliders[9].set_value(globMixer.instruments[activeInstrument].volume)
                if event.id == 3:
                    tab = 'sequencer'
                if event.id == 4:
                    tab = 'instruments'
                elif event.id == 5:
                    globSequencer.stop()
                    globSequencer.clear()
                    notes = grid[activeInstrument].getPoints()
                    for x,y in notes:
                        start = time.time()
                        globSequencer.tracks[activeInstrument].addNote(y,getNewNoteBySemitones(16.35, 24 - x)*(2**3),1,.1)
                    globSequencer.play()
                if event.id == 6:
                    globSequencer.stop()
                    globSequencer.clear()
                    for i in range(3):
                        notes = grid[i].getPoints()
                        for y,x in notes:
                            globSequencer.tracks[i].addNote(x,getNewNoteBySemitones(16.35, 24 - y)*(2**3),1,.1)
                        globSequencer.play()

                if event.id == 7:
                    globSequencer.stop()

            if tab == 'sequencer':
                onInstTab = 0
                grid[activeInstrument].update(event)

            if tab == 'instruments':
                k.update(event)
                for s in sliders:
                    s.update(event)
                if event.type == KEYBOARD_EVENT:
                    note = getNewNoteBySemitones(16.35, event.selected)*(2**event.octave)
                    sound = bufferNextFrequency(note,.1,globMixer.instruments[activeInstrument].generator,100,500,.5)
                    soundSound = pygame.sndarray.make_sound(sound)
                    soundSound.play()

        if tab == 'sequencer':
            grid[activeInstrument].draw(screen)
            for i in range(24):
                rectangle = pygame.Rect(242,i*22 + 37,40,20)
                if (24 - i)%12 in [2,4,7,9,11]:
                    rectangle.x = rectangle.x - 20
                    rectangle.width = rectangle.width + 20
                    pygame.draw.rect(screen, [0,0,0],rectangle)
                else:
                    pygame.draw.rect(screen, [255,255,255], rectangle)

        if tab == 'instruments':
            onInstTab = 1
            k.draw(screen)
            for s in sliders:
                s.draw(screen)
                
            #Draw Static
            static = pygame.transform.scale(static, (50,50))
            screen.blit(static,(130,475))
            
            #Draw Sine
            sine = pygame.transform.scale(sine, (50,50))
            screen.blit(sine,(282,475))
            
            #Draw Triangle
            triangle = pygame.transform.scale(triangle, (50,50))
            screen.blit(triangle,(465, 475))
            
            #Draw Sawtooth
            sawtooth = pygame.transform.scale(sawtooth, (50,50))
            screen.blit(sawtooth,(640, 475))
            
            #Draw Square
            square = pygame.transform.scale(square, (50,50))
            screen.blit(square,(823, 475))
            
            #Draw Audio Icon
            audio = pygame.transform.scale(audio, (50,50))
            screen.blit(audio,(935, 475))

        for ib in instrumentButtons:
            ib.draw(screen)
        for tb in tabButtons:
            tb.draw(screen)
        play.draw(screen)
        playAll.draw(screen)
        stop.draw(screen)

        pygame.display.flip()
        screen.fill([100,100,100])

        rectColors = [[255,175,000],[233,111,000],[150,70,000]]

        rectY = rectY + (instrumentButtons[activeInstrument].y - rectY)/7
        rectangle = pygame.Rect(0, rectY - 10, 200, 115)
        pygame.draw.rect(screen, rectColors[activeInstrument], rectangle)

        rect2Y = rect2Y + (430 + onInstTab*110 - rect2Y)/7
        rectangle = pygame.Rect(0, rect2Y - 10, 200, 90)
        pygame.draw.rect(screen, [233,111,000], rectangle)

        rectangle = pygame.Rect(110,0,1000,800)
        pygame.draw.rect(screen, [55,55,55],rectangle)

        fpsClock.tick(30)


if __name__ == "__main__":
    main()

pygame.quit()
