from psychopy import visual, core, event, gui
import random, time


options={"Experimento":"2b","Descripcion":"Una Figura", "Procedimiento":"2AFC","Participante":"Usuario1"}
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

PantallaInicio=visual.ImageStim(mywindow, image="Bienvenido.png", pos=[0,0])
PantallaInicio.draw()
mywindow.update()
while 'space' not in event.getKeys(): #
	core.wait(0.1)
#
#FIRST INSTRUCTIONS
#
print "Total Time"
total_time = time.time()
mywindow.setColor(color=[255,255,255], colorSpace="rgb255")
mywindow.update()
mywindow.setColor(color=[255,255,255], colorSpace="rgb255")
mywindow.update()
#####Instrucciones1=visual.ImageStim(mywindow, image="Inst_1.png", pos=[0,0])
#####Instrucciones1.draw()
#####txtResults=visual.TextStim(mywindow,text="Instrucciones:"+"\n"+"\n"+"\n"+"\n"+"En la pantalla se te mostraran dos circulos en color claro cuyo tamano deberas comparar. El circulo del lado izquierdo permanecera aislado, como referencia. El circulo del lado derecho aparecera rodeado de un conjunto de circulos de distinto tamano" +"\n"+"\n"+"\n"+"\n"+"Presiona la tecla S cuando los circulos claros SI sean del mismo tamano. "+"\n"+"\n"+"Presiona la tecla N si NO son iguales"+"\n"+"\n"+"\n"+"\n"+"\n"+"\n"+"Presiona la barra espaciadora para continuar",wrapWidth = 45,color=[0,0,0], colorSpace="rgb255")
#####txtResults.draw()
txtInst1=visual.TextStim(mywindow,text="Instrucciones:",wrapWidth = 60,color=[0,0,0], pos=[0,14], colorSpace="rgb255")
txtInst2=visual.TextStim(mywindow,text="En el centro de la pantalla se te mostrara un circulo aislado cuyo tamano y posicion permaneceran constantes. Este sera nuestro Circulo de Referencia.",wrapWidth = 35,color=[0,0,0], pos=[0,0], colorSpace="rgb255")
txtInst3=visual.TextStim(mywindow,text="Presiona la barra espaciadora para continuar",wrapWidth = 60,color=[0,0,0], pos=[0,-15], colorSpace="rgb255")
img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7], size=[3,3])
txtInst1.draw()
txtInst2.draw()
txtInst3.draw()
img4.draw()
mywindow.update()
while 'space' not in event.getKeys(): 
	core.wait(0.1)

#
#FIRST EXAMPLE
#

#mywindow.update()
img1=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[17.5,-3])
img2=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[-17,-3])
img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7], size=[3,3])
img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-3], size=[3,3])
img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17,-3], size=[1,1])
txtResults=visual.TextStim(mywindow,text="A cada lado del Circulo de Referencia aparecera un circulo del mismo color rodeado por una serie de circulos de distinto tamano.",wrapWidth = 35,pos=[0,13], color=[0,0,0], colorSpace="rgb255")
txtRes=visual.TextStim(mywindow,text="Presiona la barra espaciadora para continuar",wrapWidth = 30,pos=[0,-15], color=[0,0,0], colorSpace="rgb255")
img1.draw()
img2.draw()
img3.draw()
img4.draw()
img5.draw()
txtResults.draw()
txtRes.draw()
mywindow.update()
while 'space' not in event.getKeys(): 
	core.wait(0.1)
    

mywindow.update()
img1=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[17.5,-3])
img2=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[-17,-3])
img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7], size=[3,3])
img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-3], size=[3,3])
img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17,-3], size=[1,1])
txtResults=visual.TextStim(mywindow,text="Tu tarea consiste en indicar, presionando la TECLA DERECHA o IZQUIERDA, cual de las figuras laterales tiene el circulo central que MAS SE PARECE (en tamano) al Circulo de Referencia.",wrapWidth = 35,pos=[0,12], color=[0,0,0], colorSpace="rgb255")
txtRes=visual.TextStim(mywindow,text="Presiona la barra espaciadora para continuar",wrapWidth = 30,pos=[0,-15], color=[0,0,0], colorSpace="rgb255")
img1.draw()
img2.draw()
img3.draw()
img4.draw()
img5.draw()
txtResults.draw()
txtRes.draw()
mywindow.update()
while 'space' not in event.getKeys(): 
	core.wait(0.1)
    
    

mywindow.update()
img2=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[17.5,-3])
img2=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[-17,-3])
img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7], size=[3,3])
img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-3], size=[3,3])
img6=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17,-3], size=[1,1])
txtResults=visual.TextStim(mywindow,text="Por ejemplo, en este caso el circulo central de la figura derecha es mucho mas pequeno que el Circulo de Referencia. En tanto que, el circulo del lado izquierdo parece tener el mismo tamano. Deberias presionar la Tecla IZQUIERDA",wrapWidth = 45,pos=[0,12], color=[0,0,0], colorSpace="rgb255")
txtRes=visual.TextStim(mywindow,text="Presiona la TECLA IZQUIERDA",wrapWidth = 30,pos=[0,-15], color=[0,0,0], colorSpace="rgb255")
img1.draw()
img2.draw()
img3.draw()
img4.draw()
img5.draw()
txtResults.draw()
txtRes.draw()
mywindow.update()
	
userSel=" "
validkeys=['left']
while userSel !='left':
	keys=event.getKeys()
	for k in keys:
		if k in validkeys:
			userSel=k
		elif k=='escape': 
			myfile.Close()
			core.quit()
	core.wait(0.1)

