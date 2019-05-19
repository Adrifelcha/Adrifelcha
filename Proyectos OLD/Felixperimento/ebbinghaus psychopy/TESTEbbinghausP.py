from psychopy import visual, core, data, event, logging, sound, gui
import random

mywindow= visual.Window(monitor="testMonitor", units="cm", fullscr=True, color="white")

expName = 'Ebbinghaus'  # from the Builder filename that created this script
expInfo = {u'session': u'001', u'participant': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

Intructions_1Clock = core.Clock()
ISI_2 = core.StaticPeriod(mywindow=mywindow, screenHz=expInfo['frameRate'], name='ISI_2')
text_4 = visual.TextStim(mywindow=mywindow, ori=0, name='text_4',
    text="Welcome. You will see two letters on the screen that have been rotated. For each pair of letters, indicate if they are mirror images of each other when they two letters are in their normal upright position. (Ignore the rotations.)\r\n\r\nPress 'm' if they are mirror images of each other. Press 'n' if they are the same (not mirror images).  \r\n\r\nPress the 'm' to continue.",    font='Arial',
    pos=[0, 0], height=0.04, wrapWidth=.8,
    color='black', colorSpace='rgb', opacity=1,
    depth=-1.0)

mymouse= event.Mouse(visible=False)

central=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]

event.getKeys(keyList=['s','n'], timeStamped=False)

