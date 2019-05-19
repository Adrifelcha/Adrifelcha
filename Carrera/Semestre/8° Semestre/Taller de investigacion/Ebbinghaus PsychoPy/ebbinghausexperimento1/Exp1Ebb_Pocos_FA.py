from psychopy import visual, core, event, gui
import random, time

options={"Opcion":"1","Nombre":"Usuario1"}
myDlg=gui.DlgFromDict(dictionary=options, title="Gano")
if myDlg.OK:
	print "Ok"
else:
	core.quit()
    
mywindow= visual.Window(monitor="testMonitor", units="cm", fullscr=True, color="white")

mymouse= event.Mouse(mywindow)

mymouse.setVisible(0)

mywindow.setColor(color=[255,255,255], colorSpace="rgb255")
mywindow.update()
mywindow.setColor(color=[255,255,255], colorSpace="rgb255")
mywindow.update()
txtResults=visual.TextStim(mywindow,text="Instrucciones: "+"\n"+"\n"+"Se te mostraran dos circulos color azul claro: del lado izquierdo un circulo de referencia, aislado, y del lado derecho un circulo rodeado de otros circulos" +"\n"+"\n"+"Presiona la tecla S cuando el circulo central de la figura derecha sea del mismo tamano que el circulo del lado izquierdo. "+"\n"+"\n"+"Si este no es el caso, oprime N"+"\n"+"\n"+"Presiona la tecla E para continuar",color=[0,0,0], colorSpace="rgb255")
txtResults.draw()
mywindow.update()
while 'e' not in event.getKeys(): 
	core.wait(0.1)

ejemplo=[1]

mywindow.update()
for i in range (1):
	choice=ejemplo[random.randint(0,len(ejemplo)-1)]
	if choice==1:
		img1=visual.ImageStim(mywindow, image="ccentral.png", pos=[-12,-4], size=[3,3])

		img2=visual.ImageStim(mywindow, image="ccentral.png", pos=[5,-4], size=[2,2])

	img3=visual.ImageStim(mywindow, image="cexternochico2.png", pos=[5,-4], size=[8,10])

	txtResults=visual.TextStim(mywindow,text="Ejemplo: "+"\n"+"En este caso el circulo central de la figura derecha es mas pequeno que el circulo de referencia del lado izquierdo. Deberias presionar la tecla N porque NO son iguales",pos=[0,7], color=[0,0,0], colorSpace="rgb255")
	img1.draw()
	img2.draw()
	img3.draw()
	txtResults.draw()
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

mywindow.setColor(color=[255,255,255], colorSpace="rgb255")
mywindow.update()
mywindow.setColor(color=[255,255,255], colorSpace="rgb255")
mywindow.update()
txtResults=visual.TextStim(mywindow,text="Contesta TAN RAPIDO como puedas"+"\n"+"\n"+"Cada pareja de imagenes aparecera por SOLO 3 segundos. Para avanzar al siguiente ensayo, tienes que responder S o N"+"\n"+"\n"+"Asegurate de presionar SOLO UNA TECLA por ensayo. Los ensayos estan separados por una breve pantalla blanca, espera a que se te muestre un nuevo ensayo para responder."+"\n"+"\n"+"Presiona la tecla E para continuar",color=[0,0,0], colorSpace="rgb255")
txtResults.draw()
mywindow.update()
while 'e' not in event.getKeys(): 
	core.wait(0.1)

mywindow.setColor(color=[255,255,255], colorSpace="rgb255")
mywindow.update()
mywindow.setColor(color=[255,255,255], colorSpace="rgb255")
mywindow.update()
txtResults=visual.TextStim(mywindow,text="Recuerda: "+"\n"+"\n"+"Tecla S para SI SON IGUALES"+"\n"+"\n"+"Tecla N para NO SON IGUALES"+"\n"+"\n"+"Responde tan bien como puedas"+"\n"+"\n"+"Presiona la tecla E para comenzar el experimento",color=[0,0,0], colorSpace="rgb255")
txtResults.draw()

mywindow.update()
while 'e' not in event.getKeys(): 
	core.wait(0.1)
    
mybaseline=open("Pocos-FA"+"_"+ options["Nombre"]+"_"+time.strftime("%Y-%m-%d")+"_"+"Baseline.csv", 'w')

mytestline=open("Pocos-FA"+"_"+ options["Nombre"]+"_"+time.strftime("%Y-%m-%d")+"_"+"TestLine.csv", 'w')

