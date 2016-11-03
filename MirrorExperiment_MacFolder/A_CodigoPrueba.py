from psychopy import visual, core, event, gui
import random, time

options={"Experimento":"1","Opcion":"Y/N +Rating","Participante":"Usuario1"}
myDlg=gui.DlgFromDict(dictionary=options, title="Gano")
if myDlg.OK:
	print "Ok"
else:
	core.quit()

#
#WINDOW CONFIGURATION
#	
mywindow= visual.Window(monitor="testMonitor", units="cm", fullscr=True, color="white")
mymouse= event.Mouse(mywindow)
mymouse.setVisible(0)
mywindow.setColor(color=[255,255,255], colorSpace="rgb255")
mywindow.update()
mywindow.setColor(color=[255,255,255], colorSpace="rgb255")
mywindow.update()


#
#FIRST INSTRUCTIONS
#
txtResults=visual.TextStim(mywindow,text="Instrucciones: "+"\n"+"\n"+"Se te mostraran dos figuras de Ebbinghaus compuestas por un circulo (en color claro) rodeado por circulos de distinto tamano" +"\n"+"\n"+"Presiona la tecla S cuando los circulos centrales de ambas figuras SI sean del mismo tamano. "+"\n"+"\n"+"Si NO son iguales, oprime N"+"\n"+"\n"+"Presiona la barra espaciadora para continuar",wrapWidth = 30,color=[0,0,0], colorSpace="rgb255")
txtResults.draw()
mywindow.update()
while 'space' not in event.getKeys(): 
	core.wait(0.1)

#
#FIRST EXAMPLE
#
mywindow.update()
img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-10,0], size=[2.5,2.5])
img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0], size=[2,2])


txtResults=visual.TextStim(mywindow,text="Ejemplo: "+"\n"+"\n"+"En este caso el circulo central de la figura derecha es mas chico que el del lado izquierdo."+"\n"+"\n"+"Deberias presionar la tecla N porque NO son iguales",wrapWidth = 30,pos=[0,12], color=[0,0,0], colorSpace="rgb255")
txtRes=visual.TextStim(mywindow,text="Presiona N",wrapWidth = 30,pos=[0,-17], color=[0,0,0], colorSpace="rgb255")
img3.draw()
img4.draw()
txtResults.draw()
txtRes.draw()
mywindow.update()
	
userSel=" "
validkeys=['n']
while userSel !='n':
	keys=event.getKeys()
	for k in keys:
		if k in validkeys:
			userSel=k
		elif k=='escape': 
			myfile.Close()
			core.quit()
	core.wait(0.1)
#
#END OF FIRST EXAMPLE
#

mywindow.setColor(color=[255,255,255], colorSpace="rgb255")
mywindow.update()
mywindow.setColor(color=[255,255,255], colorSpace="rgb255")
mywindow.update()
txtResults=visual.TextStim(mywindow,text="Responde TAN RAPIDO como puedas, cada pareja a comparar se te mostrara SOLO POR 1 segundo"+"\n"+"\n"+"NO avanzaras al siguiente ensayo hasta que registres tu respuesta (S o N)."+"\n"+"\n"+"Los ensayos estan separados por una breve pantalla blanca, espera a que aparezca una nueva pareja para volver a responder."+"\n"+"\n"+"Presiona la barra espaciadora para continuar",wrapWidth = 30,color=[0,0,0], colorSpace="rgb255")
txtResults.draw()
mywindow.update()
while 'space' not in event.getKeys(): 
	core.wait(0.1)

mywindow.setColor(color=[255,255,255], colorSpace="rgb255")
mywindow.update()
mywindow.setColor(color=[255,255,255], colorSpace="rgb255")
mywindow.update()
txtResults=visual.TextStim(mywindow,text="Recuerda: "+"\n"+"\n"+"Tecla S = SI SON IGUALES"+"\n"+"\n"+"Tecla N = NO SON IGUALES"+"\n"+"\n"+"Presiona la barra espaciadora para comenzar el experimento",wrapWidth = 30,color=[0,0,0], colorSpace="rgb255",alignHoriz="center")
txtResults.draw()
mywindow.update()
while 'space' not in event.getKeys(): 
	core.wait(0.1)
