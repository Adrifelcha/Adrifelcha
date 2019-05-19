#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import visual, core, data, event, logging, sound, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions

# Store info about the experiment session
expName = 'Ebbinghaus'  # from the Builder filename that created this script
expInfo = {u'session': u'001', u'participant': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = u'data' + os.sep + '%s_%s' %(expInfo['participant'], expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)
#save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win= visual.Window(monitor="testMonitor", units="cm", fullscr=True, color="white")

# Initialize components for Routine "Intructions_1"
Intructions_1Clock = core.Clock()
ISI_2 = core.StaticPeriod(win=win, name='ISI_2')
text_4 = visual.TextStim(win=win, ori=0, name='text_4',
    text="Welcome. You will see two letters on the screen that have been rotated. For each pair of letters, indicate if they are mirror images of each other when they two letters are in their normal upright position. (Ignore the rotations.)\r\n\r\nPress 'm' if they are mirror images of each other. Press 'n' if they are the same (not mirror images).  \r\n\r\nPress the 'm' to continue.",    font='Arial',
    pos=[0, 0], height=0.04, wrapWidth=.8,
    color='black', colorSpace='rgb', opacity=1,
    depth=-1.0)
   # Initialize components for Routine "Intructions_2"
Intructions_2Clock = core.Clock()
image_L_3 = visual.ImageStim(win=win, name='image_L_3',
    image='ccentral',
    pos=[-12,0], size=[3,3])
image_R_3 = visual.ImageStim(win=win, name='image_R_3',
    image='ccentral', pos=[5,0], size=[3,3])
image_N_3 = visual.ImageStim(win=win, name='image_N_3',
    image='cexternochico8', pos=[5,0], size=[3,3])
text_5 = visual.TextStim(win=win, ori=0, name='text_5',
    text="Here, the letter on the right is a mirror image of the letter on the left. They would still be different after mentally rotating them to line up. So press 'm' (different). If they are the same, you would press 'n'.\r\n\r\nTry to respond as accurately as you can. Also try to be fast, but emphasize being accurate. Press 'n' to start.",    font='Arial',
    pos=[0, -.2], height=0.05, wrapWidth=.8,
    color='black', colorSpace='rgb', opacity=1,
    depth=-3.0) 