from psychopy import visual, core, event, gui
import random, time

options={"Experimento":"2a-v2","Descripcion":"Una Figura", "Procedimiento":"Y/N +Rating","Participante":"Usuario1"}
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
while 'space' not in event.getKeys(): 
	core.wait(0.1)
#
#FIRST INSTRUCTIONS
#
mywindow.setColor(color=[255,255,255], colorSpace="rgb255")
mywindow.update()
mywindow.setColor(color=[255,255,255], colorSpace="rgb255")
mywindow.update()
Instrucciones1=visual.ImageStim(mywindow, image="Inst_1.png", pos=[0,0])
Instrucciones1.draw()
#txtResults=visual.TextStim(mywindow,text="Instrucciones:"+"\n"+"\n"+"\n"+"\n"+"En la pantalla se te mostraran dos circulos en color claro cuyo tamano deberas comparar. El circulo del lado izquierdo permanecera aislado, como referencia. El circulo del lado derecho aparecera rodeado de un conjunto de circulos de distinto tamano" +"\n"+"\n"+"\n"+"\n"+"Presiona la tecla S cuando los circulos claros SI sean del mismo tamano. "+"\n"+"\n"+"Presiona la tecla N si NO son iguales"+"\n"+"\n"+"\n"+"\n"+"\n"+"\n"+"Presiona la barra espaciadora para continuar",wrapWidth = 45,color=[0,0,0], colorSpace="rgb255")
#txtResults.draw()
mywindow.update()
while 'space' not in event.getKeys(): 
	core.wait(0.1)

#
#FIRST EXAMPLE
#
mywindow.update()
img2=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[10,-4])
img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-14.2,-4], size=[2.5,2.5])
img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[9.5,-4.2], size=[2,2])
txtResults=visual.TextStim(mywindow,text="Por ejemplo: "+"\n"+"\n"+"\n"+"\n"+"En este caso el circulo claro de la figura derecha (el circulo central) es mas chico que el circulo aislado del lado izquierdo."+"\n"+"\n"+"Deberias presionar la tecla N porque NO son iguales",wrapWidth = 45,pos=[0,12], color=[0,0,0], colorSpace="rgb255")
txtRes=visual.TextStim(mywindow,text="Presiona N",wrapWidth = 30,pos=[0,-17], color=[0,0,0], colorSpace="rgb255")
img2.draw()
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

#INSTRUCCIONES  (2DA PARTE)
#Respecto de la REGLITA
mywindow.update()
imgx=visual.ImageStim(mywindow, image="Reglita.png", pos=[0,1.5])
txtResults=visual.TextStim(mywindow,text="Posteriormente, se te presentara una escala como la siguiente: ",wrapWidth = 45,pos=[0,8], color=[0,0,0], colorSpace="rgb255")
txtRes=visual.TextStim(mywindow,text="Deberas teclear el numero 1, 2 o el 3, dependiendo de que tan seguro estas de tu respuesta."+"\n"+"\n"+"\n"+"\n"+"Presiona la barra espaciadora para continuar",wrapWidth = 30,pos=[0,-7], color=[0,0,0], colorSpace="rgb255")
imgx.draw()
txtResults.draw()
txtRes.draw()
mywindow.update()
while 'space' not in event.getKeys(): 
	core.wait(0.1)
mywindow.update()
#
#END OF FIRST EXAMPLE
#

mywindow.setColor(color=[255,255,255], colorSpace="rgb255")
mywindow.update()
mywindow.setColor(color=[255,255,255], colorSpace="rgb255")
mywindow.update()
Instrucciones2=Visual.ImageStim(mywindow, image="Inst_2.png", pos=[0,0])
#txtResults=visual.TextStim(mywindow,text="Cada pareja a comparar se te mostrara SOLO POR 1 segundo"+"\n"+"\n"+"\n"+"\n"+"NO avanzaras al siguiente ensayo hasta que registres tu respuesta."+"\n"+"\n"+"\n"+"\n"+"Los ensayos estan separados por una breve pantalla blanca, espera a que aparezca una nueva pareja para volver a responder."+"\n"+"\n"+"\n"+"\n"+"Los estimulos se te presentaran en varios colores para facilitar la distincion entre ensayos. Los colores NO ESTAN CORRELACIONADOS de ninguna forma con nada."+"\n"+"\n"+"\n"+"\n"+"Presiona la barra espaciadora para continuar",wrapWidth = 45,color=[0,0,0], colorSpace="rgb255")
#txtResults.draw()
Instrucciones2.draw()
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
#
#END OF INSTRUCTIONS
#


#
#VARIABLE INITIALIZATION
#
mybaseline=open("MirrorEx2a-v2"+"_"+options["Participante"]+"_"+time.strftime("%Y-%m-%d")+"_"+"Y_N+R.csv", 'w')
right=[81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 453, 454, 455, 456, 457, 458, 459, 460, 461, 462, 463, 464, 465, 466, 467, 468, 469, 470, 471, 472, 473, 474, 475, 476, 477, 478, 479, 480, 481, 482, 483, 484, 485, 486, 487, 488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 537, 538, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560]
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
mybaseline.write("Ensayo, Estimulo, Respuesta, Correcto, Aciertos, Errores, Hits, ContadorH, Rechazos, ContadorR, Falsas alarmas, ContadorF, Omisiones, ContadorM, \n")
mywindow.update()

#
#BEGIN OF FIRST BLOCK
#
for j in range(1):
	central = list()
	for i in range (480):
		central.append (i+1)
	for i in range (480):
#		choice=779
		choice=central.pop(random.randint(0,len(central)-1))