#INSTRUCCIONES  (2DA PARTE)
#Respecto de la REGLITA
#mywindow.update()
#imgx=visual.ImageStim(mywindow, image="Reglita.png", pos=[0,1.5])
#txtResults=visual.TextStim(mywindow,text="Posteriormente, se te presentara una escala como la siguiente: ",wrapWidth = 45,pos=[0,8], color=[0,0,0], colorSpace="rgb255")
#txtRes=visual.TextStim(mywindow,text="Deberas teclear el numero 1, 2 o el 3, dependiendo de que tan seguro estas de tu respuesta."+"\n"+"\n"+"\n"+"\n"+"Presiona la barra espaciadora para continuar",wrapWidth = 30,pos=[0,-7], color=[0,0,0], colorSpace="rgb255")
#imgx.draw()
#txtResults.draw()
#txtRes.draw()
#mywindow.update()
#while 'space' not in event.getKeys(): 
#	core.wait(0.1)
#mywindow.update()
#
#END OF FIRST EXAMPLE
#
mywindow.setColor(color=[255,255,255], colorSpace="rgb255")
mywindow.update()
mywindow.setColor(color=[255,255,255], colorSpace="rgb255")
mywindow.update()
txtResults=visual.TextStim(mywindow,text="En cada ensayo DEBERAS ELEGIR UNA de las dos figuras laterales: La que contenga el circulo central CUYO TAMANO SE PAREZCA MAS al Circulo de Referencia."+"\n"+"\n"+"\n"+"\n"+"Elige siempre la opcion de la cual estes mas seguro(a)"+"\n"+"\n"+"\n"+"\n"+"Presiona la barra espaciadora para continuar",wrapWidth = 45,color=[0,0,0], colorSpace="rgb255")
txtResults.draw()
mywindow.update()
while 'space' not in event.getKeys(): 
	core.wait(0.1)
    

mywindow.setColor(color=[255,255,255], colorSpace="rgb255")
mywindow.update()
mywindow.setColor(color=[255,255,255], colorSpace="rgb255")
mywindow.update()
txtResults=visual.TextStim(mywindow,text="Cada pareja a comparar se te mostrara por solo un par de segundos."+"\n"+"\n"+"\n"+"\n"+"NO avanzaras al siguiente ensayo hasta que registres tu respuesta."+"\n"+"\n"+"\n"+"\n"+"Una vez respondas, el programa esperara a que presiones la barra espaciadora para indicar que estas listo(a) para el siguiente ensayo"+"\n"+"\n"+"\n"+"\n"+"Los ensayos se presentara en distintos colores para facilitar su distincion, los colores NO SON INDICADORES de nada."+"\n"+"\n"+"\n"+"\n"+"Presiona la barra espaciadora para continuar",wrapWidth = 45,color=[0,0,0], colorSpace="rgb255")
txtResults.draw()
mywindow.update()
while 'space' not in event.getKeys(): 
	core.wait(0.1)


mywindow.setColor(color=[255,255,255], colorSpace="rgb255")
mywindow.update()
mywindow.setColor(color=[255,255,255], colorSpace="rgb255")
mywindow.update()
txtResults=visual.TextStim(mywindow,text="\n"+"\n"+"\n"+"\n"+"Presiona la barra espaciadora para comenzar el experimento",wrapWidth = 45,color=[0,0,0], colorSpace="rgb255",alignHoriz="center")
txtResults.draw()
mywindow.update()
while 'space' not in event.getKeys(): 
	core.wait(0.1)

#END OF INSTRUCTIONS
#


#
#VARIABLE INITIALIZATION
#
mybaseline=open("MirrorEx2b"+"_"+options["Participante"]+"_"+time.strftime("%Y-%m-%d")+"_"+"2AFC.csv", 'w')
signalright=[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100, 102, 104, 106, 108, 110, 112, 114, 116, 118, 120, 122, 124, 126, 128]
signalleft=[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99, 101, 103, 105, 107, 109, 111, 113, 115, 117, 119, 121, 123, 125, 127]
AS_AN=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32]
BS_BN=[33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64]
AS_BN=[65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96] 
BS_AN=[97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128]
AS_BS=[129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160]
Null_ASright=[130, 132, 134, 136, 138, 140, 142, 144, 146, 148, 150, 152, 154, 156, 158, 160]
AN_BN=[161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192]
Null_ANright=[162, 164, 166, 168, 170, 172, 174, 176, 178, 180, 182, 184, 186, 188, 190, 192]
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
mybaseline.write("Ensayo, Estimulo, Comparacion, SignallPosition, Respuesta, Eleccion, Correcto, OpcionPredicha, Aciertos, Errores, RTime1, RTime2, Hits, ContadorH, Rechazos, ContadorR, Falsas alarmas, ContadorF, Omisiones, ContadorM, \n")
mywindow.update()

#
#BEGIN OF FIRST BLOCK
#
for j in range(1):
	central = list()
	for i in range (192):
		central.append (i+1)
	for i in range (192):
