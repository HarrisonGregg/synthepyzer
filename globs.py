# global variables


bits = 16
sample_rate = 44100

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (100, 100, 100)
RED = (255, 0, 0)

SCALES = { "CMAJOR" : [16.35,   18.35,   20.60,   21.83,   24.50,   27.50,   30.87,   32.70    ] , "DMAJOR" : [ 18.35,   20.60,   23.12,  24.50,   27.50,   30.87,   34.65,  36.71    ] , "EMAJOR" : [ 20.60,   23.12,  25.96,  27.50,   30.87,   34.65,  38.89,  41.20    ] , "FMAJOR" : [ 21.83,   24.50,   27.50,   29.14,  32.70,   36.71,   41.20,   43.65    ] , "GMAJOR" : [ 24.50,  27.50,  30.87,  32.70,  36.71,  41.20,  46.25, 49.00   ] , "AMAJOR" : [ 27.50,   30.87,   34.65,  36.71,   41.20,   46.25,  51.91,  55.00    ] , "BMAJOR" : [ 30.87,   34.65,  38.89,  41.20,   46.25,  51.91,  58.27,  61.74] }

USEREVENT = 25
KEYBOARD_EVENT = USEREVENT + 1
SEQUENCER_TIMER_EVENT = USEREVENT + 2
SEQUENCER_NOTE_EVENT = USEREVENT + 3
SLIDER_MOTION = USEREVENT + 4
BUTTON_DEPRESSED = USEREVENT + 5