# 676 Restando un centimetro a -15 para ajustar distancias
		if choice==1:
			img2=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2,2])
		if choice==2:
			img2=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2,2])
		if choice==3:
			img2=visual.ImageStim(mywindow, image="cext_over2_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[2,2])
		if choice==4:
			img2=visual.ImageStim(mywindow, image="cext_over2_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[2,2])
		if choice==5:
			img2=visual.ImageStim(mywindow, image="cext_over2_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[2,2])
		if choice==6:
			img2=visual.ImageStim(mywindow, image="cext_over2_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[2,2])
		if choice==7:
			img2=visual.ImageStim(mywindow, image="cext_over2_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[2,2])
		if choice==8:
			img2=visual.ImageStim(mywindow, image="cext_over2_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[2,2])
		if choice==9:
			img2=visual.ImageStim(mywindow, image="cext_over2_gui.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[10,0],size=[2,2])
		if choice==10:
			img2=visual.ImageStim(mywindow, image="cext_over2_gui.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[10,0],size=[2,2])
		if choice==11:
			img2=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2,2])
		if choice==12:
			img2=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2,2])
		if choice==13:
			img2=visual.ImageStim(mywindow, image="cext_over2_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[2,2])
		if choice==14:
			img2=visual.ImageStim(mywindow, image="cext_over2_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[2,2])
		if choice==15:
			img2=visual.ImageStim(mywindow, image="cext_over2_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[2,2])
		if choice==16:
			img2=visual.ImageStim(mywindow, image="cext_over2_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[2,2])
		if choice==17:
			img2=visual.ImageStim(mywindow, image="cext_over2_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[2,2])
		if choice==18:
			img2=visual.ImageStim(mywindow, image="cext_over2_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[2,2])
		if choice==19:
			img2=visual.ImageStim(mywindow, image="cext_over2_gui.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[10,0],size=[2,2])
		if choice==20:
			img2=visual.ImageStim(mywindow, image="cext_over2_gui.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[10,0],size=[2,2])
		if choice==21:
			img2=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2,2])
		if choice==22:
			img2=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2,2])
		if choice==23:
			img2=visual.ImageStim(mywindow, image="cext_over2_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[2,2])
		if choice==24:
			img2=visual.ImageStim(mywindow, image="cext_over2_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[2,2])
		if choice==25:
			img2=visual.ImageStim(mywindow, image="cext_over2_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[2,2])
		if choice==26:
			img2=visual.ImageStim(mywindow, image="cext_over2_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[2,2])
		if choice==27:
			img2=visual.ImageStim(mywindow, image="cext_over2_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[2,2])
		if choice==28:
			img2=visual.ImageStim(mywindow, image="cext_over2_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[2,2])
		if choice==29:
			img2=visual.ImageStim(mywindow, image="cext_over2_gui.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[10,0],size=[2,2])
		if choice==30:
			img2=visual.ImageStim(mywindow, image="cext_over2_gui.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[10,0],size=[2,2])
		if choice==31:
			img2=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[9.5,0],size=[2,2])
		if choice==32:
			img2=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[9.5,0],size=[2,2])
		if choice==33:
			img2=visual.ImageStim(mywindow, image="cext_over3_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[9.5,0],size=[2,2])
		if choice==34:
			img2=visual.ImageStim(mywindow, image="cext_over3_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[9.5,0],size=[2,2])
		if choice==35:
			img2=visual.ImageStim(mywindow, image="cext_over3_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[9.5,0],size=[2,2])
		if choice==36:
			img2=visual.ImageStim(mywindow, image="cext_over3_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[9.5,0],size=[2,2])
		if choice==37:
			img2=visual.ImageStim(mywindow, image="cext_over3_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[9.5,0],size=[2,2])
		if choice==38:
			img2=visual.ImageStim(mywindow, image="cext_over3_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[9.5,0],size=[2,2])
		if choice==39:
			img2=visual.ImageStim(mywindow, image="cext_over3_gui.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[9.5,0],size=[2,2])
		if choice==40:
			img2=visual.ImageStim(mywindow, image="cext_over3_gui.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[9.5,0],size=[2,2])
		if choice==41:
			img2=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[9.5,0],size=[2,2])
		if choice==42:
			img2=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[9.5,0],size=[2,2])
		if choice==43:
			img2=visual.ImageStim(mywindow, image="cext_over3_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[9.5,0],size=[2,2])
		if choice==44:
			img2=visual.ImageStim(mywindow, image="cext_over3_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[9.5,0],size=[2,2])
		if choice==45:
			img2=visual.ImageStim(mywindow, image="cext_over3_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[9.5,0],size=[2,2])
		if choice==46:
			img2=visual.ImageStim(mywindow, image="cext_over3_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[9.5,0],size=[2,2])
		if choice==47:
			img2=visual.ImageStim(mywindow, image="cext_over3_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[9.5,0],size=[2,2])
		if choice==48:
			img2=visual.ImageStim(mywindow, image="cext_over3_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[9.5,0],size=[2,2])
		if choice==49:
			img2=visual.ImageStim(mywindow, image="cext_over3_gui.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[9.5,0],size=[2,2])
		if choice==50:
			img2=visual.ImageStim(mywindow, image="cext_over3_gui.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[9.5,0],size=[2,2])
		if choice==51:
			img2=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[9.5,0],size=[2,2])
		if choice==52:
			img2=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[9.5,0],size=[2,2])
		if choice==53:
			img2=visual.ImageStim(mywindow, image="cext_over3_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[9.5,0],size=[2,2])
		if choice==54:
			img2=visual.ImageStim(mywindow, image="cext_over3_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[9.5,0],size=[2,2])
		if choice==55:
			img2=visual.ImageStim(mywindow, image="cext_over3_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[9.5,0],size=[2,2])
		if choice==56:
			img2=visual.ImageStim(mywindow, image="cext_over3_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[9.5,0],size=[2,2])
		if choice==57:
			img2=visual.ImageStim(mywindow, image="cext_over3_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[9.5,0],size=[2,2])
		if choice==58:
			img2=visual.ImageStim(mywindow, image="cext_over3_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[9.5,0],size=[2,2])
		if choice==59:
			img2=visual.ImageStim(mywindow, image="cext_over3_gui.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[9.5,0],size=[2,2])
		if choice==60:
			img2=visual.ImageStim(mywindow, image="cext_over3_gui.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[9.5,0],size=[2,2])
		if choice==61:
			img2=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2,2])
		if choice==62:
			img2=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2,2])
		if choice==63:
			img2=visual.ImageStim(mywindow, image="cext_under2_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[2,2])
		if choice==64:
			img2=visual.ImageStim(mywindow, image="cext_under2_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[2,2])
		if choice==65:
			img2=visual.ImageStim(mywindow, image="cext_under2_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[2,2])
		if choice==66:
			img2=visual.ImageStim(mywindow, image="cext_under2_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[2,2])
		if choice==67:
			img2=visual.ImageStim(mywindow, image="cext_under2_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[2,2])
		if choice==68:
			img2=visual.ImageStim(mywindow, image="cext_under2_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[2,2])
		if choice==69:
			img2=visual.ImageStim(mywindow, image="cext_under2_gui.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[10,0],size=[2,2])
		if choice==70:
			img2=visual.ImageStim(mywindow, image="cext_under2_gui.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[10,0],size=[2,2])
		if choice==71:
			img2=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2,2])
		if choice==72:
			img2=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2,2])
		if choice==73:
			img2=visual.ImageStim(mywindow, image="cext_under2_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[2,2])
		if choice==74:
			img2=visual.ImageStim(mywindow, image="cext_under2_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[2,2])
		if choice==75:
			img2=visual.ImageStim(mywindow, image="cext_under2_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[2,2])
		if choice==76:
			img2=visual.ImageStim(mywindow, image="cext_under2_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[2,2])
		if choice==77:
			img2=visual.ImageStim(mywindow, image="cext_under2_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[2,2])
		if choice==78:
			img2=visual.ImageStim(mywindow, image="cext_under2_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[2,2])
		if choice==79:
			img2=visual.ImageStim(mywindow, image="cext_under2_gui.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[10,0],size=[2,2])
		if choice==80:
			img2=visual.ImageStim(mywindow, image="cext_under2_gui.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[10,0],size=[2,2])
		if choice==81:
			img2=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2,2])
		if choice==82:
			img2=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2,2])
		if choice==83:
			img2=visual.ImageStim(mywindow, image="cext_under2_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[2,2])
		if choice==84:
			img2=visual.ImageStim(mywindow, image="cext_under2_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[2,2])
		if choice==85:
			img2=visual.ImageStim(mywindow, image="cext_under2_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[2,2])
		if choice==86:
			img2=visual.ImageStim(mywindow, image="cext_under2_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[2,2])
		if choice==87:
			img2=visual.ImageStim(mywindow, image="cext_under2_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[2,2])
		if choice==88:
			img2=visual.ImageStim(mywindow, image="cext_under2_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[2,2])
		if choice==89:
			img2=visual.ImageStim(mywindow, image="cext_under2_gui.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[10,0],size=[2,2])
		if choice==90:
			img2=visual.ImageStim(mywindow, image="cext_under2_gui.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[10,0],size=[2,2])
		if choice==91:
			img2=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[9,0],size=[2,2])
		if choice==92:
			img2=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[9,0],size=[2,2])
		if choice==93:
			img2=visual.ImageStim(mywindow, image="cext_under3_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[9,0],size=[2,2])
		if choice==94:
			img2=visual.ImageStim(mywindow, image="cext_under3_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[9,0],size=[2,2])
		if choice==95:
			img2=visual.ImageStim(mywindow, image="cext_under3_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[9,0],size=[2,2])
		if choice==96:
			img2=visual.ImageStim(mywindow, image="cext_under3_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[9,0],size=[2,2])
		if choice==97:
			img2=visual.ImageStim(mywindow, image="cext_under3_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[9,0],size=[2,2])
		if choice==98:
			img2=visual.ImageStim(mywindow, image="cext_under3_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[9,0],size=[2,2])
		if choice==99:
			img2=visual.ImageStim(mywindow, image="cext_under3_gui.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[9,0],size=[2,2])
		if choice==100:
			img2=visual.ImageStim(mywindow, image="cext_under3_gui.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[9,0],size=[2,2])
		if choice==101:
			img2=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[9,0],size=[2,2])
		if choice==102:
			img2=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[9,0],size=[2,2])
		if choice==103:
			img2=visual.ImageStim(mywindow, image="cext_under3_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[9,0],size=[2,2])
		if choice==104:
			img2=visual.ImageStim(mywindow, image="cext_under3_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[9,0],size=[2,2])
		if choice==105:
			img2=visual.ImageStim(mywindow, image="cext_under3_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[9,0],size=[2,2])
		if choice==106:
			img2=visual.ImageStim(mywindow, image="cext_under3_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[9,0],size=[2,2])
		if choice==107:
			img2=visual.ImageStim(mywindow, image="cext_under3_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[9,0],size=[2,2])
		if choice==108:
			img2=visual.ImageStim(mywindow, image="cext_under3_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[9,0],size=[2,2])
		if choice==109:
			img2=visual.ImageStim(mywindow, image="cext_under3_gui.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[9,0],size=[2,2])
		if choice==110:
			img2=visual.ImageStim(mywindow, image="cext_under3_gui.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[9,0],size=[2,2])
		if choice==111:
			img2=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[9,0],size=[2,2])
		if choice==112:
			img2=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[9,0],size=[2,2])
		if choice==113:
			img2=visual.ImageStim(mywindow, image="cext_under3_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[9,0],size=[2,2])
		if choice==114:
			img2=visual.ImageStim(mywindow, image="cext_under3_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[9,0],size=[2,2])
		if choice==115:
			img2=visual.ImageStim(mywindow, image="cext_under3_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[9,0],size=[2,2])
		if choice==116:
			img2=visual.ImageStim(mywindow, image="cext_under3_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[9,0],size=[2,2])
		if choice==117:
			img2=visual.ImageStim(mywindow, image="cext_under3_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[9,0],size=[2,2])
		if choice==118:
			img2=visual.ImageStim(mywindow, image="cext_under3_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[9,0],size=[2,2])
		if choice==119:
			img2=visual.ImageStim(mywindow, image="cext_under3_gui.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[9,0],size=[2,2])
		if choice==120:
			img2=visual.ImageStim(mywindow, image="cext_under3_gui.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[9,0],size=[2,2])
		if choice==121:
			img2=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[3,3])
		if choice==122:
			img2=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[3,3])
		if choice==123:
			img2=visual.ImageStim(mywindow, image="cext_under2_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[3,3])
		if choice==124:
			img2=visual.ImageStim(mywindow, image="cext_under2_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[3,3])
		if choice==125:
			img2=visual.ImageStim(mywindow, image="cext_under2_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[3,3])
		if choice==126:
			img2=visual.ImageStim(mywindow, image="cext_under2_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[3,3])
		if choice==127:
			img2=visual.ImageStim(mywindow, image="cext_under2_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[3,3])
		if choice==128:
			img2=visual.ImageStim(mywindow, image="cext_under2_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[3,3])
		if choice==129:
			img2=visual.ImageStim(mywindow, image="cext_under2_gui.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[10,0],size=[3,3])
		if choice==130:
			img2=visual.ImageStim(mywindow, image="cext_under2_gui.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[10,0],size=[3,3])
		if choice==131:
			img2=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[9,0],size=[3,3])
		if choice==132:
			img2=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[9,0],size=[3,3])
		if choice==133:
			img2=visual.ImageStim(mywindow, image="cext_under3_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[9,0],size=[3,3])
		if choice==134:
			img2=visual.ImageStim(mywindow, image="cext_under3_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[9,0],size=[3,3])
		if choice==135:
			img2=visual.ImageStim(mywindow, image="cext_under3_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[9,0],size=[3,3])
		if choice==136:
			img2=visual.ImageStim(mywindow, image="cext_under3_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[9,0],size=[3,3])
		if choice==137:
			img2=visual.ImageStim(mywindow, image="cext_under3_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[9,0],size=[3,3])
		if choice==138:
			img2=visual.ImageStim(mywindow, image="cext_under3_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[9,0],size=[3,3])
		if choice==139:
			img2=visual.ImageStim(mywindow, image="cext_under3_gui.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[9,0],size=[3,3])
		if choice==140:
			img2=visual.ImageStim(mywindow, image="cext_under3_gui.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[9,0],size=[3,3])
		if choice==141:
			img2=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2.66,2.66])
		if choice==142:
			img2=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2.66,2.66])
		if choice==143:
			img2=visual.ImageStim(mywindow, image="cext_under2_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[2.66,2.66])
		if choice==144:
			img2=visual.ImageStim(mywindow, image="cext_under2_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[2.66,2.66])
		if choice==145:
			img2=visual.ImageStim(mywindow, image="cext_under2_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[2.66,2.66])
		if choice==146:
			img2=visual.ImageStim(mywindow, image="cext_under2_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[2.66,2.66])
		if choice==147:
			img2=visual.ImageStim(mywindow, image="cext_under2_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[2.66,2.66])
		if choice==148:
			img2=visual.ImageStim(mywindow, image="cext_under2_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[2.66,2.66])
		if choice==149:
			img2=visual.ImageStim(mywindow, image="cext_under2_gui.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[10,0],size=[2.66,2.66])
		if choice==150:
			img2=visual.ImageStim(mywindow, image="cext_under2_gui.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[10,0],size=[2.66,2.66])
		if choice==151:
			img2=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[9,0],size=[2.66,2.66])
		if choice==152:
			img2=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[9,0],size=[2.66,2.66])
		if choice==153:
			img2=visual.ImageStim(mywindow, image="cext_under3_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[9,0],size=[2.66,2.66])
		if choice==154:
			img2=visual.ImageStim(mywindow, image="cext_under3_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[9,0],size=[2.66,2.66])
		if choice==155:
			img2=visual.ImageStim(mywindow, image="cext_under3_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[9,0],size=[2.66,2.66])
		if choice==156:
			img2=visual.ImageStim(mywindow, image="cext_under3_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[9,0],size=[2.66,2.66])
		if choice==157:
			img2=visual.ImageStim(mywindow, image="cext_under3_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[9,0],size=[2.66,2.66])
		if choice==158:
			img2=visual.ImageStim(mywindow, image="cext_under3_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[9,0],size=[2.66,2.66])
		if choice==159:
			img2=visual.ImageStim(mywindow, image="cext_under3_gui.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[9,0],size=[2.66,2.66])
		if choice==160:
			img2=visual.ImageStim(mywindow, image="cext_under3_gui.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[9,0],size=[2.66,2.66])
		if choice==161:
			img2=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2.33,2.33])
		if choice==162:
			img2=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2.33,2.33])
		if choice==163:
			img2=visual.ImageStim(mywindow, image="cext_under2_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[2.33,2.33])
		if choice==164:
			img2=visual.ImageStim(mywindow, image="cext_under2_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[2.33,2.33])
		if choice==165:
			img2=visual.ImageStim(mywindow, image="cext_under2_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[2.33,2.33])
		if choice==166:
			img2=visual.ImageStim(mywindow, image="cext_under2_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[2.33,2.33])
		if choice==167:
			img2=visual.ImageStim(mywindow, image="cext_under2_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[2.33,2.33])
		if choice==168:
			img2=visual.ImageStim(mywindow, image="cext_under2_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[2.33,2.33])
		if choice==169:
			img2=visual.ImageStim(mywindow, image="cext_under2_gui.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[10,0],size=[2.33,2.33])
		if choice==170:
			img2=visual.ImageStim(mywindow, image="cext_under2_gui.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[10,0],size=[2.33,2.33])
		if choice==171:
			img2=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[9,0],size=[2.33,2.33])
		if choice==172:
			img2=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[9,0],size=[2.33,2.33])
		if choice==173:
			img2=visual.ImageStim(mywindow, image="cext_under3_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[9,0],size=[2.33,2.33])
		if choice==174:
			img2=visual.ImageStim(mywindow, image="cext_under3_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[9,0],size=[2.33,2.33])
		if choice==175:
			img2=visual.ImageStim(mywindow, image="cext_under3_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[9,0],size=[2.33,2.33])
		if choice==176:
			img2=visual.ImageStim(mywindow, image="cext_under3_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[9,0],size=[2.33,2.33])
		if choice==177:
			img2=visual.ImageStim(mywindow, image="cext_under3_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[9,0],size=[2.33,2.33])
		if choice==178:
			img2=visual.ImageStim(mywindow, image="cext_under3_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[9,0],size=[2.33,2.33])
		if choice==179:
			img2=visual.ImageStim(mywindow, image="cext_under3_gui.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[9,0],size=[2.33,2.33])
		if choice==180:
			img2=visual.ImageStim(mywindow, image="cext_under3_gui.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[9,0],size=[2.33,2.33])
		if choice==181:
			img2=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1.66,1.66])
		if choice==182:
			img2=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1.66,1.66])
		if choice==183:
			img2=visual.ImageStim(mywindow, image="cext_over2_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[1.66,1.66])
		if choice==184:
			img2=visual.ImageStim(mywindow, image="cext_over2_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[1.66,1.66])
		if choice==185:
			img2=visual.ImageStim(mywindow, image="cext_over2_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[1.66,1.66])
		if choice==186:
			img2=visual.ImageStim(mywindow, image="cext_over2_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[1.66,1.66])
		if choice==187:
			img2=visual.ImageStim(mywindow, image="cext_over2_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[1.66,1.66])
		if choice==188:
			img2=visual.ImageStim(mywindow, image="cext_over2_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[1.66,1.66])
		if choice==189:
			img2=visual.ImageStim(mywindow, image="cext_over2_gui.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[10,0],size=[1.66,1.66])
		if choice==190:
			img2=visual.ImageStim(mywindow, image="cext_over2_gui.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[10,0],size=[1.66,1.66])
		if choice==191:
			img2=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[9.5,0],size=[1.66,1.66])
		if choice==192:
			img2=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[9.5,0],size=[1.66,1.66])
		if choice==193:
			img2=visual.ImageStim(mywindow, image="cext_over3_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[9.5,0],size=[1.66,1.66])
		if choice==194:
			img2=visual.ImageStim(mywindow, image="cext_over3_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[9.5,0],size=[1.66,1.66])
		if choice==195:
			img2=visual.ImageStim(mywindow, image="cext_over3_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[9.5,0],size=[1.66,1.66])
		if choice==196:
			img2=visual.ImageStim(mywindow, image="cext_over3_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[9.5,0],size=[1.66,1.66])
		if choice==197:
			img2=visual.ImageStim(mywindow, image="cext_over3_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[9.5,0],size=[1.66,1.66])
		if choice==198:
			img2=visual.ImageStim(mywindow, image="cext_over3_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[9.5,0],size=[1.66,1.66])
		if choice==199:
			img2=visual.ImageStim(mywindow, image="cext_over3_gui.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[9.5,0],size=[1.66,1.66])
		if choice==200:
			img2=visual.ImageStim(mywindow, image="cext_over3_gui.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[9.5,0],size=[1.66,1.66])
		if choice==201:
			img2=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1.33,1.33])
		if choice==202:
			img2=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1.33,1.33])
		if choice==203:
			img2=visual.ImageStim(mywindow, image="cext_over2_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[1.33,1.33])
		if choice==204:
			img2=visual.ImageStim(mywindow, image="cext_over2_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[1.33,1.33])
		if choice==205:
			img2=visual.ImageStim(mywindow, image="cext_over2_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[1.33,1.33])
		if choice==206:
			img2=visual.ImageStim(mywindow, image="cext_over2_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[1.33,1.33])
		if choice==207:
			img2=visual.ImageStim(mywindow, image="cext_over2_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[1.33,1.33])
		if choice==208:
			img2=visual.ImageStim(mywindow, image="cext_over2_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[1.33,1.33])
		if choice==209:
			img2=visual.ImageStim(mywindow, image="cext_over2_gui.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[10,0],size=[1.33,1.33])
		if choice==210:
			img2=visual.ImageStim(mywindow, image="cext_over2_gui.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[10,0],size=[1.33,1.33])
		if choice==211:
			img2=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[9.5,0],size=[1.33,1.33])
		if choice==212:
			img2=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[9.5,0],size=[1.33,1.33])
		if choice==213:
			img2=visual.ImageStim(mywindow, image="cext_over3_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[9.5,0],size=[1.33,1.33])
		if choice==214:
			img2=visual.ImageStim(mywindow, image="cext_over3_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[9.5,0],size=[1.33,1.33])
		if choice==215:
			img2=visual.ImageStim(mywindow, image="cext_over3_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[9.5,0],size=[1.33,1.33])
		if choice==216:
			img2=visual.ImageStim(mywindow, image="cext_over3_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[9.5,0],size=[1.33,1.33])
		if choice==217:
			img2=visual.ImageStim(mywindow, image="cext_over3_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[9.5,0],size=[1.33,1.33])
		if choice==218:
			img2=visual.ImageStim(mywindow, image="cext_over3_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[9.5,0],size=[1.33,1.33])
		if choice==219:
			img2=visual.ImageStim(mywindow, image="cext_over3_gui.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[9.5,0],size=[1.33,1.33])
		if choice==220:
			img2=visual.ImageStim(mywindow, image="cext_over3_gui.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[9.5,0],size=[1.33,1.33])
		if choice==221:
			img2=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1,1])
		if choice==222:
			img2=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1,1])
		if choice==223:
			img2=visual.ImageStim(mywindow, image="cext_over2_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[1,1])
		if choice==224:
			img2=visual.ImageStim(mywindow, image="cext_over2_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[1,1])
		if choice==225:
			img2=visual.ImageStim(mywindow, image="cext_over2_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[1,1])
		if choice==226:
			img2=visual.ImageStim(mywindow, image="cext_over2_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[1,1])
		if choice==227:
			img2=visual.ImageStim(mywindow, image="cext_over2_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[1,1])
		if choice==228:
			img2=visual.ImageStim(mywindow, image="cext_over2_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[1,1])
		if choice==229:
			img2=visual.ImageStim(mywindow, image="cext_over2_gui.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[10,0],size=[1,1])
		if choice==230:
			img2=visual.ImageStim(mywindow, image="cext_over2_gui.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[10,0],size=[1,1])
		if choice==231:
			img2=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[9.5,0],size=[1,1])
		if choice==232:
			img2=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[9.5,0],size=[1,1])
		if choice==233:
			img2=visual.ImageStim(mywindow, image="cext_over3_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[9.5,0],size=[1,1])
		if choice==234:
			img2=visual.ImageStim(mywindow, image="cext_over3_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[9.5,0],size=[1,1])
		if choice==235:
			img2=visual.ImageStim(mywindow, image="cext_over3_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[9.5,0],size=[1,1])
		if choice==236:
			img2=visual.ImageStim(mywindow, image="cext_over3_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[9.5,0],size=[1,1])
		if choice==237:
			img2=visual.ImageStim(mywindow, image="cext_over3_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[9.5,0],size=[1,1])
		if choice==238:
			img2=visual.ImageStim(mywindow, image="cext_over3_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[9.5,0],size=[1,1])
		if choice==239:
			img2=visual.ImageStim(mywindow, image="cext_over3_gui.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[9.5,0],size=[1,1])
		if choice==240:
			img2=visual.ImageStim(mywindow, image="cext_over3_gui.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[9.5,0],size=[1,1])
		if choice==241:
			img2=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2,2])
		if choice==242:
			img2=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2,2])
		if choice==243:
			img2=visual.ImageStim(mywindow, image="cext_over7_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[2,2])
		if choice==244:
			img2=visual.ImageStim(mywindow, image="cext_over7_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[2,2])
		if choice==245:
			img2=visual.ImageStim(mywindow, image="cext_over7_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[2,2])
		if choice==246:
			img2=visual.ImageStim(mywindow, image="cext_over7_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[2,2])
		if choice==247:
			img2=visual.ImageStim(mywindow, image="cext_over7_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[2,2])
		if choice==248:
			img2=visual.ImageStim(mywindow, image="cext_over7_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[2,2])
		if choice==249:
			img2=visual.ImageStim(mywindow, image="cext_over7_gui.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[10,0],size=[2,2])
		if choice==250:
			img2=visual.ImageStim(mywindow, image="cext_over7_gui.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[10,0],size=[2,2])
		if choice==251:
			img2=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2,2])
		if choice==252:
			img2=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2,2])
		if choice==253:
			img2=visual.ImageStim(mywindow, image="cext_over7_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[2,2])
		if choice==254:
			img2=visual.ImageStim(mywindow, image="cext_over7_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[2,2])
		if choice==255:
			img2=visual.ImageStim(mywindow, image="cext_over7_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[2,2])
		if choice==256:
			img2=visual.ImageStim(mywindow, image="cext_over7_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[2,2])
		if choice==257:
			img2=visual.ImageStim(mywindow, image="cext_over7_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[2,2])
		if choice==258:
			img2=visual.ImageStim(mywindow, image="cext_over7_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[2,2])
		if choice==259:
			img2=visual.ImageStim(mywindow, image="cext_over7_gui.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[10,0],size=[2,2])
		if choice==260:
			img2=visual.ImageStim(mywindow, image="cext_over7_gui.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[10,0],size=[2,2])
		if choice==261:
			img2=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2,2])
		if choice==262:
			img2=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2,2])
		if choice==263:
			img2=visual.ImageStim(mywindow, image="cext_over7_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[2,2])
		if choice==264:
			img2=visual.ImageStim(mywindow, image="cext_over7_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[2,2])
		if choice==265:
			img2=visual.ImageStim(mywindow, image="cext_over7_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[2,2])
		if choice==266:
			img2=visual.ImageStim(mywindow, image="cext_over7_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[2,2])
		if choice==267:
			img2=visual.ImageStim(mywindow, image="cext_over7_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[2,2])
		if choice==268:
			img2=visual.ImageStim(mywindow, image="cext_over7_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[2,2])
		if choice==269:
			img2=visual.ImageStim(mywindow, image="cext_over7_gui.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[10,0],size=[2,2])
		if choice==270:
			img2=visual.ImageStim(mywindow, image="cext_over7_gui.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[10,0],size=[2,2])
		if choice==271:
			img2=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2,2])
		if choice==272:
			img2=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2,2])
		if choice==273:
			img2=visual.ImageStim(mywindow, image="cext_over8_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[2,2])
		if choice==274:
			img2=visual.ImageStim(mywindow, image="cext_over8_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[2,2])
		if choice==275:
			img2=visual.ImageStim(mywindow, image="cext_over8_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[2,2])
		if choice==276:
			img2=visual.ImageStim(mywindow, image="cext_over8_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[2,2])
		if choice==277:
			img2=visual.ImageStim(mywindow, image="cext_over8_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[2,2])
		if choice==278:
			img2=visual.ImageStim(mywindow, image="cext_over8_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[2,2])
		if choice==279:
			img2=visual.ImageStim(mywindow, image="cext_over8_gui.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[10,0],size=[2,2])
		if choice==280:
			img2=visual.ImageStim(mywindow, image="cext_over8_gui.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[10,0],size=[2,2])
		if choice==281:
			img2=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2,2])
		if choice==282:
			img2=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2,2])
		if choice==283:
			img2=visual.ImageStim(mywindow, image="cext_over8_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[2,2])
		if choice==284:
			img2=visual.ImageStim(mywindow, image="cext_over8_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[2,2])
		if choice==285:
			img2=visual.ImageStim(mywindow, image="cext_over8_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[2,2])
		if choice==286:
			img2=visual.ImageStim(mywindow, image="cext_over8_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[2,2])
		if choice==287:
			img2=visual.ImageStim(mywindow, image="cext_over8_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[2,2])
		if choice==288:
			img2=visual.ImageStim(mywindow, image="cext_over8_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[2,2])
		if choice==289:
			img2=visual.ImageStim(mywindow, image="cext_over8_gui.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[10,0],size=[2,2])
		if choice==290:
			img2=visual.ImageStim(mywindow, image="cext_over8_gui.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[10,0],size=[2,2])
		if choice==291:
			img2=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2,2])
		if choice==292:
			img2=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2,2])
		if choice==293:
			img2=visual.ImageStim(mywindow, image="cext_over8_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[2,2])
		if choice==294:
			img2=visual.ImageStim(mywindow, image="cext_over8_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[2,2])
		if choice==295:
			img2=visual.ImageStim(mywindow, image="cext_over8_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[2,2])
		if choice==296:
			img2=visual.ImageStim(mywindow, image="cext_over8_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[2,2])
		if choice==297:
			img2=visual.ImageStim(mywindow, image="cext_over8_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[2,2])
		if choice==298:
			img2=visual.ImageStim(mywindow, image="cext_over8_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[2,2])
		if choice==299:
			img2=visual.ImageStim(mywindow, image="cext_over8_gui.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[10,0],size=[2,2])
		if choice==300:
			img2=visual.ImageStim(mywindow, image="cext_over8_gui.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[10,0],size=[2,2])
		if choice==301:
			img2=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[9.5,0],size=[2,2])
		if choice==302:
			img2=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[9.5,0],size=[2,2])
		if choice==303:
			img2=visual.ImageStim(mywindow, image="cext_under7_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[9.5,0],size=[2,2])
		if choice==304:
			img2=visual.ImageStim(mywindow, image="cext_under7_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[9.5,0],size=[2,2])
		if choice==305:
			img2=visual.ImageStim(mywindow, image="cext_under7_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[9.5,0],size=[2,2])
		if choice==306:
			img2=visual.ImageStim(mywindow, image="cext_under7_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[9.5,0],size=[2,2])
		if choice==307:
			img2=visual.ImageStim(mywindow, image="cext_under7_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[9.5,0],size=[2,2])
		if choice==308:
			img2=visual.ImageStim(mywindow, image="cext_under7_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[9.5,0],size=[2,2])
		if choice==309:
			img2=visual.ImageStim(mywindow, image="cext_under7_gui.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[9.5,0],size=[2,2])
		if choice==310:
			img2=visual.ImageStim(mywindow, image="cext_under7_gui.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[9.5,0],size=[2,2])
		if choice==311:
			img2=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[9.5,0],size=[2,2])
		if choice==312:
			img2=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[9.5,0],size=[2,2])
		if choice==313:
			img2=visual.ImageStim(mywindow, image="cext_under7_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[9.5,0],size=[2,2])
		if choice==314:
			img2=visual.ImageStim(mywindow, image="cext_under7_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[9.5,0],size=[2,2])
		if choice==315:
			img2=visual.ImageStim(mywindow, image="cext_under7_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[9.5,0],size=[2,2])
		if choice==316:
			img2=visual.ImageStim(mywindow, image="cext_under7_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[9.5,0],size=[2,2])
		if choice==317:
			img2=visual.ImageStim(mywindow, image="cext_under7_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[9.5,0],size=[2,2])
		if choice==318:
			img2=visual.ImageStim(mywindow, image="cext_under7_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[9.5,0],size=[2,2])
		if choice==319:
			img2=visual.ImageStim(mywindow, image="cext_under7_gui.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[9.5,0],size=[2,2])
		if choice==320:
			img2=visual.ImageStim(mywindow, image="cext_under7_gui.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[9.5,0],size=[2,2])
		if choice==321:
			img2=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[9.5,0],size=[2,2])
		if choice==322:
			img2=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[9.5,0],size=[2,2])
		if choice==323:
			img2=visual.ImageStim(mywindow, image="cext_under7_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[9.5,0],size=[2,2])
		if choice==324:
			img2=visual.ImageStim(mywindow, image="cext_under7_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[9.5,0],size=[2,2])
		if choice==325:
			img2=visual.ImageStim(mywindow, image="cext_under7_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[9.5,0],size=[2,2])
		if choice==326:
			img2=visual.ImageStim(mywindow, image="cext_under7_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[9.5,0],size=[2,2])
		if choice==327:
			img2=visual.ImageStim(mywindow, image="cext_under7_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[9.5,0],size=[2,2])
		if choice==328:
			img2=visual.ImageStim(mywindow, image="cext_under7_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[9.5,0],size=[2,2])
		if choice==329:
			img2=visual.ImageStim(mywindow, image="cext_under7_gui.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[9.5,0],size=[2,2])
		if choice==330:
			img2=visual.ImageStim(mywindow, image="cext_under7_gui.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[9.5,0],size=[2,2])
		if choice==331:
			img2=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2,2])
		if choice==332:
			img2=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2,2])
		if choice==333:
			img2=visual.ImageStim(mywindow, image="cext_under8_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[2,2])
		if choice==334:
			img2=visual.ImageStim(mywindow, image="cext_under8_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[2,2])
		if choice==335:
			img2=visual.ImageStim(mywindow, image="cext_under8_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[2,2])
		if choice==336:
			img2=visual.ImageStim(mywindow, image="cext_under8_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[2,2])
		if choice==337:
			img2=visual.ImageStim(mywindow, image="cext_under8_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[2,2])
		if choice==338:
			img2=visual.ImageStim(mywindow, image="cext_under8_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[2,2])
		if choice==339:
			img2=visual.ImageStim(mywindow, image="cext_under8_gui.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[10,0],size=[2,2])
		if choice==340:
			img2=visual.ImageStim(mywindow, image="cext_under8_gui.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[10,0],size=[2,2])
		if choice==341:
			img2=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2,2])
		if choice==342:
			img2=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2,2])
		if choice==343:
			img2=visual.ImageStim(mywindow, image="cext_under8_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[2,2])
		if choice==344:
			img2=visual.ImageStim(mywindow, image="cext_under8_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[2,2])
		if choice==345:
			img2=visual.ImageStim(mywindow, image="cext_under8_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[2,2])
		if choice==346:
			img2=visual.ImageStim(mywindow, image="cext_under8_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[2,2])
		if choice==347:
			img2=visual.ImageStim(mywindow, image="cext_under8_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[2,2])
		if choice==348:
			img2=visual.ImageStim(mywindow, image="cext_under8_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[2,2])
		if choice==349:
			img2=visual.ImageStim(mywindow, image="cext_under8_gui.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[10,0],size=[2,2])
		if choice==350:
			img2=visual.ImageStim(mywindow, image="cext_under8_gui.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[10,0],size=[2,2])
		if choice==351:
			img2=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2,2])
		if choice==352:
			img2=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2,2])
		if choice==353:
			img2=visual.ImageStim(mywindow, image="cext_under8_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[2,2])
		if choice==354:
			img2=visual.ImageStim(mywindow, image="cext_under8_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[2,2])
		if choice==355:
			img2=visual.ImageStim(mywindow, image="cext_under8_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[2,2])
		if choice==356:
			img2=visual.ImageStim(mywindow, image="cext_under8_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[2,2])
		if choice==357:
			img2=visual.ImageStim(mywindow, image="cext_under8_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[2,2])
		if choice==358:
			img2=visual.ImageStim(mywindow, image="cext_under8_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[2,2])
		if choice==359:
			img2=visual.ImageStim(mywindow, image="cext_under8_gui.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[10,0],size=[2,2])
		if choice==360:
			img2=visual.ImageStim(mywindow, image="cext_under8_gui.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[10,0],size=[2,2])
		if choice==361:
			img2=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[9.5,0],size=[3,3])
		if choice==362:
			img2=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[9.5,0],size=[3,3])
		if choice==363:
			img2=visual.ImageStim(mywindow, image="cext_under7_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[9.5,0],size=[3,3])
		if choice==364:
			img2=visual.ImageStim(mywindow, image="cext_under7_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[9.5,0],size=[3,3])
		if choice==365:
			img2=visual.ImageStim(mywindow, image="cext_under7_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[9.5,0],size=[3,3])
		if choice==366:
			img2=visual.ImageStim(mywindow, image="cext_under7_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[9.5,0],size=[3,3])
		if choice==367:
			img2=visual.ImageStim(mywindow, image="cext_under7_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[9.5,0],size=[3,3])
		if choice==368:
			img2=visual.ImageStim(mywindow, image="cext_under7_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[9.5,0],size=[3,3])
		if choice==369:
			img2=visual.ImageStim(mywindow, image="cext_under7_gui.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[9.5,0],size=[3,3])
		if choice==370:
			img2=visual.ImageStim(mywindow, image="cext_under7_gui.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[9.5,0],size=[3,3])
		if choice==371:
			img2=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[3,3])
		if choice==372:
			img2=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[3,3])
		if choice==373:
			img2=visual.ImageStim(mywindow, image="cext_under8_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[3,3])
		if choice==374:
			img2=visual.ImageStim(mywindow, image="cext_under8_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[3,3])
		if choice==375:
			img2=visual.ImageStim(mywindow, image="cext_under8_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[3,3])
		if choice==376:
			img2=visual.ImageStim(mywindow, image="cext_under8_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[3,3])
		if choice==377:
			img2=visual.ImageStim(mywindow, image="cext_under8_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[3,3])
		if choice==378:
			img2=visual.ImageStim(mywindow, image="cext_under8_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[3,3])
		if choice==379:
			img2=visual.ImageStim(mywindow, image="cext_under8_gui.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[10,0],size=[3,3])
		if choice==380:
			img2=visual.ImageStim(mywindow, image="cext_under8_gui.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[10,0],size=[3,3])
		if choice==381:
			img2=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[9.5,0],size=[2.66,2.66])
		if choice==382:
			img2=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[9.5,0],size=[2.66,2.66])
		if choice==383:
			img2=visual.ImageStim(mywindow, image="cext_under7_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[9.5,0],size=[2.66,2.66])
		if choice==384:
			img2=visual.ImageStim(mywindow, image="cext_under7_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[9.5,0],size=[2.66,2.66])
		if choice==385:
			img2=visual.ImageStim(mywindow, image="cext_under7_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[9.5,0],size=[2.66,2.66])
		if choice==386:
			img2=visual.ImageStim(mywindow, image="cext_under7_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[9.5,0],size=[2.66,2.66])
		if choice==387:
			img2=visual.ImageStim(mywindow, image="cext_under7_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[9.5,0],size=[2.66,2.66])
		if choice==388:
			img2=visual.ImageStim(mywindow, image="cext_under7_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[9.5,0],size=[2.66,2.66])
		if choice==389:
			img2=visual.ImageStim(mywindow, image="cext_under7_gui.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[9.5,0],size=[2.66,2.66])
		if choice==390:
			img2=visual.ImageStim(mywindow, image="cext_under7_gui.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[9.5,0],size=[2.66,2.66])
		if choice==391:
			img2=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2.66,2.66])
		if choice==392:
			img2=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2.66,2.66])
		if choice==393:
			img2=visual.ImageStim(mywindow, image="cext_under8_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[2.66,2.66])
		if choice==394:
			img2=visual.ImageStim(mywindow, image="cext_under8_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[2.66,2.66])
		if choice==395:
			img2=visual.ImageStim(mywindow, image="cext_under8_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[2.66,2.66])
		if choice==396:
			img2=visual.ImageStim(mywindow, image="cext_under8_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[2.66,2.66])
		if choice=397:
			img2=visual.ImageStim(mywindow, image="cext_under8_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[2.66,2.66])
		if choice==398:
			img2=visual.ImageStim(mywindow, image="cext_under8_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[2.66,2.66])
		if choice==399:
			img2=visual.ImageStim(mywindow, image="cext_under8_gui.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[10,0],size=[2.66,2.66])
		if choice==400:
			img2=visual.ImageStim(mywindow, image="cext_under8_gui.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[10,0],size=[2.66,2.66])
		if choice==401:
			img2=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[9.5,0],size=[2.33,2.33])
		if choice==402:
			img2=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[9.5,0],size=[2.33,2.33])
		if choice==403:
			img2=visual.ImageStim(mywindow, image="cext_under7_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[9.5,0],size=[2.33,2.33])
		if choice==404:
			img2=visual.ImageStim(mywindow, image="cext_under7_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[9.5,0],size=[2.33,2.33])
		if choice==405:
			img2=visual.ImageStim(mywindow, image="cext_under7_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[9.5,0],size=[2.33,2.33])
		if choice==406:
			img2=visual.ImageStim(mywindow, image="cext_under7_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[9.5,0],size=[2.33,2.33])
		if choice==407:
			img2=visual.ImageStim(mywindow, image="cext_under7_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[9.5,0],size=[2.33,2.33])
		if choice==408:
			img2=visual.ImageStim(mywindow, image="cext_under7_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[9.5,0],size=[2.33,2.33])
		if choice==409:
			img2=visual.ImageStim(mywindow, image="cext_under7_gui.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[9.5,0],size=[2.33,2.33])
		if choice==410:
			img2=visual.ImageStim(mywindow, image="cext_under7_gui.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[9.5,0],size=[2.33,2.33])
		if choice==411:
			img2=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2.33,2.33])
		if choice==412:
			img2=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2.33,2.33])
		if choice==413:
			img2=visual.ImageStim(mywindow, image="cext_under8_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[2.33,2.33])
		if choice==414:
			img2=visual.ImageStim(mywindow, image="cext_under8_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[2.33,2.33])
		if choice==415:
			img2=visual.ImageStim(mywindow, image="cext_under8_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[2.33,2.33])
		if choice==416:
			img2=visual.ImageStim(mywindow, image="cext_under8_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[2.33,2.33])
		if choice==417:
			img2=visual.ImageStim(mywindow, image="cext_under8_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[2.33,2.33])
		if choice==418:
			img2=visual.ImageStim(mywindow, image="cext_under8_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[2.33,2.33])
		if choice==419:
			img2=visual.ImageStim(mywindow, image="cext_under8_gui.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[10,0],size=[2.33,2.33])
		if choice==420:
			img2=visual.ImageStim(mywindow, image="cext_under8_gui.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[10,0],size=[2.33,2.33])
		if choice==421:
			img2=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1.66,1.66])
		if choice==422:
			img2=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1.66,1.66])
		if choice==423:
			img2=visual.ImageStim(mywindow, image="cext_over7_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[1.66,1.66])
		if choice==424:
			img2=visual.ImageStim(mywindow, image="cext_over7_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[1.66,1.66])
		if choice==425:
			img2=visual.ImageStim(mywindow, image="cext_over7_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[1.66,1.66])
		if choice==426:
			img2=visual.ImageStim(mywindow, image="cext_over7_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[1.66,1.66])
		if choice==427:
			img2=visual.ImageStim(mywindow, image="cext_over7_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[1.66,1.66])
		if choice==428:
			img2=visual.ImageStim(mywindow, image="cext_over7_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[1.66,1.66])
		if choice==429:
			img2=visual.ImageStim(mywindow, image="cext_over7_gui.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[10,0],size=[1.66,1.66])
		if choice==430:
			img2=visual.ImageStim(mywindow, image="cext_over7_gui.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[10,0],size=[1.66,1.66])
		if choice==431:
			img2=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1.66,1.66])
		if choice==432:
			img2=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1.66,1.66])
		if choice==433:
			img2=visual.ImageStim(mywindow, image="cext_over8_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[1.66,1.66])
		if choice==434:
			img2=visual.ImageStim(mywindow, image="cext_over8_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[1.66,1.66])
		if choice==435:
			img2=visual.ImageStim(mywindow, image="cext_over8_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[1.66,1.66])
		if choice==436:
			img2=visual.ImageStim(mywindow, image="cext_over8_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[1.66,1.66])
		if choice==437:
			img2=visual.ImageStim(mywindow, image="cext_over8_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[1.66,1.66])
		if choice==438:
			img2=visual.ImageStim(mywindow, image="cext_over8_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[1.66,1.66])
		if choice==439:
			img2=visual.ImageStim(mywindow, image="cext_over8_gui.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[10,0],size=[1.66,1.66])
		if choice==440:
			img2=visual.ImageStim(mywindow, image="cext_over8_gui.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[10,0],size=[1.66,1.66])
		if choice==441:
			img2=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1.33,1.33])
		if choice==442:
			img2=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1.33,1.33])
		if choice==443:
			img2=visual.ImageStim(mywindow, image="cext_over7_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[1.33,1.33])
		if choice==444:
			img2=visual.ImageStim(mywindow, image="cext_over7_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[1.33,1.33])
		if choice==445:
			img2=visual.ImageStim(mywindow, image="cext_over7_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[1.33,1.33])
		if choice==446:
			img2=visual.ImageStim(mywindow, image="cext_over7_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[1.33,1.33])
		if choice==447:
			img2=visual.ImageStim(mywindow, image="cext_over7_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[1.33,1.33])
		if choice==448:
			img2=visual.ImageStim(mywindow, image="cext_over7_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[1.33,1.33])
		if choice==449:
			img2=visual.ImageStim(mywindow, image="cext_over7_gui.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[10,0],size=[1.33,1.33])
		if choice==450:
			img2=visual.ImageStim(mywindow, image="cext_over7_gui.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[10,0],size=[1.33,1.33])
		if choice==451:
			img2=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1.33,1.33])
		if choice==452:
			img2=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1.33,1.33])
		if choice==453:
			img2=visual.ImageStim(mywindow, image="cext_over8_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[1.33,1.33])
		if choice==454:
			img2=visual.ImageStim(mywindow, image="cext_over8_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[1.33,1.33])
		if choice==455:
			img2=visual.ImageStim(mywindow, image="cext_over8_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[1.33,1.33])
		if choice==456:
			img2=visual.ImageStim(mywindow, image="cext_over8_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[1.33,1.33])
		if choice==457:
			img2=visual.ImageStim(mywindow, image="cext_over8_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[1.33,1.33])
		if choice==458:
			img2=visual.ImageStim(mywindow, image="cext_over8_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[1.33,1.33])
		if choice==459:
			img2=visual.ImageStim(mywindow, image="cext_over8_gui.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[10,0],size=[1.33,1.33])
		if choice==460:
			img2=visual.ImageStim(mywindow, image="cext_over8_gui.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[10,0],size=[1.33,1.33])
		if choice==461:
			img2=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1,1])
		if choice==462:
			img2=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1,1])
		if choice==463:
			img2=visual.ImageStim(mywindow, image="cext_over7_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[1,1])
		if choice==464:
			img2=visual.ImageStim(mywindow, image="cext_over7_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[1,1])
		if choice==465:
			img2=visual.ImageStim(mywindow, image="cext_over7_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[1,1])
		if choice==466:
			img2=visual.ImageStim(mywindow, image="cext_over7_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[1,1])
		if choice==467:
			img2=visual.ImageStim(mywindow, image="cext_over7_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[1,1])
		if choice==468:
			img2=visual.ImageStim(mywindow, image="cext_over7_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[1,1])
		if choice==469:
			img2=visual.ImageStim(mywindow, image="cext_over7_gui.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[10,0],size=[1,1])
		if choice==470:
			img2=visual.ImageStim(mywindow, image="cext_over7_gui.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[10,0],size=[1,1])
		if choice==471:
			img2=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1,1])
		if choice==472:
			img2=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1,1])
		if choice==473:
			img2=visual.ImageStim(mywindow, image="cext_over8_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[1,1])
		if choice==474:
			img2=visual.ImageStim(mywindow, image="cext_over8_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[1,1])
		if choice==475:
			img2=visual.ImageStim(mywindow, image="cext_over8_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[1,1])
		if choice==476:
			img2=visual.ImageStim(mywindow, image="cext_over8_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[1,1])
		if choice==477:
			img2=visual.ImageStim(mywindow, image="cext_over8_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[1,1])
		if choice==478:
			img2=visual.ImageStim(mywindow, image="cext_over8_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[1,1])
		if choice==479:
			img2=visual.ImageStim(mywindow, image="cext_over8_gui.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[10,0],size=[1,1])
		if choice==480:
			img2=visual.ImageStim(mywindow, image="cext_over8_gui.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[-14,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[10,0],size=[1,1])
		txtRecordat1=visual.ImageStim(mywindow, image="Recordatorio1.png", pos=[0,15])
		txtRecordat2=visual.TextStim(mywindow,text="S = Si",wrapWidth = 60,color=[0,0,0], pos=[-9,-14], colorSpace="rgb255")
		txtRecordat3=visual.TextStim(mywindow,text="N = No",wrapWidth = 60,color=[0,0,0], pos=[7,-14], colorSpace="rgb255")
		txtRecordat1.draw()
		txtRecordat2.draw()
		txtRecordat3.draw()
		img2.draw()
		img3.draw()
		img4.draw()
		mybaseline.close
		mywindow.update()
#Tiempo que duran los ensayos0
		core.wait(1.5)
#		mywindow.setColor(color=[255,255,255], colorSpace="rgb255")
#		mywindow.update()
		mywindow.setColor(color=[255,255,255], colorSpace="rgb255")
		txtRecordat1=visual.ImageStim(mywindow, image="Recordatorio1.png", pos=[0,15])
		txtRecordat2=visual.TextStim(mywindow,text="S = Si",wrapWidth = 60,color=[0,0,0], pos=[-9,-14], colorSpace="rgb255")
		txtRecordat3=visual.TextStim(mywindow,text="N = No",wrapWidth = 60,color=[0,0,0], pos=[7,-14], colorSpace="rgb255")
		txtRecordat1.draw()
		txtRecordat2.draw()
		txtRecordat3.draw()
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
#		mywindow.setColor(color=[255,255,255], colorSpace="rgb255")
#		mywindow.update()
#		mywindow.setColor(color=[255,255,255], colorSpace="rgb255")
#		mywindow.update()
#		core.wait(0.5)
		reglita=visual.ImageStim(mywindow, image="Reglita.png", pos=[0,0])
		reglita.draw()
		txtRegla=visual.ImageStim(mywindow, image="Recordatorio2.png", pos=[0,8])
		txtRegla.draw()
		mywindow.update()
#Tiempo que dura la Reglita 
#		core.wait(.5)
#		mywindow.setColor(color=[255,255,255], colorSpace="rgb255")
#		mywindow.update()
#		mywindow.setColor(color=[255,255,255], colorSpace="rgb255")
#		mywindow.update()
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
		txtResults=visual.TextStim(mywindow,text="\n"+"\n"+"\n"+"\n"+"Presiona la barra espaciadora para pasar al siguiente ensayo.",wrapWidth = 45,color=[0,0,0], colorSpace="rgb255",alignHoriz="center")
		txtResults.draw()
		mywindow.update()
		while 'space' not in event.getKeys(): 
			core.wait(0.1)
#END OF ONE TEST
	#END OF A BLOCK OF 48 TESTS
#
#END OF THE FIRST BLOCK
#

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