#		choice=192
		choice=central.pop(random.randint(0,len(central)-1))
		if choice==1:
			img1=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[-17,-3])
			img2=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[17,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-3],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17,-3],size=[3,3])
		if choice==2:
			img1=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[-17,-3])
			img2=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[17,-2.8])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-3],size=[3,3])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17,-2.8],size=[2,2])
		if choice==3:
			img1=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[-17,-3])
			img2=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[17.5,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-3],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17.5,-3],size=[2.5,2.5])
		if choice==4:
			img1=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[-17,-3])
			img2=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[17,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-3],size=[2.5,2.5])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17,-3],size=[2,2])
		if choice==5:
			img1=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[-17,-3])
			img2=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[17,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-3],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17,-3],size=[1.5,1.5])
		if choice==6:
			img1=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[-17,-3])
			img2=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[17,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-3],size=[1.5,1.5])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17,-3],size=[2,2])
		if choice==7:
			img1=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[-17,-3])
			img2=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[17.3,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-3],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17.3,-3],size=[1,1])
		if choice==8:
			img1=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[-17,-3])
			img2=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[16.6,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-3],size=[1,1])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[16.6,-3],size=[2,2])
		if choice==9:
			img1=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[-17,-3])
			img2=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[17,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17.5,-3],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[16.4,-2.9],size=[3,3])
		if choice==10:
			img1=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[-17,-3])
			img2=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[17,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-18,-3],size=[3,3])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[16.5,-3],size=[2,2])
		if choice==11:
			img1=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[-17,-3])
			img2=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[18.5,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17.5,-3],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17.5,-2.7],size=[2.5,2.5])
		if choice==12:
			img1=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[-17,-3])
			img2=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[17,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17.6,-2.9],size=[2.5,2.5])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[16.5,-3],size=[2,2])
		if choice==13:
			img1=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[-17,-3])
			img2=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[17,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17.5,-3],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[16.5,-3],size=[1.5,1.5])
		if choice==14:
			img1=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[-17,-2.5])
			img2=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[17,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-18,-2.5],size=[1.5,1.5])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[16.5,-3],size=[2,2])
		if choice==15:
			img1=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[-17,-3])
			img2=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[18,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17.5,-3],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17,-2.8],size=[1,1])
		if choice==16:
			img1=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[-17.3,-3])
			img2=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[18,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17.8,-3],size=[1,1])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17.5,-3],size=[2,2])
		if choice==17:
			img1=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[-17,-3])
			img2=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[17,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-3],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17,-3],size=[3,3])
		if choice==18:
			img1=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[-17,-3])
			img2=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[17,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-3],size=[3,3])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17,-3],size=[2,2])
		if choice==19:
			img1=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[-17,-3])
			img2=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[17,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-3],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17,-3],size=[2.5,2.5])
		if choice==20:
			img1=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[-17,-3])
			img2=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[17,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-3],size=[2.5,2.5])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17,-3],size=[2,2])
		if choice==21:
			img1=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[-17,-3])
			img2=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[17,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-3],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17,-3],size=[1.5,1.5])
		if choice==22:
			img1=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[-17,-3])
			img2=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[17.5,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-3],size=[1.5,1.5])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17.5,-3],size=[2,2])
		if choice==23:
			img1=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[-17,-3])
			img2=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[17,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-3],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17,-3],size=[1,1])
		if choice==24:
			img1=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[-17,-3])
			img2=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[17,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-3],size=[1,1])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17,-3],size=[2,2])
		if choice==25:
			img1=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[-17,-3])
			img2=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[17.5,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-18,-3],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[16.5,-3],size=[3,3])
		if choice==26:
			img1=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[-17,-3])
			img2=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[17.5,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17.5,-3],size=[3,3])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[16.5,-2.7],size=[2,2])
		if choice==27:
			img1=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[-17,-3])
			img2=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[17,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-18,-3],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[16.5,-3],size=[2.5,2.5])
		if choice==28:
			img1=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[-17,-3])
			img2=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[17,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-18,-3],size=[2.5,2.5])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[16,-3],size=[2,2])
		if choice==29:
			img1=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[-17,-3])
			img2=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[17,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-18,-3],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[16,-3],size=[1.5,1.5])
		if choice==30:
			img1=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[-17,-3])
			img2=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[17.5,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17.5,-2.8],size=[1.5,1.5])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[16.5,-3],size=[2,2])
		if choice==31:
			img1=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[-17,-3])
			img2=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[17,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-18,-3],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[16.5,-3],size=[1,1])
		if choice==32:
			img1=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[-17,-3])
			img2=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[17,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-18,-2.8],size=[1,1])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[16,-3],size=[2,2])
		if choice==33:
			img1=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[-17,-3])
			img2=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[17,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-3],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17,-3.1],size=[3,3])
		if choice==34:
			img1=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[-17,-1])
			img2=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[17,-2])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17.5,-1],size=[3,3])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17,-2.1],size=[2,2])
		if choice==35:
			img1=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[-17,-2])
			img2=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[18,-1])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-2],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17.5,-1],size=[2.5,2.5])
		if choice==36:
			img1=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[-17,-3])
			img2=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[17,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-3],size=[2.5,2.5])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17,-3],size=[2,2])
		if choice==37:
			img1=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[-17,-3])
			img2=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[17,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-3],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17,-3],size=[1.5,1.5])
		if choice==38:
			img1=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[-17,-1])
			img2=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[17,-2])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17.5,-1],size=[1.5,1.5])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17,-2],size=[2,2])
		if choice==39:
			img1=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[-17,-2])
			img2=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[18,-1])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-2],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17.5,-1],size=[1,1])
		if choice==40:
			img1=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[-17,-3])
			img2=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[17,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-3],size=[1,1])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17,-3],size=[2,2])
		if choice==41:
			img1=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[-17,-3])
			img2=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[17,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-3],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17,-3],size=[3,3])
		if choice==42:
			img1=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[-17,-1])
			img2=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[17,-2])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-1],size=[3,3])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17,-2],size=[2,2])
		if choice==43:
			img1=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[-17,-2])
			img2=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[18,-1])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-2],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[18,-1],size=[2.5,2.5])
		if choice==44:
			img1=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[-17,-3])
			img2=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[17,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-3],size=[2.5,2.5])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17,-3],size=[2,2])
		if choice==45:
			img1=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[-17,-3])
			img2=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[17,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-3],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17,-3],size=[1.5,1.5])
		if choice==46:
			img1=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[-17,-1])
			img2=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[17,-2])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-1],size=[1.5,1.5])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17,-2],size=[2,2])
		if choice==47:
			img1=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[-17,-2])
			img2=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[18.5,-1])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-2],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[18.5,-1],size=[1,1])
		if choice==48:
			img1=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[-17,-3])
			img2=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[17,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-3],size=[1,1])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17,-3],size=[2,2])
		if choice==49:
			img1=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[-18,-1])
			img2=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[18.5,-1])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-18.5,-1],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[18,-1],size=[3,3])
		if choice==50:
			img1=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[-17,-2])
			img2=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[18.5,-1])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-2],size=[3,3])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[18,-1],size=[2,2])
		if choice==51:
			img1=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[-17,-1])
			img2=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[17,-2])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17.5,-1],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17,-2],size=[2.5,2.5])
		if choice==52:
			img1=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[-18,-1])
			img2=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[18.5,-1])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-18.5,-1],size=[2.5,2.5])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[18,-1],size=[2,2])
		if choice==53:
			img1=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[-18,-1])
			img2=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[18,-1])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-18.5,-1],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17.5,-1],size=[1.5,1.5])
		if choice==54:
			img1=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[-17,-2])
			img2=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[18,-1])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-2],size=[1.5,1.5])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17.5,-1],size=[2,2])
		if choice==55:
			img1=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[-17,-1])
			img2=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[17,-2])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17.5,-1],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17,-2],size=[1,1])
		if choice==56:
			img1=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[-17,-1])
			img2=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[18,-1])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17.5,-1],size=[1,1])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17.5,-1],size=[2,2])
		if choice==57:
			img1=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[-18,-1])
			img2=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[18,-1])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-18,-1],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[18,-1],size=[3,3])
		if choice==58:
			img1=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[-17,-2])
			img2=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[18,-1])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-2],size=[3,3])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[18,-1],size=[2,2])
		if choice==59:
			img1=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[-17,-1])
			img2=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[17,-2])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-1],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17,-2],size=[2.5,2.5])
		if choice==60:
			img1=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[-18,-1])
			img2=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[18,-1])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-18,-1],size=[2.5,2.5])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[18,-1],size=[2,2])
		if choice==61:
			img1=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[-18,-1])
			img2=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[18,-1])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-18,-1],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[18,-1],size=[1.5,1.5])
		if choice==62:
			img1=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[-17,-2])
			img2=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[18,-1])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-2],size=[1.5,1.5])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[18,-1],size=[2,2])
		if choice==63:
			img1=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[-17,-1])
			img2=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[17,-2])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-1],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17,-2],size=[1,1])
		if choice==64:
			img1=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[-18,-1])
			img2=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[18,-1])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-18,-1],size=[1,1])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[18,-1],size=[2,2])
		if choice==65:
			img1=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[-17,-3])
			img2=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[17,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-3],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17,-3],size=[3,3])
		if choice==66:
			img1=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[-18,-1])
			img2=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[17,-2])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-1],size=[2.5,2.5])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[18,-2],size=[2,2])
		if choice==67:
			img1=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[-17,-3])
			img2=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[17,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-3],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17,-3],size=[1.5,1.5])
		if choice==68:
			img1=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[-17,-1])
			img2=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[17,-2])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17.5,-1],size=[1,1])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17,-2],size=[2,2])
		if choice==69:
			img1=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[-17,-2])
			img2=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[18,-1])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-2],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[18,-1],size=[3,3])
		if choice==70:
			img1=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[-17,-3])
			img2=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[17,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-3],size=[2.5,2.5])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17,-3],size=[2,2])
		if choice==71:
			img1=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[-17,-2])
			img2=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[18,-1])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-2],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17.5,-1],size=[1.5,1.5])
		if choice==72:
			img1=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[-17,-3])
			img2=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[17,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-3],size=[1,1])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17,-3],size=[2,2])
		if choice==73:
			img1=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[-17,-3])
			img2=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[17,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17.5,-3],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17,-3],size=[3,3])
		if choice==74:
			img1=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[-17,-1])
			img2=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[17,-2])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17.5,-1],size=[2.5,2.5])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[16.5,-2],size=[2,2])
		if choice==75:
			img1=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[-17,-2])
			img2=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[18,-1])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17.5,-2],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17.5,-1],size=[3,3])
		if choice==76:
			img1=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[-17,-3])
			img2=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[17,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-3],size=[2.5,2.5])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[16.5,-3],size=[2,2])
		if choice==77:
			img1=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[-17,-3])
			img2=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[17,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17.5,-3],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17,-3],size=[1.5,1.5])
		if choice==78:
			img1=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[-17,-1])
			img2=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[17,-2])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-1],size=[1,1])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[16.5,-2],size=[2,2])
		if choice==79:
			img1=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[-17,-2])
			img2=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[18,-1])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17.5,-2],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[18,-1],size=[1.5,1.5])
		if choice==80:
			img1=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[-17,-3])
			img2=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[17,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-3],size=[1,1])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[16.5,-3],size=[2,2])
		if choice==81:
			img1=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[-17,-2])
			img2=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[18,-1])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-2],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17.5,-1],size=[2.5,2.5])
		if choice==82:
			img1=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[-17,-3])
			img2=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[17,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-3],size=[3,3])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17,-3],size=[2,2])
		if choice==83:
			img1=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[-17,-3])
			img2=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[17,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-3],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17,-3],size=[2.5,2.5])
		if choice==84:
			img1=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[-17,-1])
			img2=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[17,-2])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17.5,-1],size=[3,3])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17,-2],size=[2,2])
		if choice==85:
			img1=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[-17,-2])
			img2=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[18,-1])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-2],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[18,-1],size=[1,1])
		if choice==86:
			img1=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[-17,-3])
			img2=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[17,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-3],size=[1.5,1.5])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17,-3],size=[2,2])
		if choice==87:
			img1=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[-17,-3])
			img2=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[17,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-3],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17,-3],size=[1,1])
		if choice==88:
			img1=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[-17,-1])
			img2=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[17,-2])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-1],size=[1.5,1.5])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17,-2],size=[2,2])
		if choice==89:
			img1=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[-17,-2])
			img2=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[18,-1])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-18,-2],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[18,-1],size=[2.5,2.5])
		if choice==90:
			img1=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[-17,-3])
			img2=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[17,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-3],size=[3,3])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[16,-3],size=[2,2])
		if choice==91:
			img1=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[-17,-2])
			img2=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[18,-1])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-18,-2],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17.5,-1],size=[1,1])
		if choice==92:
			img1=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[-17,-3])
			img2=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[17,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-3],size=[1.5,1.5])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[15.9,-2.7],size=[2,2])
		if choice==93:
			img1=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[-16.5,-3])
			img2=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[17,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17.5,-3],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17,-3],size=[2.5,2.5])
		if choice==94:
			img1=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[-17,-1])
			img2=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[18,-2])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-1],size=[3,3])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17,-2],size=[2,2])
		if choice==95:
			img1=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[-17,-3])
			img2=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[17,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-18,-3],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17,-3],size=[1,1])
		if choice==96:
			img1=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[-17,-1])
			img2=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[18,-2])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17.5,-1],size=[1.5,1.5])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17,-2],size=[2,2])
		if choice==97:
			img1=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[-17,-2])
			img2=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[18,-1])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-2],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17.5,-1],size=[2.5,2.5])
		if choice==98:
			img1=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[-17,-3])
			img2=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[17,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-3],size=[3,3])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17,-3],size=[2,2])
		if choice==99:
			img1=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[-17,-3])
			img2=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[17,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-3],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17,-3],size=[2.5,2.5])
		if choice==100:
			img1=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[-17,-1])
			img2=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[17,-2])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17.5,-1],size=[3,3])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17,-2],size=[2,2])
		if choice==101:
			img1=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[-17,-2])
			img2=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[18,-1])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-2],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[18,-1],size=[1,1])
		if choice==102:
			img1=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[-17,-3])
			img2=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[17,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-3],size=[1.5,1.5])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17,-3],size=[2,2])
		if choice==103:
			img1=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[-17,-3])
			img2=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[17,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-3.1],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17,-3.2],size=[1,1])
		if choice==104:
			img1=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[-17,-1])
			img2=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[17,-2])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-1],size=[1.5,1.5])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17,-2],size=[2,2])
		if choice==105:
			img1=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[-17,-3])
			img2=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[17,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17.5,-3],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17,-3.1],size=[3,3])
		if choice==106:
			img1=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[-17,-1])
			img2=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[17,-2])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-1],size=[2.5,2.5])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[16.5,-2],size=[2,2])
		if choice==107:
			img1=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[-17,-3])
			img2=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[17,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17.5,-3],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17,-3],size=[1.5,1.5])
		if choice==108:
			img1=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[-17,-1])
			img2=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[17,-2])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17.5,-1],size=[1,1])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[16.5,-2],size=[2,2])
		if choice==109:
			img1=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[-17,-2])
			img2=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[18,-1])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17.5,-2],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[18,-1],size=[3,3])
		if choice==110:
			img1=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[-17,-3])
			img2=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[17,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17.5,-3],size=[2.5,2.5])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17,-3],size=[2,2])
		if choice==111:
			img1=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[-17,-2])
			img2=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[18,-1])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17.5,-2],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17.5,-1],size=[1.5,1.5])
		if choice==112:
			img1=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[-17,-3])
			img2=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[17,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-3],size=[1,1])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[16.5,-3],size=[2,2])
		if choice==113:
			img1=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[-17,-1])
			img2=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[17,-2])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17.5,-1],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[16,-1.8],size=[2.5,2.5])
		if choice==114:
			img1=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[-17,-2])
			img2=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[18,-1])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-2],size=[3,3])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17.5,-1],size=[2,2])
		if choice==115:
			img1=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[-17,-1])
			img2=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[17,-2])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17.5,-1],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17,-2],size=[1,1])
		if choice==116:
			img1=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[-17,-2])
			img2=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[18,-1])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17.5, -2],size=[1.5,1.5])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17.5,-1],size=[2,2])
		if choice==117:
			img1=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[-17,-1])
			img2=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[17,-2])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17.5,-1],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17,-2],size=[2.5,2.5])
		if choice==118:
			img1=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[-17,-2])
			img2=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[18,-1])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-18,-2],size=[3,3])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17.5,-1],size=[2,2])
		if choice==119:
			img1=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[-17,-1])
			img2=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[17,-2])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17.5,-1],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[16.5,-2],size=[1,1])
		if choice==120:
			img1=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[-17,-2])
			img2=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[18,-1])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-2],size=[1.5,1.5])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17.5,-1],size=[2,2])
		if choice==121:
			img1=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[-17,-3])
			img2=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[17,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-18,-3],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17,-3],size=[3,3])
		if choice==122:
			img1=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[-17,-1])
			img2=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[17,-2])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17.5,-1],size=[2.5,2.5])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[16,-2],size=[2,2])
		if choice==123:
			img1=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[-17,-2])
			img2=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[18.5,-1])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-18,-2],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[18,-1],size=[3,3])
		if choice==124:
			img1=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[-17,-3])
			img2=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[17,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-3],size=[2.5,2.5])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[16,-3],size=[2,2])
		if choice==125:
			img1=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[-17,-2])
			img2=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[18,-1])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-18,-2],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[18,-1],size=[1.5,1.5])
		if choice==126:
			img1=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[-17,-1])
			img2=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[17,-2])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-1],size=[1,1])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[16,-1.8],size=[2,2])
		if choice==127:
			img1=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[-17,-2])
			img2=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[17,-1])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-18,-1.8],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17,-1],size=[1.5,1.5])
		if choice==128:
			img1=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[-17,-3])
			img2=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[17,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-3],size=[1,1])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[16,-2.8],size=[2,2])
		if choice==129:
			img1=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[-17,-3])
			img2=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[17,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-3],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17,-3],size=[2,2])
		if choice==130:
			img1=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[-17,-3])
			img2=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[17,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-3],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17,-3],size=[2,2])
		if choice==131:
			img1=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[-17,-3])
			img2=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[17,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-3],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17,-3],size=[2,2])
		if choice==132:
			img1=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[-17,-3])
			img2=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[17,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-3],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17,-3],size=[2,2])
		if choice==133:
			img1=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[-17,-3])
			img2=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[17,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-3],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17,-3],size=[2,2])
		if choice==134:
			img1=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[-17,-3])
			img2=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[17,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-3],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17,-3],size=[2,2])
		if choice==135:
			img1=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[-17,-3])
			img2=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[17,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-18,-3],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17,-3],size=[2,2])
		if choice==136:
			img1=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[-17,-3])
			img2=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[17,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-3],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[16,-3],size=[2,2])
		if choice==137:
			img1=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[-17,-3])
			img2=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[17,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17.5,-3],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17,-3],size=[2,2])
		if choice==138:
			img1=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[-17,-1])
			img2=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[17,-2])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17.5,-1],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[16.5,-2],size=[2,2])
		if choice==139:
			img1=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[-17,-3])
			img2=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[17,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17.5,-3],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17,-3],size=[2,2])
		if choice==140:
			img1=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[-17,-3])
			img2=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[17,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-3],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[16.5,-3],size=[2,2])
		if choice==141:
			img1=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[-17,-3])
			img2=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[17,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-3],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17,-3],size=[2,2])
		if choice==142:
			img1=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[-17,-3])
			img2=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[17,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-3],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17,-3],size=[2,2])
		if choice==143:
			img1=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[-17,-3])
			img2=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[17,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-18,-2.8],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17,-3],size=[2,2])
		if choice==144:
			img1=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[-17,-3])
			img2=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[17,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-3],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[16,-2.8],size=[2,2])
		if choice==145:
			img1=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[-17,-2])
			img2=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[18,-1])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-2],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17.5,-1],size=[2,2])
		if choice==146:
			img1=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[-17,-1])
			img2=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[17,-2])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17.5,-1],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17,-2],size=[2,2])
		if choice==147:
			img1=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[-17,-2])
			img2=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[18,-1])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17.5,-2],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17.5,-1],size=[2,2])
		if choice==148:
			img1=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[-17,-1])
			img2=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[17,-2])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17.5,-1],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[16.5,-2],size=[2,2])
		if choice==149:
			img1=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[-17,-2])
			img2=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[18,-1])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-2],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17.5,-1],size=[2,2])
		if choice==150:
			img1=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[-17,-1])
			img2=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[17,-2])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17.5,-1],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17,-2],size=[2,2])
		if choice==151:
			img1=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[-17,-2])
			img2=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[18,-1])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-2],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[18,-1],size=[2,2])
		if choice==152:
			img1=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[-17,-1])
			img2=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[17,-2])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-1],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17,-2],size=[2,2])
		if choice==153:
			img1=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[-17,-2])
			img2=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[18,-1])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-2],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[18,-1],size=[2,2])
		if choice==154:
			img1=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[-17,-1])
			img2=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[17,-2])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-1],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17,-2],size=[2,2])
		if choice==155:
			img1=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[-17,-2])
			img2=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[18,-1])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17.5,-2],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[18,-1],size=[2,2])
		if choice==156:
			img1=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[-17,-1])
			img2=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[17,-2])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-1],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[16.5,-2],size=[2,2])
		if choice==157:
			img1=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[-17,-2])
			img2=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[18,-1])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-18,-2],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17.5,-1],size=[2,2])
		if choice==158:
			img1=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[-17,-1])
			img2=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[17,-2])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17.5,-1],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[16,-1.8],size=[2,2])
		if choice==159:
			img1=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[-17,-2])
			img2=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[18,-1])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-18,-1.8],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[18,-1],size=[2,2])
		if choice==160:
			img1=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[-17,-1])
			img2=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[17,-2])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-1],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[16,-1.8],size=[2,2])
		if choice==161:
			img1=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[-17,-3])
			img2=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[17,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-3],size=[3,3])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17,-3],size=[3,3])
		if choice==162:
			img1=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[-17,-1])
			img2=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[17,-2])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17.5,-1],size=[3,3])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17,-2],size=[3,3])
		if choice==163:
			img1=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[-17,-2])
			img2=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[18,-1])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17.5,-2],size=[3,3])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17.5,-1],size=[3,3])
		if choice==164:
			img1=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[-17,-3])
			img2=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[17,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-3],size=[3,3])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[16.5,-3],size=[3,3])
		if choice==165:
			img1=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[-17,-3])
			img2=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[17,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-3],size=[3,3])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17,-3],size=[3,3])
		if choice==166:
			img1=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[-17,-1])
			img2=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[17,-2])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-1],size=[3,3])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17,-2],size=[3,3])
		if choice==167:
			img1=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[-17,-2])
			img2=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[18,-1])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-18,-1.8],size=[3,3])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[18,-1],size=[3,3])
		if choice==168:
			img1=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[-17,-3])
			img2=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[17,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-3],size=[3,3])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[16,-2.8],size=[3,3])
		if choice==169:
			img1=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[-17,-2])
			img2=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[18,-1])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-2],size=[2.5,2.5])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[18,-1],size=[2.5,2.5])
		if choice==170:
			img1=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[-17,-1])
			img2=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[17,-2])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-1],size=[2.5,2.5])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17,-2],size=[2.5,2.5])
		if choice==171:
			img1=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[-17,-3])
			img2=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[17,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,3],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17.5,-3],size=[2.5,2.5])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17,-3],size=[2.5,2.5])
		if choice==172:
			img1=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[-17,-1])
			img2=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[17,-2])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-1],size=[2.5,2.5])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[16.5,-1.8],size=[2.5,2.5])
		if choice==173:
			img1=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[-17,-2])
			img2=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[17,-1])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-2],size=[2.5,2.5])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[16.5,-1],size=[2.5,2.5])
		if choice==174:
			img1=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[-17,-3])
			img2=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[17,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-3],size=[2.5,2.5])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17,-3],size=[2.5,2.5])
		if choice==175:
			img1=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[-17,-3])
			img2=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[17,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-18,-2.8],size=[2.5,2.5])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17,-3],size=[2.5,2.5])
		if choice==176:
			img1=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[-17,-1])
			img2=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[17,-2])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17.5,-1],size=[2.5,2.5])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[16,-1.8],size=[2.5,2.5])
		if choice==177:
			img1=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[-17,-2])
			img2=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[18,-1])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-2],size=[1.5,1.5])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17.5,-1],size=[1.5,1.5])
		if choice==178:
			img1=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[-17,-3])
			img2=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[17,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-3],size=[1.5,1.5])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17,-3],size=[1.5,1.5])
		if choice==179:
			img1=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[-17,-3])
			img2=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[17,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17.5,-3],size=[1.5,1.5])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17,-3],size=[1.5,1.5])
		if choice==180:
			img1=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[-17,-1])
			img2=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[17,-2])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17.5,-1],size=[1.5,1.5])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[16.5,-2],size=[1.5,1.5])
		if choice==181:
			img1=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[-17,-2])
			img2=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[18,-1])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-2],size=[1.5,1.5])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[18,-1],size=[1.5,1.5])
		if choice==182:
			img1=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[-17,-3])
			img2=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[17,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-3],size=[1.5,1.5])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17,-3],size=[1.5,1.5])
		if choice==183:
			img1=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[-17,-3])
			img2=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[17,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-18,-2.8],size=[1.5,1.5])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17,-3],size=[1.5,1.5])
		if choice==184:
			img1=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[-17,-1])
			img2=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[17,-2])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-1],size=[1.5,1.5])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[16,-1.8],size=[1.5,1.5])
		if choice==185:
			img1=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[-17,-3])
			img2=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[17,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,-3],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-3],size=[1,1])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17,-3],size=[1,1])
		if choice==186:
			img1=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[-17,-1])
			img2=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[17,-2])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-1],size=[1,1])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17,-2],size=[1,1])
		if choice==187:
			img1=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[-17,-2])
			img2=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[18,-1])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17.5,-2],size=[1,1])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[18,-1],size=[1,1])
		if choice==188:
			img1=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[-17,-3])
			img2=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[17,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-3],size=[1,1])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[16.5,-3],size=[1,1])
		if choice==189:
			img1=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[-17,-3])
			img2=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[17,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-3],size=[1,1])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17,-3],size=[1,1])
		if choice==190:
			img1=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[-17,-1])
			img2=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[17,-2])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17.5,-1],size=[1,1])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17,-2],size=[1,1])
		if choice==191:
			img1=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[-17,-2])
			img2=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[18,-1])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-18,-1.8],size=[1,1])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[18,-1],size=[1,1])
		if choice==192:
			img1=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[-17,-2.8])
			img2=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[17.5,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-3],size=[1,1])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[16.5,-2.8],size=[1,1])
		txtRecordat1=visual.ImageStim(mywindow, image="Recordatorio3.png", pos=[0,13])
		txtRecordat2=visual.ImageStim(mywindow,image="Right.png", pos=[17,-15.8])
		txtRecordat3=visual.ImageStim(mywindow,image="Left.png", pos=[-17,-15.8])
		txtRecordat1.draw()
		txtRecordat2.draw()
		txtRecordat3.draw()
		img1.draw()
		img2.draw()
		img3.draw()
		img4.draw()
		img5.draw()
		mybaseline.close
		mywindow.update()
		presentation_time = time.time()