mywindow.update()
for i in range (30):
	choice=central[random.randint(0,len(central)-1)]
	if choice==1:
		img1=visual.ImageStim(mywindow, image="ccentral.png", pos=[-12,0], size=[3,3])

		img2=visual.ImageStim(mywindow, image="ccentral.png", pos=[5,0], size=[2,2])

	        img3=visual.ImageStim(mywindow, image="cexternochico2.png", pos=[5,0])
	if choice==2:
		img1=visual.ImageStim(mywindow, image="ccentral.png", pos=[-12,0], size=[3,3])

		img2=visual.ImageStim(mywindow, image="ccentral.png", pos=[5,0], size=[2,2])

	        img3=visual.ImageStim(mywindow, image="cexternogrande2.png", pos=[5,0])
	if choice==3:
		img1=visual.ImageStim(mywindow, image="ccentral.png", pos=[-12,0], size=[3,3])

		img2=visual.ImageStim(mywindow, image="ccentral.png", pos=[5,0], size=[2,2])

	        img3=visual.ImageStim(mywindow, image="cexternochico3.png", pos=[4.5,1])
	if choice==4:
		img1=visual.ImageStim(mywindow, image="ccentral.png", pos=[-12,0], size=[3,3])

		img2=visual.ImageStim(mywindow, image="ccentral.png", pos=[5,0], size=[2,2])

	        img3=visual.ImageStim(mywindow, image="cexternogrande3.png", pos=[5.3,-0.3])
	if choice==5:
		img1=visual.ImageStim(mywindow, image="ccentral.png", pos=[-12,0], size=[3,3])

		img2=visual.ImageStim(mywindow, image="ccentral.png", pos=[5,0], size=[2,2])

	        img3=visual.ImageStim(mywindow, image="cexternochico4.png", pos=[5,0])
	if choice==6:
		img1=visual.ImageStim(mywindow, image="ccentral.png", pos=[-12,0], size=[3,3])

		img2=visual.ImageStim(mywindow, image="ccentral.png", pos=[5,0], size=[2,2])

	        img3=visual.ImageStim(mywindow, image="cexternogrande4.png", pos=[5,0], size=[22,22])
	if choice==7:
		img1=visual.ImageStim(mywindow, image="ccentral.png", pos=[-12,0], size=[3,3])

		img2=visual.ImageStim(mywindow, image="ccentral.png", pos=[5,0], size=[2.5,2.5])

	        img3=visual.ImageStim(mywindow, image="cexternochico2.png", pos=[5,0])
	if choice==8:
		img1=visual.ImageStim(mywindow, image="ccentral.png", pos=[-12,0], size=[3,3])

		img2=visual.ImageStim(mywindow, image="ccentral.png", pos=[5,0], size=[2.5,2.5])

	        img3=visual.ImageStim(mywindow, image="cexternogrande2.png", pos=[5,0])
	if choice==9:
		img1=visual.ImageStim(mywindow, image="ccentral.png", pos=[-12,0], size=[3,3])

		img2=visual.ImageStim(mywindow, image="ccentral.png", pos=[5,0], size=[2.5,2.5])

	        img3=visual.ImageStim(mywindow, image="cexternochico3.png", pos=[4.5,1])
	if choice==10:
		img1=visual.ImageStim(mywindow, image="ccentral.png", pos=[-12,0], size=[3,3])

		img2=visual.ImageStim(mywindow, image="ccentral.png", pos=[5,0], size=[2.5,2.5])

	        img3=visual.ImageStim(mywindow, image="cexternogrande3.png", pos=[5.3,-0.3])
	if choice==11:
		img1=visual.ImageStim(mywindow, image="ccentral.png", pos=[-12,0], size=[3,3])

		img2=visual.ImageStim(mywindow, image="ccentral.png", pos=[5,0], size=[2.5,2.5])

	        img3=visual.ImageStim(mywindow, image="cexternochico4.png", pos=[5,0])
	if choice==12:
		img1=visual.ImageStim(mywindow, image="ccentral.png", pos=[-12,0], size=[3,3])

		img2=visual.ImageStim(mywindow, image="ccentral.png", pos=[5,0], size=[2.5,2.5])

	        img3=visual.ImageStim(mywindow, image="cexternogrande4.png", pos=[5,0], size=[22,22])
	if choice==13:
		img1=visual.ImageStim(mywindow, image="ccentral.png", pos=[-12,0], size=[3,3])

		img2=visual.ImageStim(mywindow, image="ccentral.png", pos=[5,0], size=[3,3])

	        img3=visual.ImageStim(mywindow, image="cexternochico2.png", pos=[5,0])
	if choice==14:
		img1=visual.ImageStim(mywindow, image="ccentral.png", pos=[-12,0], size=[3,3])

		img2=visual.ImageStim(mywindow, image="ccentral.png", pos=[5,0], size=[3,3])

	        img3=visual.ImageStim(mywindow, image="cexternogrande2.png", pos=[5,0])
	if choice==15:
		img1=visual.ImageStim(mywindow, image="ccentral.png", pos=[-12,0], size=[3,3])

		img2=visual.ImageStim(mywindow, image="ccentral.png", pos=[5,0], size=[3,3])

	        img3=visual.ImageStim(mywindow, image="cexternochico3.png", pos=[4.5,1])
	if choice==16:
		img1=visual.ImageStim(mywindow, image="ccentral.png", pos=[-12,0], size=[3,3])

		img2=visual.ImageStim(mywindow, image="ccentral.png", pos=[5,0], size=[3,3])

	        img3=visual.ImageStim(mywindow, image="cexternogrande3.png", pos=[5.3,-0.3])
	if choice==17:
		img1=visual.ImageStim(mywindow, image="ccentral.png", pos=[-12,0], size=[3,3])

		img2=visual.ImageStim(mywindow, image="ccentral.png", pos=[5,0], size=[3,3])

	        img3=visual.ImageStim(mywindow, image="cexternochico4.png", pos=[5,0])
	if choice==18:
		img1=visual.ImageStim(mywindow, image="ccentral.png", pos=[-12,0], size=[3,3])

		img2=visual.ImageStim(mywindow, image="ccentral.png", pos=[5,0], size=[3,3])

	        img3=visual.ImageStim(mywindow, image="cexternogrande4.png", pos=[5,0], size=[22,22])
	if choice==19:
		img1=visual.ImageStim(mywindow, image="ccentral.png", pos=[-12,0], size=[3,3])

		img2=visual.ImageStim(mywindow, image="ccentral.png", pos=[5,0], size=[3.5,3.5])

	        img3=visual.ImageStim(mywindow, image="cexternochico2.png", pos=[5,0])
	if choice==20:
		img1=visual.ImageStim(mywindow, image="ccentral.png", pos=[-12,0], size=[3,3])

		img2=visual.ImageStim(mywindow, image="ccentral.png", pos=[5,0], size=[3.5,3.5])

	        img3=visual.ImageStim(mywindow, image="cexternogrande2.png", pos=[5,0])
	if choice==21:
		img1=visual.ImageStim(mywindow, image="ccentral.png", pos=[-12,0], size=[3,3])

		img2=visual.ImageStim(mywindow, image="ccentral.png", pos=[5,0], size=[3.5,3.5])

	        img3=visual.ImageStim(mywindow, image="cexternochico3.png", pos=[4.5,1])
	if choice==22:
		img1=visual.ImageStim(mywindow, image="ccentral.png", pos=[-12,0], size=[3,3])

		img2=visual.ImageStim(mywindow, image="ccentral.png", pos=[5,0], size=[3.5,3.5])

	        img3=visual.ImageStim(mywindow, image="cexternogrande3.png", pos=[5.3,-0.3])
	if choice==23:
		img1=visual.ImageStim(mywindow, image="ccentral.png", pos=[-12,0], size=[3,3])

		img2=visual.ImageStim(mywindow, image="ccentral.png", pos=[5,0], size=[3.5,3.5])

	        img3=visual.ImageStim(mywindow, image="cexternochico4.png", pos=[5,0])
	if choice==24:
		img1=visual.ImageStim(mywindow, image="ccentral.png", pos=[-12,0], size=[3,3])

		img2=visual.ImageStim(mywindow, image="ccentral.png", pos=[5,0], size=[3.5,3.5])

	        img3=visual.ImageStim(mywindow, image="cexternogrande4.png", pos=[5,0], size=[22,22])
	if choice==25:
		img1=visual.ImageStim(mywindow, image="ccentral.png", pos=[-12,0], size=[3,3])

		img2=visual.ImageStim(mywindow, image="ccentral.png", pos=[5,0], size=[4,4])

	        img3=visual.ImageStim(mywindow, image="cexternochico2.png", pos=[5,0])
	if choice==26:
		img1=visual.ImageStim(mywindow, image="ccentral.png", pos=[-12,0], size=[3,3])

		img2=visual.ImageStim(mywindow, image="ccentral.png", pos=[5,0], size=[4,4])

	        img3=visual.ImageStim(mywindow, image="cexternogrande2.png", pos=[5,0])
	if choice==27:
		img1=visual.ImageStim(mywindow, image="ccentral.png", pos=[-12,0], size=[3,3])

		img2=visual.ImageStim(mywindow, image="ccentral.png", pos=[5,0], size=[4,4])

	        img3=visual.ImageStim(mywindow, image="cexternochico3.png", pos=[4.5,1])
	if choice==28:
		img1=visual.ImageStim(mywindow, image="ccentral.png", pos=[-12,0], size=[3,3])

		img2=visual.ImageStim(mywindow, image="ccentral.png", pos=[5,0], size=[4,4])

	        img3=visual.ImageStim(mywindow, image="cexternogrande3.png", pos=[5.3,-0.3])
	if choice==29:
		img1=visual.ImageStim(mywindow, image="ccentral.png", pos=[-12,0], size=[3,3])

		img2=visual.ImageStim(mywindow, image="ccentral.png", pos=[5,0], size=[4,4])

	        img3=visual.ImageStim(mywindow, image="cexternochico4.png", pos=[5,0])
	if choice==30:
		img1=visual.ImageStim(mywindow, image="ccentral.png", pos=[-12,0], size=[3,3])

		img2=visual.ImageStim(mywindow, image="ccentral.png", pos=[5,0], size=[4,4])

	        img3=visual.ImageStim(mywindow, image="cexternogrande4.png", pos=[5,0], size=[22,22])
	img1.draw()

	img2.draw()
	
	img3.draw()

	mywindow.update()
	while 's' or 'n' not in event.getKeys(): 
		core.wait(0.1)
		#if 'escape' in event.getKeys():
			#core.quit() 