right=[13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]

rightcounterb=0

wrongcounterb=0

falsealarmB=0

hitB=0

rejectionB=0

missB=0

rightcounterT=0

wrongcounterT=0

falsealarmT=0

hitT=0

rejectionT=0

missT=0

#central=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
central=list()
for i in range(48):
	for j in range (7):
		central.append (i+1)

mybaseline.write("Ensayo, Estimulo, Respuesta, Correcto, Aciertos, Errores, Hits, ContadorH, Rechazos, ContadorR, Falsas alarmas, ContadorF, Omisiones, ContadorM, \n")

mywindow.update()
for i in range (336):
	choice=central.pop(random.randint(0,len(central)-1))
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

		img2=visual.ImageStim(mywindow, image="ccentral.png", pos=[5,0.5], size=[2,2])

	        img3=visual.ImageStim(mywindow, image="cexternogrande3.png", pos=[4,0])
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

		img2=visual.ImageStim(mywindow, image="ccentral.png", pos=[5,0.5], size=[2.5,2.5])

	        img3=visual.ImageStim(mywindow, image="cexternogrande3.png", pos=[4,0])
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

	        img3=visual.ImageStim(mywindow, image="cexternochico2.png", pos=[5,0])
	if choice==15:
		img1=visual.ImageStim(mywindow, image="ccentral.png", pos=[-12,0], size=[3,3])

		img2=visual.ImageStim(mywindow, image="ccentral.png", pos=[5,0], size=[3,3])

	        img3=visual.ImageStim(mywindow, image="cexternochico2.png", pos=[5,0])
	if choice==16:
		img1=visual.ImageStim(mywindow, image="ccentral.png", pos=[-12,0], size=[3,3])

		img2=visual.ImageStim(mywindow, image="ccentral.png", pos=[5,0], size=[3,3])

	        img3=visual.ImageStim(mywindow, image="cexternochico2.png", pos=[5,0])
	if choice==17:
		img1=visual.ImageStim(mywindow, image="ccentral.png", pos=[-12,0], size=[3,3])

		img2=visual.ImageStim(mywindow, image="ccentral.png", pos=[5,0], size=[3,3])

	        img3=visual.ImageStim(mywindow, image="cexternogrande2.png", pos=[5,0])
	if choice==18:
		img1=visual.ImageStim(mywindow, image="ccentral.png", pos=[-12,0], size=[3,3])

		img2=visual.ImageStim(mywindow, image="ccentral.png", pos=[5,0], size=[3,3])

	        img3=visual.ImageStim(mywindow, image="cexternogrande2.png", pos=[5,0])
	if choice==19:
		img1=visual.ImageStim(mywindow, image="ccentral.png", pos=[-12,0], size=[3,3])

		img2=visual.ImageStim(mywindow, image="ccentral.png", pos=[5,0], size=[3,3])

	        img3=visual.ImageStim(mywindow, image="cexternogrande2.png", pos=[5,0])
	if choice==20:
		img1=visual.ImageStim(mywindow, image="ccentral.png", pos=[-12,0], size=[3,3])

		img2=visual.ImageStim(mywindow, image="ccentral.png", pos=[5,0], size=[3,3])

	        img3=visual.ImageStim(mywindow, image="cexternogrande2.png", pos=[5,0])
	if choice==21:
		img1=visual.ImageStim(mywindow, image="ccentral.png", pos=[-12,0], size=[3,3])

		img2=visual.ImageStim(mywindow, image="ccentral.png", pos=[5,0], size=[3,3])

	        img3=visual.ImageStim(mywindow, image="cexternochico3.png", pos=[4.5,1])
	if choice==22:
		img1=visual.ImageStim(mywindow, image="ccentral.png", pos=[-12,0], size=[3,3])

		img2=visual.ImageStim(mywindow, image="ccentral.png", pos=[5,0], size=[3,3])

	        img3=visual.ImageStim(mywindow, image="cexternochico3.png", pos=[4.5,1])
	if choice==23:
		img1=visual.ImageStim(mywindow, image="ccentral.png", pos=[-12,0], size=[3,3])

		img2=visual.ImageStim(mywindow, image="ccentral.png", pos=[5,0], size=[3,3])

	        img3=visual.ImageStim(mywindow, image="cexternochico3.png", pos=[4.5,1])
	if choice==24:
		img1=visual.ImageStim(mywindow, image="ccentral.png", pos=[-12,0], size=[3,3])

		img2=visual.ImageStim(mywindow, image="ccentral.png", pos=[5,0], size=[3,3])

	        img3=visual.ImageStim(mywindow, image="cexternochico3.png", pos=[4.5,1])
	if choice==25:
		img1=visual.ImageStim(mywindow, image="ccentral.png", pos=[-12,0], size=[3,3])

		img2=visual.ImageStim(mywindow, image="ccentral.png", pos=[5,0.5], size=[3,3])

	        img3=visual.ImageStim(mywindow, image="cexternogrande3.png", pos=[4,0])
	if choice==26:
		img1=visual.ImageStim(mywindow, image="ccentral.png", pos=[-12,0], size=[3,3])

		img2=visual.ImageStim(mywindow, image="ccentral.png", pos=[5,0.5], size=[3,3])

	        img3=visual.ImageStim(mywindow, image="cexternogrande3.png", pos=[4,0])
	if choice==27:
		img1=visual.ImageStim(mywindow, image="ccentral.png", pos=[-12,0], size=[3,3])

		img2=visual.ImageStim(mywindow, image="ccentral.png", pos=[5,0.5], size=[3,3])

	        img3=visual.ImageStim(mywindow, image="cexternogrande3.png", pos=[4,0])
	if choice==28:
		img1=visual.ImageStim(mywindow, image="ccentral.png", pos=[-12,0], size=[3,3])

		img2=visual.ImageStim(mywindow, image="ccentral.png", pos=[5,0.5], size=[3,3])

	        img3=visual.ImageStim(mywindow, image="cexternogrande3.png", pos=[4,0])
	if choice==29:
		img1=visual.ImageStim(mywindow, image="ccentral.png", pos=[-12,0], size=[3,3])

		img2=visual.ImageStim(mywindow, image="ccentral.png", pos=[5,0], size=[3,3])

	        img3=visual.ImageStim(mywindow, image="cexternochico4.png", pos=[5,0])
	if choice==30:
		img1=visual.ImageStim(mywindow, image="ccentral.png", pos=[-12,0], size=[3,3])

		img2=visual.ImageStim(mywindow, image="ccentral.png", pos=[5,0], size=[3,3])

	        img3=visual.ImageStim(mywindow, image="cexternochico4.png", pos=[5,0])
	if choice==31:
		img1=visual.ImageStim(mywindow, image="ccentral.png", pos=[-12,0], size=[3,3])

		img2=visual.ImageStim(mywindow, image="ccentral.png", pos=[5,0], size=[3,3])

	        img3=visual.ImageStim(mywindow, image="cexternochico4.png", pos=[5,0])
	if choice==32:
		img1=visual.ImageStim(mywindow, image="ccentral.png", pos=[-12,0], size=[3,3])

		img2=visual.ImageStim(mywindow, image="ccentral.png", pos=[5,0], size=[3,3])

	        img3=visual.ImageStim(mywindow, image="cexternochico4.png", pos=[5,0])
	if choice==33:
		img1=visual.ImageStim(mywindow, image="ccentral.png", pos=[-12,0], size=[3,3])

		img2=visual.ImageStim(mywindow, image="ccentral.png", pos=[5,0], size=[3,3])

	        img3=visual.ImageStim(mywindow, image="cexternogrande4.png", pos=[5,0], size=[22,22])
	if choice==34:
		img1=visual.ImageStim(mywindow, image="ccentral.png", pos=[-12,0], size=[3,3])

		img2=visual.ImageStim(mywindow, image="ccentral.png", pos=[5,0], size=[3,3])

	        img3=visual.ImageStim(mywindow, image="cexternogrande4.png", pos=[5,0], size=[22,22])
	if choice==35:
		img1=visual.ImageStim(mywindow, image="ccentral.png", pos=[-12,0], size=[3,3])

		img2=visual.ImageStim(mywindow, image="ccentral.png", pos=[5,0], size=[3,3])

	        img3=visual.ImageStim(mywindow, image="cexternogrande4.png", pos=[5,0], size=[22,22])
	if choice==36:
		img1=visual.ImageStim(mywindow, image="ccentral.png", pos=[-12,0], size=[3,3])

		img2=visual.ImageStim(mywindow, image="ccentral.png", pos=[5,0], size=[3,3])

	        img3=visual.ImageStim(mywindow, image="cexternogrande4.png", pos=[5,0], size=[22,22])
	if choice==37:
		img1=visual.ImageStim(mywindow, image="ccentral.png", pos=[-12,0], size=[3,3])

		img2=visual.ImageStim(mywindow, image="ccentral.png", pos=[5,0], size=[3.5,3.5])

	        img3=visual.ImageStim(mywindow, image="cexternochico2.png", pos=[5,0])
	if choice==38:
		img1=visual.ImageStim(mywindow, image="ccentral.png", pos=[-12,0], size=[3,3])

		img2=visual.ImageStim(mywindow, image="ccentral.png", pos=[5,0], size=[3.5,3.5])

	        img3=visual.ImageStim(mywindow, image="cexternogrande2.png", pos=[5,0])
	if choice==39:
		img1=visual.ImageStim(mywindow, image="ccentral.png", pos=[-12,0], size=[3,3])

		img2=visual.ImageStim(mywindow, image="ccentral.png", pos=[5,0], size=[3.5,3.5])

	        img3=visual.ImageStim(mywindow, image="cexternochico3.png", pos=[4.5,1])
	if choice==40:
		img1=visual.ImageStim(mywindow, image="ccentral.png", pos=[-12,0], size=[3,3])

		img2=visual.ImageStim(mywindow, image="ccentral.png", pos=[5,0.5], size=[3.5,3.5])

	        img3=visual.ImageStim(mywindow, image="cexternogrande3.png", pos=[4,0])
	if choice==41:
		img1=visual.ImageStim(mywindow, image="ccentral.png", pos=[-12,0], size=[3,3])

		img2=visual.ImageStim(mywindow, image="ccentral.png", pos=[5,0], size=[3.5,3.5])

	        img3=visual.ImageStim(mywindow, image="cexternochico4.png", pos=[5,0])
	if choice==42:
		img1=visual.ImageStim(mywindow, image="ccentral.png", pos=[-12,0], size=[3,3])

		img2=visual.ImageStim(mywindow, image="ccentral.png", pos=[5,0], size=[3.5,3.5])

	        img3=visual.ImageStim(mywindow, image="cexternogrande4.png", pos=[5,0], size=[22,22])
	if choice==43:
		img1=visual.ImageStim(mywindow, image="ccentral.png", pos=[-12,0], size=[3,3])

		img2=visual.ImageStim(mywindow, image="ccentral.png", pos=[5,0], size=[4,4])

	        img3=visual.ImageStim(mywindow, image="cexternochico2.png", pos=[5,0])
	if choice==44:
		img1=visual.ImageStim(mywindow, image="ccentral.png", pos=[-12,0], size=[3,3])

		img2=visual.ImageStim(mywindow, image="ccentral.png", pos=[5,0], size=[4,4])

	        img3=visual.ImageStim(mywindow, image="cexternogrande2.png", pos=[5,0])
	if choice==45:
		img1=visual.ImageStim(mywindow, image="ccentral.png", pos=[-12,0], size=[3,3])

		img2=visual.ImageStim(mywindow, image="ccentral.png", pos=[5,0], size=[4,4])

	        img3=visual.ImageStim(mywindow, image="cexternochico3.png", pos=[4.5,1])
	if choice==46:
		img1=visual.ImageStim(mywindow, image="ccentral.png", pos=[-12,0], size=[3,3])

		img2=visual.ImageStim(mywindow, image="ccentral.png", pos=[5,0.5], size=[4,4])

	        img3=visual.ImageStim(mywindow, image="cexternogrande3.png", pos=[4,0])
	if choice==47:
		img1=visual.ImageStim(mywindow, image="ccentral.png", pos=[-12,0], size=[3,3])

		img2=visual.ImageStim(mywindow, image="ccentral.png", pos=[5,0], size=[4,4])

	        img3=visual.ImageStim(mywindow, image="cexternochico4.png", pos=[5,0])
	if choice==48:
		img1=visual.ImageStim(mywindow, image="ccentral.png", pos=[-12,0], size=[3,3])

		img2=visual.ImageStim(mywindow, image="ccentral.png", pos=[5,0], size=[4,4])

	        img3=visual.ImageStim(mywindow, image="cexternogrande4.png", pos=[5,0], size=[22,22])
	img1.draw()

	img2.draw()
	
	img3.draw()

	mybaseline.close

	mywindow.update()
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
				mybaseline.Close()
				core.quit()
		core.wait(0.1)
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
	mybaseline.write(str(i)+","+str(choice)+","+str(userSel)+","+str(isCorrect)+","+str(rightcounterb)+","+str(wrongcounterb)+","+str(isHit)+","+str(hitB)+","+str(isRejection)+","+str(rejectionB)+","+str(isFalseAlarm)+","+str(falsealarmB)+","+str(isMiss)+","+str(missB)+","+"\n")
	mywindow.setColor(color=[255,255,255], colorSpace="rgb255")
	mywindow.update()
	mywindow.setColor(color=[255,255,255], colorSpace="rgb255")
	mywindow.update()