#Tiempo que duran los ensayos0
		core.wait(1.5)
		presentation2_time = time.time()
#		mywindow.setColor(color=[255,255,255], colorSpace="rgb255")
#		mywindow.update()
		mywindow.setColor(color=[255,255,255], colorSpace="rgb255")
		txtRecordat1=visual.ImageStim(mywindow, image="Recordatorio3.png", pos=[0,13])
		txtRecordat2=visual.ImageStim(mywindow,image="Right.png", pos=[17,-15.8])
		txtRecordat3=visual.ImageStim(mywindow,image="Left.png", pos=[-17,-15.8])
		txtRecordat1.draw()
		txtRecordat2.draw()
		txtRecordat3.draw()
		mywindow.update()
		userSel=" "
		validkeys=['left', 'right']
		while userSel !='left' and userSel !='right':
			keys=event.getKeys()
			for k in keys:
				if k in validkeys:
					userSel=k
				elif k=='escape': 
					mytestline.Close()
					core.quit()
			core.wait(0.1)
			response_time = time.time() - presentation_time
			response_timeB = time.time() - presentation2_time
		isASAN=(choice in AS_AN)
		if isASAN: 
			Comparacion='1 AS-AN'
		isBSBN=(choice in BS_BN)
		if isBSBN: 
			Comparacion='3 BS-BN'
		isASBN=(choice in AS_BN)
		if isASBN: 
			Comparacion='2 AS-BN'
		isBSAN=(choice in BS_AN)
		if isBSAN: 
			Comparacion='4 BS-AN'
		isASBS=(choice in AS_BS)
		if isASBS: 
			Comparacion='5 AS-BS'
			PosSenal='Both'
		isANBN=(choice in AN_BN)
		if isANBN: 
			Comparacion='6 AN-BN'
			PosSenal='None'
		isCorrect=(choice in signalright and userSel =='right') or (choice in signalleft and userSel =='left')
		if isCorrect: 
			Correcto=1
			rightcounterb=rightcounterb+1
			PrefPred=1
		isWrong=(choice in signalright and userSel =='left') or (choice in signalleft and userSel =='right')
		if isWrong:
			 wrongcounterb=wrongcounterb+1
			 Correcto=0
			 PrefPred=0
		isAS=(choice in signalright and choice in AS_AN and userSel =='right') or (choice in signalright and choice in AS_BN and userSel =='right') or (choice in signalleft and choice in AS_AN and userSel =='left') or (choice in signalleft and choice in AS_BN and userSel =='left') or (choice in AS_BS and choice not in Null_ASright and userSel =='left') or (choice in AS_BS and choice in Null_ASright and userSel =='right')
		if isAS: 
			Eleccion='AS'
		isAN=(choice in signalright and choice in AS_AN and userSel =='left') or (choice in signalleft and choice in AS_AN and userSel =='right') or (choice in signalright and choice in BS_AN and userSel =='left') or (choice in signalleft and choice in BS_AN and userSel =='right') or (choice in AN_BN and choice not in Null_ANright and userSel =='left') or (choice in AN_BN and choice in Null_ANright and userSel =='right')
		if isAN: 
			Eleccion='AN'
		isBS=(choice in signalright and choice in BS_AN and userSel =='right') or (choice in signalright and choice in BS_BN and userSel =='right') or (choice in signalleft and choice in BS_AN and userSel =='left') or (choice in signalleft and choice in BS_BN and userSel =='left') or (choice in AS_BS and choice not in Null_ASright and userSel =='right') or (choice in AS_BS and choice in Null_ASright and userSel =='left')
		if isBS: 
			Eleccion='BS'
		isBN=(choice in signalright and choice in BS_BN and userSel =='left') or (choice in signalleft and choice in BS_BN and userSel =='right') or (choice in signalleft and choice in AS_BN and userSel =='right') or (choice in signalright and choice in AS_BN and userSel =='left') or (choice in AN_BN and choice not in Null_ANright and userSel =='right') or (choice in AN_BN and choice in Null_ANright and userSel =='left')
		if isBN: 
			Eleccion='BN'
		isNULLConsistent=(choice in AS_BS and choice not in Null_ASright and userSel =='left') or (choice in AS_BS and choice in Null_ANright and userSel =='right') or (choice in AN_BN and choice not in Null_ANright and userSel =='right') or (choice in AN_BN and choice in Null_ANright and userSel =='left')
		if isNULLConsistent:
			PrefPred=1
		isNULLInconsistent=(choice in AS_BS and choice not in Null_ASright and userSel =='right') or (choice in AS_BS and choice in Null_ANright and userSel =='left') or (choice in AN_BN and choice not in Null_ANright and userSel =='left') or (choice in AN_BN and choice in Null_ANright and userSel =='right')
		if isNULLInconsistent:
			PrefPred=0
		isSignalright=(choice in signalright)
		if isSignalright:
			PosSenal='Right'
		isSignalleft=(choice in signalleft)
		if isSignalleft: 
			PosSenal='Left'
		isNoRightAnswer=(choice in AN_BN or choice in AS_BS)
		if isNoRightAnswer: 
			Correcto='NA'
			Hit='NA'
			Rechazo='NA'
			FalseAlarm='NA'
			Miss='NA'
		isHit_and_Rejection=(choice in signalright and userSel =='right') or (choice in signalleft and userSel =='left')
		if isHit_and_Rejection: 
			hitB=hitB+1
			Hit=1
			rejectionB=rejectionB+1
			Rechazo=1
			FalseAlarm=0
			Miss=0
		isFalseAlarm_and_Miss=(choice in signalright and userSel =='left') or (choice in signalleft and userSel =='right')
		if isFalseAlarm_and_Miss: 
			falsealarmB=falsealarmB+1
			FalseAlarm=1
			missB=missB+1
			Miss=1
			Hit=0
			Rechazo=0
		mybaseline.write(str(i)+","+str(choice)+","+str(Comparacion)+","+str(PosSenal)+','+str(userSel)+","+str(Eleccion)+','+str(Correcto)+","+str(PrefPred)+','+str(rightcounterb)+","+str(wrongcounterb)+","+str(response_time)+","+str(response_timeB)+','+str(Hit)+","+str(hitB)+","+str(Rechazo)+","+str(rejectionB)+","+str(FalseAlarm)+","+str(falsealarmB)+","+str(Miss)+","+str(missB)+"\n")
		mywindow.setColor(color=[255,255,255], colorSpace="rgb255")
		mywindow.update()
		mywindow.setColor(color=[255,255,255], colorSpace="rgb255")
		mywindow.update()
		txtResults=visual.TextStim(mywindow,text="\n"+"\n"+"\n"+"\n"+"Presiona la barra espaciadora para avanzar al siguiente ensayo.",wrapWidth = 45,color=[0,0,0], colorSpace="rgb255",alignHoriz="center")
		txtResults.draw()
		mywindow.update()
		while 'space' not in event.getKeys(): 
			core.wait(0.1)