#
#END OF INSTRUCTIONS
#


#
#VARIABLE INITIALIZATION
#
mybaseline=open("MirrorEx1"+"_"+options["Participante"]+"_"+time.strftime("%Y-%m-%d")+"_"+"Y_N+R.csv", 'w')
right=[2, 4, 6]
#Variables uses to count the four possible results in Signal Detection Theory: hit, false alarm, miss and rejection
#Variables for counting in the first block
rightcounterb=0
wrongcounterb=0
falsealarmB=0
hitB=0
rejectionB=0
missB=0
#Variables for counting in the second block
rightcounterT=0
wrongcounterT=0
falsealarmT=0
hitT=0
rejectionT=0
missT=0

#central=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
mybaseline.write("Ensayo, Estimulo, Respuesta, Correcto, Aciertos, Errores, Hits, ContadorH, Rechazos, ContadorR, Falsas alarmas, ContadorF, Omisiones, ContadorM, Confidence, \n")
mywindow.update()

#
#BEGIN OF FIRST BLOCK
#
for j in range(1):
	central = list()
	for i in range (6):
		central.append (i+1)
	for i in range (6):
		choice=central.pop(random.randint(0,len(central)-1))
		if choice==1:
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-7,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[7,0],size=[3,3])
		if choice==2:
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-7,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[7,0],size=[2,2])
		if choice==3:
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-7,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[7,0],size=[2,2])
		if choice==4:
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-7,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[7,0],size=[3,3])
		if choice==5:
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-7,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[7,0],size=[1,1])
		if choice==6:
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-7,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[7,0],size=[1,1])
#COLOCAMOS LOS TEXTOS/ ESTIMULOS CONTINUAMENTE PRESENTES
		txtRecordat1=visual.TextStim(mywindow,text="Los circulos centrales son iguales?",wrapWidth = 45,color=[0,0,0], pos=[0,9],  colorSpace="rgb255")
		txtRecordat2=visual.TextStim(mywindow,text="S = Si",wrapWidth = 45,color=[0,0,0], pos=[0,-5], colorSpace="rgb255")
		txtRecordat3=visual.TextStim(mywindow,text="N = No",wrapWidth = 45,color=[0,0,0], pos=[0,-9], colorSpace="rgb255")
		txtRecordat1.draw()
		txtRecordat2.draw()
		txtRecordat3.draw()
		img3.draw()
		img4.draw()
		mybaseline.close
		mywindow.update()
#Tiempo durante el cual aparece el ensayo (En segundos)
		core.wait(2)
		mywindow.setColor(color=[255,255,255], colorSpace="rgb255")
		mywindow.update()
		mywindow.setColor(color=[255,255,255], colorSpace="rgb255")
		mywindow.update()
		userSel=" "
		validkeys=['s', 'n']
		while userSel !='s' and userSel !='n':
			keys=event.getKeys()
			for k in keys:
				if k in validkeys:
					userSel=k
				elif k=='escape': 
					mytestline.Close()
					core.quit()
			core.wait(0.1)
		isSignal=(choice in right and userSel =='s') or (choice not in right and userSel =='s')
		if isSignal: 
			Respuesta='s'
		isNoise=(choice in right and userSel =='n') or (choice not in right and userSel =='n')
		if isNoise: 
			Respuesta='n'
		isCorrect=(choice in right and userSel =='s') or (choice not in right and userSel =='n')
		if isCorrect: 
			rightcounterb=rightcounterb+1
		else:
			 wrongcounterb=wrongcounterb+1
		isHit=(choice in right and userSel =='s')
		if isHit: 
			hitB=hitB+1
		isFalseAlarm=(choice not in right and userSel =='s')
		if isFalseAlarm: 
			falsealarmB=falsealarmB+1
		isMiss=(choice in right and userSel =='n')
		if isMiss: 
			missB=missB+1
		isRejection=(choice not in right and userSel =='n')
		if isRejection: 
			rejectionB=rejectionB+1
