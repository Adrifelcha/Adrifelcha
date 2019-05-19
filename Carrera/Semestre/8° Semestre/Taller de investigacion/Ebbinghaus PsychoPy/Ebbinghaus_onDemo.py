from __future__ import division  
from psychopy import visual, core, data, event, logging, sound, gui
from psychopy.constants import *  
import numpy as np  
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  

_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

expName = u'DemoOnEbbinghaus'  
expInfo = {u'session': u'001', u'participant': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  
expInfo['date'] = data.getDateStr()  
expInfo['expName'] = expName

filename = _thisDir + os.sep + u'data' + os.sep + '%s_%s' %(expInfo['participant'], expInfo['date'])