#		mybaseline.write(str(i)+","+str(choice)+","+str(userSel)+","+str(isCorrect)+","+str(rightcounterb)+","+str(wrongcounterb)+","+str(isHit)+","+str(hitB)+","+str(isRejection)+","+str(rejectionB)+","+str(isFalseAlarm)+","+str(falsealarmB)+","+str(isMiss)+","+str(missB)+","+"\n")
#		mywindow.setColor(color=[255,255,255], colorSpace="rgb255")
#		mywindow.update()
#		mywindow.setColor(color=[255,255,255], colorSpace="rgb255")
#		mywindow.update()
#		core.wait(0.5)
#		reglita=visual.ImageStim(mywindow, image="Reglita.png", pos=[0,0])
#		reglita.draw()
#		txtRegla=visual.ImageStim(mywindow, image="Recordatorio2.png", pos=[0,8])
#		txtRegla.draw()
#		mywindow.update()
#		reglita_time = time.time()
#Tiempo que dura la Reglita 
#		core.wait(.5)
#		mywindow.setColor(color=[255,255,255], colorSpace="rgb255")
#		mywindow.update()
#		mywindow.setColor(color=[255,255,255], colorSpace="rgb255")
#		mywindow.update()
#		userSel=" "
#		validkeys=['1', '2', '3']
#		while userSel !='1' and userSel !='2' and userSel !='3':
#			keys=event.getKeys()
#			for k in keys:
#				if k in validkeys:
#					userSel=k
#				elif k=='escape': 
#					mytestline.Close()
#					core.quit()
#			core.wait(0.1)
#			response_time2 = time.time() - reglita_time
#		isHighOld=(isFalseAlarm and userSel =='3') or (isHit and userSel =='3')
#		if isHighOld: 
#			Confidence=6 
#		isHighNew=(isRejection and userSel =='3') or (isMiss and userSel =='3')
#		if isHighNew: 
#			Confidence=1
#		isMediumOld=(isFalseAlarm and userSel =='2') or (isHit and userSel =='2')
#		if isMediumOld: 
#			Confidence=5
#		isMediumNew=(isRejection and userSel =='2') or (isMiss and userSel =='2')
#		if isMediumNew: 
#			Confidence=2
#		isLowOld=(isFalseAlarm and userSel =='1') or (isHit and userSel =='1')
#		if isLowOld: 
#			Confidence=4
#		isLowNew=(isRejection and userSel =='1') or (isMiss and userSel =='1')
#		if isLowNew: 
#			Confidence=3