#		mybaseline.write(str(i)+","+str(choice)+","+str(userSel)+","+str(isCorrect)+","+str(rightcounterb)+","+str(wrongcounterb)+","+str(isHit)+","+str(hitB)+","+str(isRejection)+","+str(rejectionB)+","+str(isFalseAlarm)+","+str(falsealarmB)+","+str(isMiss)+","+str(missB)+","+"\n")
		mywindow.setColor(color=[255,255,255], colorSpace="rgb255")
		mywindow.update()
		mywindow.setColor(color=[255,255,255], colorSpace="rgb255")
		mywindow.update()
		core.wait(0.5)
		reglita=visual.ImageStim(mywindow, image="Reglita.png", pos=[0,0])
		reglita.draw()
		mywindow.update()
#Tiempo que dura la Reglita 
		core.wait(2)
		mywindow.setColor(color=[255,255,255], colorSpace="rgb255")
		mywindow.update()
		mywindow.setColor(color=[255,255,255], colorSpace="rgb255")
		mywindow.update()
		userSel=" "
		validkeys=['1', '2', '3']
		while userSel !='1' and userSel !='2' and userSel !='3':
			keys=event.getKeys()
			for k in keys:
				if k in validkeys:
					userSel=k
				elif k=='escape': 
					mytestline.Close()
					core.quit()
			core.wait(0.1)
		isHighOld=(isFalseAlarm and userSel =='3') or (isHit and userSel =='3')
		if isHighOld: 
			Confidence=6 
		isHighNew=(isRejection and userSel =='3') or (isMiss and userSel =='3')
		if isHighNew: 
			Confidence=1
		isMediumOld=(isFalseAlarm and userSel =='2') or (isHit and userSel =='2')
		if isMediumOld: 
			Confidence=5
		isMediumNew=(isRejection and userSel =='2') or (isMiss and userSel =='2')
		if isMediumNew: 
			Confidence=2
		isLowOld=(isFalseAlarm and userSel =='1') or (isHit and userSel =='1')
		if isLowOld: 
			Confidence=4
		isLowNew=(isRejection and userSel =='1') or (isMiss and userSel =='1')
		if isLowNew: 
			Confidence=3
		mybaseline.write(str(i)+","+str(choice)+","+str(Respuesta)+","+str(isCorrect)+","+str(rightcounterb)+","+str(wrongcounterb)+","+str(isHit)+","+str(hitB)+","+str(isRejection)+","+str(rejectionB)+","+str(isFalseAlarm)+","+str(falsealarmB)+","+str(isMiss)+","+str(missB)+","+str(Confidence)+","+"\n")
		mywindow.setColor(color=[255,255,255], colorSpace="rgb255")
		mywindow.update()
		mywindow.setColor(color=[255,255,255], colorSpace="rgb255")
		mywindow.update()
		core.wait(0.5)
#END OF ONE TEST
	#END OF A BLOCK OF 48 TESTS
#
#END OF THE FIRST BLOCK
#

mywindow.setColor(color=[255,255,255], colorSpace="rgb255")
mywindow.update()

mywindow.setColor(color=[255,255,255], colorSpace="rgb255")
mywindow.update()
txtResults=visual.TextStim(mywindow,text="Resultados: "+"\n"+"\n"+"Respuesatas Correctas: "+str(rightcounterb)+"\n"+"Respuestas Incorrectas: "+str(wrongcounterb)+"\n"+"\n"+"Presiona la tecla E para continuar",color=[0,0,0], colorSpace="rgb255")
txtResults.draw()
mywindow.update()
while 'e' not in event.getKeys(): 
	core.wait(0.1)



mywindow.setColor(color=[255,255,255], colorSpace="rgb255")
mywindow.update()
mywindow.setColor(color=[255,255,255], colorSpace="rgb255")
mywindow.update()
txtResults=visual.TextStim(mywindow,text="El experimento ha terminado."+"\n"+"\n"+"Haz hecho muy feliz a Felisa."+"\n"+"\n"+"Por supuesto que no tienes que depositar nada, sin importar tu puntaje"+"\n"+"\n"+"\n"+"\n"+"MUCHAS gracias por tu participacion"+"\n"+"\n"+"\n"+"\n"+"Presiona la tecla E para salir",color=[0,0,0], colorSpace="rgb255")
txtResults.draw()
mywindow.update()
while 'e' not in event.getKeys(): 
	core.wait(0.1)