#	core.wait(1)

mywindow.setColor(color=[255,255,255], colorSpace="rgb255")
mywindow.update()

mywindow.setColor(color=[255,255,255], colorSpace="rgb255")
mywindow.update()
txtResults=visual.TextStim(mywindow,text="Resultados: "+"\n"+"\n"+"Respuesatas Correctas: "+str(rightcounterb)+"\n"+"Respuestas Incorrectas: "+str(wrongcounterb)+"\n"+"\n"+"Presiona la tecla E para continuar", color=[0,0,0], colorSpace="rgb255")
txtResults.draw()
mywindow.update()
while 'e' not in event.getKeys(): 
	core.wait(0.1)

mywindow.setColor(color=[255,255,255], colorSpace="rgb255")
mywindow.update()
mywindow.setColor(color=[255,255,255], colorSpace="rgb255")
mywindow.update()
txtResults=visual.TextStim(mywindow,text="Fase de Prueba: "+"\n"+"\n"+"La tarea y las instrucciones siguen siendo exactamente las mismas" +"\n"+"\n"+"PERO Esta vez acumularas PUNTOS NEGATIVOS cada vez que digas que los circulos SI SON iguales cuando de hecho NO sea el caso (Falsa Alarma)."+"\n"+"\n"+"Si terminas la prueba con 15 puntos negativos, o mas, se te bajara un punto en la calificacion final."+"\n"+"\n"+"Presiona la tecla E para comenzar.",color=[0,0,0], colorSpace="rgb255")
txtResults.draw()
mywindow.update()
while 'e' not in event.getKeys(): 
	core.wait(0.1)