#END OF ONE TEST
	#END OF A BLOCK OF 48 TESTS
#
#END OF THE FIRST BLOCK
#
TOTAL_time = time.time() - total_time
print str(TOTAL_time)
mybaseline.write(str(TOTAL_time))

mywindow.setColor(color=[255,255,255], colorSpace="rgb255")
mywindow.update()

mywindow.setColor(color=[255,255,255], colorSpace="rgb255")
mywindow.update()
txtResults=visual.TextStim(mywindow,text="Resultado: "+"\n"+"\n"+"Respuesatas Correctas: "+str(rightcounterb)+"\n"+"Respuestas Incorrectas: "+str(wrongcounterb)+"\n"+"\n"+"Presiona la barra espaciadora para continuar",color=[0,0,0], colorSpace="rgb255")
txtResults.draw()
mywindow.update()
while 'space' not in event.getKeys(): 
	core.wait(0.1)



mywindow.setColor(color=[255,255,255], colorSpace="rgb255")
mywindow.update()
mywindow.setColor(color=[255,255,255], colorSpace="rgb255")
mywindow.update()
txtResults=visual.TextStim(mywindow,text="Listo! El experimento ha terminado!"+"\n"+"\n"+"Muchisimas gracias por tu tiempo y cooperacion."+"\n"+"\n"+"Gracias por contribuir al trabajo de una tesista"+"\n"+"\n"+"\n"+"\n"+"Presiona la barra espaciadora para salir",color=[0,0,0], colorSpace="rgb255")
txtResults.draw()
mywindow.update()
while 'space' not in event.getKeys(): 
	core.wait(0.1)

