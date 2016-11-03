from psychopy import visual, core, event
#Creating window
myWin = visual.Window((800.0,800.0),allowGUI=False,winType='pyglet',
            monitor='testMonitor', units ='deg', screen=0)
myWin.recordFrameIntervals = True


#choose some fonts. If a list is provided, the first font found will be used.
fancy = ['Monotype Corsiva', 'Palace Script MT', 'Edwardian Script ITC']
sans = ['Gill Sans MT', 'Arial','Helvetica','Verdana'] #use the first font found on this list
serif = ['Times','Times New Roman'] #use the first font found on this list
comic = 'Comic Sans MS' #note the full name of the font - the short name won't work

opcion1 = visual.TextStim(myWin, 
                        text = "u1. Enviar al grupo de rescatistas a una escuela primaria con el 40 de probabilidad de salvar a 200 ninos.", wrapWidth=0.9,
                        units='norm', height=0.05,color='DarkSlateBlue',
                        pos=[-0.50,0]) 
opcion2 = visual.TextStim(myWin, 
                        text = "u2. Enviar al grupo de rescatistas a una oficina con el 60 de probabilidad de salvar a 400 trabajadores.", wrapWidth=0.9,
                        units='norm', height=0.05,color='DarkSlateBlue',
                        pos=[0.50,0]) 
trialClock = core.Clock()
t=lastFPSupdate=0;

# Continues the loop until one of these keys are pressed
while not event.getKeys(keyList=['q', 'p']):
    t=trialClock.getTime()
    opcion1.draw()
    opcion2.draw()
    myWin.flip()