mytestline.write("Ensayo, Estimulo, Respuesta, Correcto, Aciertos, Errores, Hits, ContadorH, Rechazos, ContadorR, Falsas alarmas, ContadorF, Omisiones, ContadorM, \n")

prueba=list()
for i in range(48):
	for j in range (7):
		prueba.append (i+1)
        
mywindow.update()
for i in range (336):
	choice=prueba.pop(random.randint(0,len(prueba)-1))
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

		img2=visual.ImageStim(mywindow, image="ccentral.png", pos=[5,0.5], size=[2,2])

	        img3=visual.ImageStim(mywindow, image="cexternogrande3.png", pos=[4,0])
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

		img2=visual.ImageStim(mywindow, image="ccentral.png", pos=[5,0.5], size=[2.5,2.5])

	        img3=visual.ImageStim(mywindow, image="cexternogrande3.png", pos=[4,0])
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

	        img3=visual.ImageStim(mywindow, image="cexternochico2.png", pos=[5,0])
	if choice==15:
		img1=visual.ImageStim(mywindow, image="ccentral.png", pos=[-12,0], size=[3,3])

		img2=visual.ImageStim(mywindow, image="ccentral.png", pos=[5,0], size=[3,3])

	        img3=visual.ImageStim(mywindow, image="cexternochico2.png", pos=[5,0])
	if choice==16:
		img1=visual.ImageStim(mywindow, image="ccentral.png", pos=[-12,0], size=[3,3])

		img2=visual.ImageStim(mywindow, image="ccentral.png", pos=[5,0], size=[3,3])

	        img3=visual.ImageStim(mywindow, image="cexternochico2.png", pos=[5,0])
	if choice==17:
		img1=visual.ImageStim(mywindow, image="ccentral.png", pos=[-12,0], size=[3,3])

		img2=visual.ImageStim(mywindow, image="ccentral.png", pos=[5,0], size=[3,3])

	        img3=visual.ImageStim(mywindow, image="cexternogrande2.png", pos=[5,0])
	if choice==18:
		img1=visual.ImageStim(mywindow, image="ccentral.png", pos=[-12,0], size=[3,3])

		img2=visual.ImageStim(mywindow, image="ccentral.png", pos=[5,0], size=[3,3])

	        img3=visual.ImageStim(mywindow, image="cexternogrande2.png", pos=[5,0])
	if choice==19:
		img1=visual.ImageStim(mywindow, image="ccentral.png", pos=[-12,0], size=[3,3])

		img2=visual.ImageStim(mywindow, image="ccentral.png", pos=[5,0], size=[3,3])

	        img3=visual.ImageStim(mywindow, image="cexternogrande2.png", pos=[5,0])
	if choice==20:
		img1=visual.ImageStim(mywindow, image="ccentral.png", pos=[-12,0], size=[3,3])

		img2=visual.ImageStim(mywindow, image="ccentral.png", pos=[5,0], size=[3,3])

	        img3=visual.ImageStim(mywindow, image="cexternogrande2.png", pos=[5,0])
	if choice==21:
		img1=visual.ImageStim(mywindow, image="ccentral.png", pos=[-12,0], size=[3,3])

		img2=visual.ImageStim(mywindow, image="ccentral.png", pos=[5,0], size=[3,3])

	        img3=visual.ImageStim(mywindow, image="cexternochico3.png", pos=[4.5,1])
	if choice==22:
		img1=visual.ImageStim(mywindow, image="ccentral.png", pos=[-12,0], size=[3,3])

		img2=visual.ImageStim(mywindow, image="ccentral.png", pos=[5,0], size=[3,3])

	        img3=visual.ImageStim(mywindow, image="cexternochico3.png", pos=[4.5,1])
	if choice==23:
		img1=visual.ImageStim(mywindow, image="ccentral.png", pos=[-12,0], size=[3,3])

		img2=visual.ImageStim(mywindow, image="ccentral.png", pos=[5,0], size=[3,3])

	        img3=visual.ImageStim(mywindow, image="cexternochico3.png", pos=[4.5,1])
	if choice==24:
		img1=visual.ImageStim(mywindow, image="ccentral.png", pos=[-12,0], size=[3,3])

		img2=visual.ImageStim(mywindow, image="ccentral.png", pos=[5,0], size=[3,3])

	        img3=visual.ImageStim(mywindow, image="cexternochico3.png", pos=[4.5,1])
	if choice==25:
		img1=visual.ImageStim(mywindow, image="ccentral.png", pos=[-12,0], size=[3,3])

		img2=visual.ImageStim(mywindow, image="ccentral.png", pos=[5,0.5], size=[3,3])

	        img3=visual.ImageStim(mywindow, image="cexternogrande3.png", pos=[4,0])
	if choice==26:
		img1=visual.ImageStim(mywindow, image="ccentral.png", pos=[-12,0], size=[3,3])

		img2=visual.ImageStim(mywindow, image="ccentral.png", pos=[5,0.5], size=[3,3])

	        img3=visual.ImageStim(mywindow, image="cexternogrande3.png", pos=[4,0])
	if choice==27:
		img1=visual.ImageStim(mywindow, image="ccentral.png", pos=[-12,0], size=[3,3])

		img2=visual.ImageStim(mywindow, image="ccentral.png", pos=[5,0.5], size=[3,3])

	        img3=visual.ImageStim(mywindow, image="cexternogrande3.png", pos=[4,0])
	if choice==28:
		img1=visual.ImageStim(mywindow, image="ccentral.png", pos=[-12,0], size=[3,3])

		img2=visual.ImageStim(mywindow, image="ccentral.png", pos=[5,0.5], size=[3,3])

	        img3=visual.ImageStim(mywindow, image="cexternogrande3.png", pos=[4,0])
	if choice==29:
		img1=visual.ImageStim(mywindow, image="ccentral.png", pos=[-12,0], size=[3,3])

		img2=visual.ImageStim(mywindow, image="ccentral.png", pos=[5,0], size=[3,3])

	        img3=visual.ImageStim(mywindow, image="cexternochico4.png", pos=[5,0])
	if choice==30:
		img1=visual.ImageStim(mywindow, image="ccentral.png", pos=[-12,0], size=[3,3])

		img2=visual.ImageStim(mywindow, image="ccentral.png", pos=[5,0], size=[3,3])

	        img3=visual.ImageStim(mywindow, image="cexternochico4.png", pos=[5,0])
	if choice==31:
		img1=visual.ImageStim(mywindow, image="ccentral.png", pos=[-12,0], size=[3,3])

		img2=visual.ImageStim(mywindow, image="ccentral.png", pos=[5,0], size=[3,3])

	        img3=visual.ImageStim(mywindow, image="cexternochico4.png", pos=[5,0])
	if choice==32:
		img1=visual.ImageStim(mywindow, image="ccentral.png", pos=[-12,0], size=[3,3])

		img2=visual.ImageStim(mywindow, image="ccentral.png", pos=[5,0], size=[3,3])

	        img3=visual.ImageStim(mywindow, image="cexternochico4.png", pos=[5,0])
	if choice==33:
		img1=visual.ImageStim(mywindow, image="ccentral.png", pos=[-12,0], size=[3,3])

		img2=visual.ImageStim(mywindow, image="ccentral.png", pos=[5,0], size=[3,3])

	        img3=visual.ImageStim(mywindow, image="cexternogrande4.png", pos=[5,0], size=[22,22])
	if choice==34:
		img1=visual.ImageStim(mywindow, image="ccentral.png", pos=[-12,0], size=[3,3])

		img2=visual.ImageStim(mywindow, image="ccentral.png", pos=[5,0], size=[3,3])

	        img3=visual.ImageStim(mywindow, image="cexternogrande4.png", pos=[5,0], size=[22,22])
	if choice==35:
		img1=visual.ImageStim(mywindow, image="ccentral.png", pos=[-12,0], size=[3,3])

		img2=visual.ImageStim(mywindow, image="ccentral.png", pos=[5,0], size=[3,3])

	        img3=visual.ImageStim(mywindow, image="cexternogrande4.png", pos=[5,0], size=[22,22])
	if choice==36:
		img1=visual.ImageStim(mywindow, image="ccentral.png", pos=[-12,0], size=[3,3])

		img2=visual.ImageStim(mywindow, image="ccentral.png", pos=[5,0], size=[3,3])

	        img3=visual.ImageStim(mywindow, image="cexternogrande4.png", pos=[5,0], size=[22,22])
	if choice==37:
		img1=visual.ImageStim(mywindow, image="ccentral.png", pos=[-12,0], size=[3,3])

		img2=visual.ImageStim(mywindow, image="ccentral.png", pos=[5,0], size=[3.5,3.5])

	        img3=visual.ImageStim(mywindow, image="cexternochico2.png", pos=[5,0])
	if choice==38:
		img1=visual.ImageStim(mywindow, image="ccentral.png", pos=[-12,0], size=[3,3])

		img2=visual.ImageStim(mywindow, image="ccentral.png", pos=[5,0], size=[3.5,3.5])

	        img3=visual.ImageStim(mywindow, image="cexternogrande2.png", pos=[5,0])
	if choice==39:
		img1=visual.ImageStim(mywindow, image="ccentral.png", pos=[-12,0], size=[3,3])

		img2=visual.ImageStim(mywindow, image="ccentral.png", pos=[5,0], size=[3.5,3.5])

	        img3=visual.ImageStim(mywindow, image="cexternochico3.png", pos=[4.5,1])
	if choice==40:
		img1=visual.ImageStim(mywindow, image="ccentral.png", pos=[-12,0], size=[3,3])

		img2=visual.ImageStim(mywindow, image="ccentral.png", pos=[5,0.5], size=[3.5,3.5])

	        img3=visual.ImageStim(mywindow, image="cexternogrande3.png", pos=[4,0])
	if choice==41:
		img1=visual.ImageStim(mywindow, image="ccentral.png", pos=[-12,0], size=[3,3])

		img2=visual.ImageStim(mywindow, image="ccentral.png", pos=[5,0], size=[3.5,3.5])

	        img3=visual.ImageStim(mywindow, image="cexternochico4.png", pos=[5,0])
	if choice==42:
		img1=visual.ImageStim(mywindow, image="ccentral.png", pos=[-12,0], size=[3,3])

		img2=visual.ImageStim(mywindow, image="ccentral.png", pos=[5,0], size=[3.5,3.5])

	        img3=visual.ImageStim(mywindow, image="cexternogrande4.png", pos=[5,0], size=[22,22])
	if choice==43:
		img1=visual.ImageStim(mywindow, image="ccentral.png", pos=[-12,0], size=[3,3])

		img2=visual.ImageStim(mywindow, image="ccentral.png", pos=[5,0], size=[4,4])

	        img3=visual.ImageStim(mywindow, image="cexternochico2.png", pos=[5,0])
	if choice==44:
		img1=visual.ImageStim(mywindow, image="ccentral.png", pos=[-12,0], size=[3,3])

		img2=visual.ImageStim(mywindow, image="ccentral.png", pos=[5,0], size=[4,4])

	        img3=visual.ImageStim(mywindow, image="cexternogrande2.png", pos=[5,0])
	if choice==45:
		img1=visual.ImageStim(mywindow, image="ccentral.png", pos=[-12,0], size=[3,3])

		img2=visual.ImageStim(mywindow, image="ccentral.png", pos=[5,0], size=[4,4])

	        img3=visual.ImageStim(mywindow, image="cexternochico3.png", pos=[4.5,1])
	if choice==46:
		img1=visual.ImageStim(mywindow, image="ccentral.png", pos=[-12,0], size=[3,3])

		img2=visual.ImageStim(mywindow, image="ccentral.png", pos=[5,0.5], size=[4,4])

	        img3=visual.ImageStim(mywindow, image="cexternogrande3.png", pos=[4,0])
	if choice==47:
		img1=visual.ImageStim(mywindow, image="ccentral.png", pos=[-12,0], size=[3,3])

		img2=visual.ImageStim(mywindow, image="ccentral.png", pos=[5,0], size=[4,4])

	        img3=visual.ImageStim(mywindow, image="cexternochico4.png", pos=[5,0])
	if choice==48:
		img1=visual.ImageStim(mywindow, image="ccentral.png", pos=[-12,0], size=[3,3])

		img2=visual.ImageStim(mywindow, image="ccentral.png", pos=[5,0], size=[4,4])

	        img3=visual.ImageStim(mywindow, image="cexternogrande4.png", pos=[5,0], size=[22,22])
	img1.draw()

	img2.draw()
	
	img3.draw()

	mytestline.close

	mywindow.update()
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
	isCorrect=(choice in right and userSel =='s') or (choice not in right and userSel =='n')
	if isCorrect: 
		rightcounterT=rightcounterT+1
	else:
		 wrongcounterT=wrongcounterT+1
	isHitTest=(choice in right and userSel =='s')
	if isHitTest: 
		hitT=hitT+1
	isFalseAlarmTest=(choice not in right and userSel =='s')
	if isFalseAlarmTest: 
		falsealarmT=falsealarmT+1
	isMissTest=(choice in right and userSel =='n')
	if isMissTest: 
		missT=missT+1
	isRejectionTest=(choice not in right and userSel =='n')
	if isRejectionTest: 
		rejectionT=rejectionT+1
	mytestline.write(str(i)+","+str(choice)+","+str(userSel)+","+str(isCorrect)+","+str(rightcounterT)+","+str(wrongcounterT)+","+str(isHitTest)+","+str(hitT)+","+str(isRejectionTest)+","+str(rejectionT)+","+str(isFalseAlarmTest)+","+str(falsealarmT)+","+str(isMissTest)+","+str(missT)+","+"\n")
	mywindow.setColor(color=[255,255,255], colorSpace="rgb255")
	mywindow.update()
	mywindow.setColor(color=[255,255,255], colorSpace="rgb255")
	mywindow.update()
#	core.wait(1)
mywindow.setColor(color=[255,255,255], colorSpace="rgb255")
mywindow.update()

mywindow.setColor(color=[255,255,255], colorSpace="rgb255")
mywindow.update()
txtResults=visual.TextStim(mywindow,text="Puntaje Final: "+"\n"+"\n"+"Puntos Negativos: "+str(falsealarmT)+"\n"+"\n"+"Presiona la tecla 'e' para continuar.",color=[0,0,0], colorSpace="rgb255")
txtResults.draw()
mywindow.update()
while 'e' not in event.getKeys(): 
	core.wait(0.1)

mywindow.setColor(color=[255,255,255], colorSpace="rgb255")
mywindow.update()
mywindow.setColor(color=[255,255,255], colorSpace="rgb255")
mywindow.update()
txtResults=visual.TextStim(mywindow,text="El experimento ha terminado."+"\n"+"\n"+"Muchisimas gracias por tu participacion."+"\n"+"\n"+"\n"+"\n"+"Presiona la tecla E para salir",color=[0,0,0], colorSpace="rgb255")
txtResults.draw()
mywindow.update()
while 'e' not in event.getKeys(): 
	core.wait(0.1)
