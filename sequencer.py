
import globs
from globs import *
import synthepyzer_utils
from synthepyzer_utils import *
import pygame
from pygame import locals

class Note:
    def __init__(self,step,frequency,velocity,duration):
        self.step = step
        self.frequency = frequency
        self.velocity = velocity
        self.duration = duration

class Track:
    def __init__(self,instrumentID, repeat = 0):
        self.notes = []
        self.instrumentID = instrumentID
        self.repeat = repeat
    def addNote(self,step,frequency,velocity,duration):
        # i = 0
        # if len(self.notes) != 0:
        #     while i < len(self.notes) and self.notes[i] < step:
        #         i = i + 1
        #     self.notes.insert(i,Note(step,frequency,velocity,duration))
        # else:
        self.notes.append(Note(step,frequency,velocity,duration))
        # eventNotes = self.getNextNotes(0) 
        # if eventNotes == []:
        #     eventNotes = self.getNotesAtStep(0)
        # d = {"instrument":self.instrumentID, "notes":[],"next_notes":eventNotes}
        # e = pygame.event.Event(SEQUENCER_NOTE_EVENT, d)
        # pygame.event.post(e)
    def getNotesAtStep(self,step):
        output = []
        if self.repeat > 0:
            step = step%self.repeat 
        for note in self.notes:
            if step == note.step:
                output.append(note)
            elif step < note.step:
                break
        return output
    def clear(self):
        self.notes = []
    def getNextNotes(self,step):
        outputStep = -1
        if self.repeat > 0:
            step = step%self.repeat 
        for note in self.notes:
            if step < note.step and outputStep == -1:
                outputStep = note.step
        if outputStep == -1:
            if len(self.notes) > 0:
                return [self.notes[0]]
            else:
                return []
        return self.getNotesAtStep(outputStep)


class Sequencer:
    def __init__(self,beatsPerMinute,stepsPerBeat):
        self.tracks = []
        self.beatsPerMinute = beatsPerMinute
        self.stepsPerBeat = stepsPerBeat
        self.step = 0
        self.play()
    def clear(self):
        for track in self.tracks:
            track.clear()
    def addTrack(self,instrumentID, repeat = 0):
        self.tracks.append(Track(instrumentID,repeat))
    def play(self):
        step = 0
        pygame.time.set_timer(SEQUENCER_TIMER_EVENT, int(1/float(self.beatsPerMinute)*60*1000/self.stepsPerBeat))
        for track in self.tracks:
            d = {"instrument":track.instrumentID, "notes":[],"next_notes":track.getNextNotes(0)}
            e = pygame.event.Event(SEQUENCER_NOTE_EVENT, d)
            pygame.event.post(e)
    def pause(self):
        pygame.time.set_timer(SEQUENCER_TIMER_EVENT, 0)
    def stop(self):
        self.pause()
        self.clear()
        step = 0
    def update(self,event):
        if event.type == SEQUENCER_TIMER_EVENT:
            self.step = self.step + 1
            for track in self.tracks:
                notesToPlay = track.getNotesAtStep(self.step)
                if len(notesToPlay) > 0:
                    d = {"instrument":track.instrumentID, "notes":notesToPlay,"next_notes":track.getNextNotes(self.step)}
                    e = pygame.event.Event(SEQUENCER_NOTE_EVENT, d)
                    pygame.event.post(e)

    
