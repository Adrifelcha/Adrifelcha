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
img1=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[16,-5])
img2=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[-15,-5])
img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15.2,-5], size=[2.5,2.5])
img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[16,-5.2], size=[2,2])


txtResults=visual.TextStim(mywindow,text="Ejemplo: "+"\n"+"\n"+"En este caso el circulo central de la figura derecha es mas chico que el del lado izquierdo."+"\n"+"\n"+"Deberias presionar la tecla N porque NO son iguales",wrapWidth = 30,pos=[0,12], color=[0,0,0], colorSpace="rgb255")
txtRes=visual.TextStim(mywindow,text="Presiona N",wrapWidth = 30,pos=[0,-17], color=[0,0,0], colorSpace="rgb255")
img1.draw()
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
right=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 453, 454, 455, 456, 457, 458, 459, 460, 461, 462, 463, 464, 465, 466, 467, 468, 469, 470, 471, 472, 473, 474, 475, 476, 477, 478, 479, 480, 481, 482, 483, 484, 485, 486, 487, 488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 537, 538, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586, 587, 588, 589, 590, 591, 592, 593, 594, 595, 596, 597, 598, 599, 600]
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

#txtRecordat1=visual.TextStim(mywindow,text="Los circulos centrales son iguales?",wrapWidth = 45,color=[0,0,0], pos=[0,10], bold="True", colorSpace="rgb255")
#txtRecordat2=visual.TextStim(mywindow,text="S = Si",wrapWidth = 45,color=[0,0,0], pos=[0,-10], bold="True", colorSpace="rgb255")
#txtRecordat3=visual.TextStim(mywindow,text="N = No",wrapWidth = 45,color=[0,0,0], pos=[0,-15], bold="True", colorSpace="rgb255")
#
#BEGIN OF FIRST BLOCK
#
for j in range(1):
	central = list()
	for i in range (800):
		central.append (i+1)
	for i in range (800):
		choice=central.pop(random.randint(0,len(central)-1))
		if choice==1:
			img1=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[3,3])
		if choice==2:
			img1=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[3,3])
		if choice==3:
			img1=visual.ImageStim(mywindow, image="cext_over2_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[3,3])
		if choice==4:
			img1=visual.ImageStim(mywindow, image="cext_under2_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[3,3])
		if choice==5:
			img1=visual.ImageStim(mywindow, image="cext_over2_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[3,3])
		if choice==6:
			img1=visual.ImageStim(mywindow, image="cext_under2_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[3,3])
		if choice==7:
			img1=visual.ImageStim(mywindow, image="cext_over2_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[3,3])
		if choice==8:
			img1=visual.ImageStim(mywindow, image="cext_under2_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[3,3])
		if choice==9:
			img1=visual.ImageStim(mywindow, image="cext_over2_gui.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_gui.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[10,0],size=[3,3])
		if choice==10:
			img1=visual.ImageStim(mywindow, image="cext_under2_gui.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_gui.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[10,0],size=[3,3])
		if choice==11:
			img1=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15.5,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[9.5,0],size=[3,3])
		if choice==12:
			img1=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[9.5,0],size=[3,3])
		if choice==13:
			img1=visual.ImageStim(mywindow, image="cext_over3_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15.5,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[9.5,0],size=[3,3])
		if choice==14:
			img1=visual.ImageStim(mywindow, image="cext_under3_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[9.5,0],size=[3,3])
		if choice==15:
			img1=visual.ImageStim(mywindow, image="cext_over3_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15.5,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[9.5,0],size=[3,3])
		if choice==16:
			img1=visual.ImageStim(mywindow, image="cext_under3_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[9.5,0],size=[3,3])
		if choice==17:
			img1=visual.ImageStim(mywindow, image="cext_over3_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15.5,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[9.5,0],size=[3,3])
		if choice==18:
			img1=visual.ImageStim(mywindow, image="cext_under3_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[9.5,0],size=[3,3])
		if choice==19:
			img1=visual.ImageStim(mywindow, image="cext_over3_gui.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_gui.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[-15.5,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[9.5,0],size=[3,3])
		if choice==20:
			img1=visual.ImageStim(mywindow, image="cext_under3_gui.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_gui.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[-15.5,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_gui.png", pos=[9.5,0],size=[3,3])
		if choice==21:
			img1=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[9.5,0],size=[3,3])
		if choice==22:
			img1=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15.5,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[3,3])
		if choice==23:
			img1=visual.ImageStim(mywindow, image="cext_over2_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[9.5,0],size=[3,3])
		if choice==24:
			img1=visual.ImageStim(mywindow, image="cext_under3_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15.5,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[3,3])
		if choice==25:
			img1=visual.ImageStim(mywindow, image="cext_over2_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[9.5,0],size=[3,3])
		if choice==26:
			img1=visual.ImageStim(mywindow, image="cext_under3_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15.5,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[3,3])
		if choice==27:
			img1=visual.ImageStim(mywindow, image="cext_over2_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[9.5,0],size=[3,3])
		if choice==28:
			img1=visual.ImageStim(mywindow, image="cext_under3_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15.5,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[3,3])
		if choice==29:
			img1=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[9.5,0],size=[3,3])
		if choice==30:
			img1=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15.5,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[3,3])
		if choice==31:
			img1=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15.5,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[3,3])
		if choice==32:
			img1=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[9.5,0],size=[3,3])
		if choice==33:
			img1=visual.ImageStim(mywindow, image="cext_over3_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15.5,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[3,3])
		if choice==34:
			img1=visual.ImageStim(mywindow, image="cext_under2_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[9.5,0],size=[3,3])
		if choice==35:
			img1=visual.ImageStim(mywindow, image="cext_over3_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15.5,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[3,3])
		if choice==36:
			img1=visual.ImageStim(mywindow, image="cext_under2_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[9.5,0],size=[3,3])
		if choice==37:
			img1=visual.ImageStim(mywindow, image="cext_over3_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15.5,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[3,3])
		if choice==38:
			img1=visual.ImageStim(mywindow, image="cext_under2_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[9.5,0],size=[3,3])
		if choice==39:
			img1=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15.5,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[3,3])
		if choice==40:
			img1=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[9.5,0],size=[3,3])
		if choice==41:
			img1=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2.5,2.5])
		if choice==42:
			img1=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2.5,2.5])
		if choice==43:
			img1=visual.ImageStim(mywindow, image="cext_over2_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[2.5,2.5])
		if choice==44:
			img1=visual.ImageStim(mywindow, image="cext_under2_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[2.5,2.5])
		if choice==45:
			img1=visual.ImageStim(mywindow, image="cext_over2_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[2.5,2.5])
		if choice==46:
			img1=visual.ImageStim(mywindow, image="cext_under2_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[2.5,2.5])
		if choice==47:
			img1=visual.ImageStim(mywindow, image="cext_over2_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[2.5,2.5])
		if choice==48:
			img1=visual.ImageStim(mywindow, image="cext_under2_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[2.5,2.5])
		if choice==49:
			img1=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2.5,2.5])
		if choice==50:
			img1=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2.5,2.5])
		if choice==51:
			img1=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15.5,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[9.5,0],size=[2.5,2.5])
		if choice==52:
			img1=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15.5,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[9.5,0],size=[2.5,2.5])
		if choice==53:
			img1=visual.ImageStim(mywindow, image="cext_over3_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15.5,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[9.5,0],size=[2.5,2.5])
		if choice==54:
			img1=visual.ImageStim(mywindow, image="cext_under3_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15.5,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[9.5,0],size=[2.5,2.5])
		if choice==55:
			img1=visual.ImageStim(mywindow, image="cext_over3_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15.5,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[9.5,0],size=[2.5,2.5])
		if choice==56:
			img1=visual.ImageStim(mywindow, image="cext_under3_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15.5,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[9.5,0],size=[2.5,2.5])
		if choice==57:
			img1=visual.ImageStim(mywindow, image="cext_over3_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15.5,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[9.5,0],size=[2.5,2.5])
		if choice==58:
			img1=visual.ImageStim(mywindow, image="cext_under3_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15.5,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[9.5,0],size=[2.5,2.5])
		if choice==59:
			img1=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15.5,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[9.5,0],size=[2.5,2.5])
		if choice==60:
			img1=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15.5,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[9.5,0],size=[2.5,2.5])
		if choice==61:
			img1=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[9.5,0],size=[2.5,2.5])
		if choice==62:
			img1=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15.5,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2.5,2.5])
		if choice==63:
			img1=visual.ImageStim(mywindow, image="cext_over2_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[9.5,0],size=[2.5,2.5])
		if choice==64:
			img1=visual.ImageStim(mywindow, image="cext_under3_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15.5,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[2.5,2.5])
		if choice==65:
			img1=visual.ImageStim(mywindow, image="cext_over2_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[9.5,0],size=[2.5,2.5])
		if choice==66:
			img1=visual.ImageStim(mywindow, image="cext_under3_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15.5,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[2.5,2.5])
		if choice==67:
			img1=visual.ImageStim(mywindow, image="cext_over2_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[9.5,0],size=[2.5,2.5])
		if choice==68:
			img1=visual.ImageStim(mywindow, image="cext_under3_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15.5,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[2.5,2.5])
		if choice==69:
			img1=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[9.5,0],size=[2.5,2.5])
		if choice==70:
			img1=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15.5,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2.5,2.5])
		if choice==71:
			img1=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15.5,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2.5,2.5])
		if choice==72:
			img1=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[9.5,0],size=[2.5,2.5])
		if choice==73:
			img1=visual.ImageStim(mywindow, image="cext_over3_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15.5,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[2.5,2.5])
		if choice==74:
			img1=visual.ImageStim(mywindow, image="cext_under2_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[9.5,0],size=[2.5,2.5])
		if choice==75:
			img1=visual.ImageStim(mywindow, image="cext_over3_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15.5,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[2.5,2.5])
		if choice==76:
			img1=visual.ImageStim(mywindow, image="cext_under2_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[9.5,0],size=[2.5,2.5])
		if choice==77:
			img1=visual.ImageStim(mywindow, image="cext_over3_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15.5,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[2.5,2.5])
		if choice==78:
			img1=visual.ImageStim(mywindow, image="cext_under2_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[9.5,0],size=[2.5,2.5])
		if choice==79:
			img1=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15.5,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2.5,2.5])
		if choice==80:
			img1=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[9.5,0],size=[2.5,2.5])
		if choice==81:
			img1=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2,2])
		if choice==82:
			img1=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2,2])
		if choice==83:
			img1=visual.ImageStim(mywindow, image="cext_over2_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[2,2])
		if choice==84:
			img1=visual.ImageStim(mywindow, image="cext_under2_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[2,2])
		if choice==85:
			img1=visual.ImageStim(mywindow, image="cext_over2_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[2,2])
		if choice==86:
			img1=visual.ImageStim(mywindow, image="cext_under2_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[2,2])
		if choice==87:
			img1=visual.ImageStim(mywindow, image="cext_over2_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[2,2])
		if choice==88:
			img1=visual.ImageStim(mywindow, image="cext_under2_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[2,2])
		if choice==89:
			img1=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2,2])
		if choice==90:
			img1=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2,2])
		if choice==91:
			img1=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15.5,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[9.5,0],size=[2,2])
		if choice==92:
			img1=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15.5,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[9.5,0],size=[2,2])
		if choice==93:
			img1=visual.ImageStim(mywindow, image="cext_over3_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15.5,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[9.5,0],size=[2,2])
		if choice==94:
			img1=visual.ImageStim(mywindow, image="cext_under3_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15.5,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[9.5,0],size=[2,2])
		if choice==95:
			img1=visual.ImageStim(mywindow, image="cext_over3_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15.5,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[9.5,0],size=[2,2])
		if choice==96:
			img1=visual.ImageStim(mywindow, image="cext_under3_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15.5,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[9.5,0],size=[2,2])
		if choice==97:
			img1=visual.ImageStim(mywindow, image="cext_over3_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15.5,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[9.5,0],size=[2,2])
		if choice==98:
			img1=visual.ImageStim(mywindow, image="cext_under3_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15.5,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[9.5,0],size=[2,2])
		if choice==99:
			img1=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15.5,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[9.5,0],size=[2,2])
		if choice==100:
			img1=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15.5,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[9.5,0],size=[2,2])
		if choice==101:
			img1=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[9.5,0],size=[2,2])
		if choice==102:
			img1=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15.5,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2,2])
		if choice==103:
			img1=visual.ImageStim(mywindow, image="cext_over2_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[9.5,0],size=[2,2])
		if choice==104:
			img1=visual.ImageStim(mywindow, image="cext_under3_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15.5,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[2,2])
		if choice==105:
			img1=visual.ImageStim(mywindow, image="cext_over2_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[9.5,0],size=[2,2])
		if choice==106:
			img1=visual.ImageStim(mywindow, image="cext_under3_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15.5,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[2,2])
		if choice==107:
			img1=visual.ImageStim(mywindow, image="cext_over2_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[9.5,0],size=[2,2])
		if choice==108:
			img1=visual.ImageStim(mywindow, image="cext_under3_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15.5,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[2,2])
		if choice==109:
			img1=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[9.5,0],size=[2,2])
		if choice==110:
			img1=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15.5,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2,2])
		if choice==111:
			img1=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15.5,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2,2])
		if choice==112:
			img1=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[9.5,0],size=[2,2])
		if choice==113:
			img1=visual.ImageStim(mywindow, image="cext_over3_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15.5,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[2,2])
		if choice==114:
			img1=visual.ImageStim(mywindow, image="cext_under2_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[9.5,0],size=[2,2])
		if choice==115:
			img1=visual.ImageStim(mywindow, image="cext_over3_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15.5,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[2,2])
		if choice==116:
			img1=visual.ImageStim(mywindow, image="cext_under2_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[9.5,0],size=[2,2])
		if choice==117:
			img1=visual.ImageStim(mywindow, image="cext_over3_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15.5,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[2,2])
		if choice==118:
			img1=visual.ImageStim(mywindow, image="cext_under2_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[9.5,0],size=[2,2])
		if choice==119:
			img1=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15.5,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2,2])
		if choice==120:
			img1=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[9.5,0],size=[2,2])
		if choice==121:
			img1=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1.5,1.5])
		if choice==122:
			img1=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1.5,1.5])
		if choice==123:
			img1=visual.ImageStim(mywindow, image="cext_over2_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[1.5,1.5])
		if choice==124:
			img1=visual.ImageStim(mywindow, image="cext_under2_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[1.5,1.5])
		if choice==125:
			img1=visual.ImageStim(mywindow, image="cext_over2_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[1.5,1.5])
		if choice==126:
			img1=visual.ImageStim(mywindow, image="cext_under2_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[1.5,1.5])
		if choice==127:
			img1=visual.ImageStim(mywindow, image="cext_over2_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[1.5,1.5])
		if choice==128:
			img1=visual.ImageStim(mywindow, image="cext_under2_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[1.5,1.5])
		if choice==129:
			img1=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1.5,1.5])
		if choice==130:
			img1=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1.5,1.5])
		if choice==131:
			img1=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15.5,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[9.5,0],size=[1.5,1.5])
		if choice==132:
			img1=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15.5,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[9.5,0],size=[1.5,1.5])
		if choice==133:
			img1=visual.ImageStim(mywindow, image="cext_over3_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15.5,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[9.5,0],size=[1.5,1.5])
		if choice==134:
			img1=visual.ImageStim(mywindow, image="cext_under3_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15.5,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[9.5,0],size=[1.5,1.5])
		if choice==135:
			img1=visual.ImageStim(mywindow, image="cext_over3_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15.5,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[9.5,0],size=[1.5,1.5])
		if choice==136:
			img1=visual.ImageStim(mywindow, image="cext_under3_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15.5,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[9.5,0],size=[1.5,1.5])
		if choice==137:
			img1=visual.ImageStim(mywindow, image="cext_over3_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15.5,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[9.5,0],size=[1.5,1.5])
		if choice==138:
			img1=visual.ImageStim(mywindow, image="cext_under3_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15.5,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[9.5,0],size=[1.5,1.5])
		if choice==139:
			img1=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15.5,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[9.5,0],size=[1.5,1.5])
		if choice==140:
			img1=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15.5,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[9.5,0],size=[1.5,1.5])
		if choice==141:
			img1=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[9.5,0],size=[1.5,1.5])
		if choice==142:
			img1=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15.5,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1.5,1.5])
		if choice==143:
			img1=visual.ImageStim(mywindow, image="cext_over2_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[9.5,0],size=[1.5,1.5])
		if choice==144:
			img1=visual.ImageStim(mywindow, image="cext_under3_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15.5,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[1.5,1.5])
		if choice==145:
			img1=visual.ImageStim(mywindow, image="cext_over2_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[9.5,0],size=[1.5,1.5])
		if choice==146:
			img1=visual.ImageStim(mywindow, image="cext_under3_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15.5,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[1.5,1.5])
		if choice==147:
			img1=visual.ImageStim(mywindow, image="cext_over2_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[9.5,0],size=[1.5,1.5])
		if choice==148:
			img1=visual.ImageStim(mywindow, image="cext_under3_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15.5,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[1.5,1.5])
		if choice==149:
			img1=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[9.5,0],size=[1.5,1.5])
		if choice==150:
			img1=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15.5,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1.5,1.5])
		if choice==151:
			img1=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15.5,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1.5,1.5])
		if choice==152:
			img1=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[9.5,0],size=[1.5,1.5])
		if choice==153:
			img1=visual.ImageStim(mywindow, image="cext_over3_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15.5,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[1.5,1.5])
		if choice==154:
			img1=visual.ImageStim(mywindow, image="cext_under2_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[9.5,0],size=[1.5,1.5])
		if choice==155:
			img1=visual.ImageStim(mywindow, image="cext_over3_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15.5,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[1.5,1.5])
		if choice==156:
			img1=visual.ImageStim(mywindow, image="cext_under2_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[9.5,0],size=[1.5,1.5])
		if choice==157:
			img1=visual.ImageStim(mywindow, image="cext_over3_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15.5,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[1.5,1.5])
		if choice==158:
			img1=visual.ImageStim(mywindow, image="cext_under2_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[9.5,0],size=[1.5,1.5])
		if choice==159:
			img1=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15.5,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1.5,1.5])
		if choice==160:
			img1=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[9.5,0],size=[1.5,1.5])
		if choice==161:
			img1=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1,1])
		if choice==162:
			img1=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1,1])
		if choice==163:
			img1=visual.ImageStim(mywindow, image="cext_over2_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[1,1])
		if choice==164:
			img1=visual.ImageStim(mywindow, image="cext_under2_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[1,1])
		if choice==165:
			img1=visual.ImageStim(mywindow, image="cext_over2_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[1,1])
		if choice==166:
			img1=visual.ImageStim(mywindow, image="cext_under2_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[1,1])
		if choice==167:
			img1=visual.ImageStim(mywindow, image="cext_over2_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[1,1])
		if choice==168:
			img1=visual.ImageStim(mywindow, image="cext_under2_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[1,1])
		if choice==169:
			img1=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1,1])
		if choice==170:
			img1=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1,1])
		if choice==171:
			img1=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15.5,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[9.5,0],size=[1,1])
		if choice==172:
			img1=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15.5,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[9.5,0],size=[1,1])
		if choice==173:
			img1=visual.ImageStim(mywindow, image="cext_over3_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15.5,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[9.5,0],size=[1,1])
		if choice==174:
			img1=visual.ImageStim(mywindow, image="cext_under3_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15.5,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[9.5,0],size=[1,1])
		if choice==175:
			img1=visual.ImageStim(mywindow, image="cext_over3_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15.5,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[9.5,0],size=[1,1])
		if choice==176:
			img1=visual.ImageStim(mywindow, image="cext_under3_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15.5,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[9.5,0],size=[1,1])
		if choice==177:
			img1=visual.ImageStim(mywindow, image="cext_over3_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15.5,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[9.5,0],size=[1,1])
		if choice==178:
			img1=visual.ImageStim(mywindow, image="cext_under3_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15.5,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[9.5,0],size=[1,1])
		if choice==179:
			img1=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15.5,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[9.5,0],size=[1,1])
		if choice==180:
			img1=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15.5,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[9.5,0],size=[1,1])
		if choice==181:
			img1=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[9.5,0],size=[1,1])
		if choice==182:
			img1=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15.5,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1,1])
		if choice==183:
			img1=visual.ImageStim(mywindow, image="cext_over2_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[9.5,0],size=[1,1])
		if choice==184:
			img1=visual.ImageStim(mywindow, image="cext_under3_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15.5,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[1,1])
		if choice==185:
			img1=visual.ImageStim(mywindow, image="cext_over2_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[9.5,0],size=[1,1])
		if choice==186:
			img1=visual.ImageStim(mywindow, image="cext_under3_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15.5,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[1,1])
		if choice==187:
			img1=visual.ImageStim(mywindow, image="cext_over2_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[9.5,0],size=[1,1])
		if choice==188:
			img1=visual.ImageStim(mywindow, image="cext_under3_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15.5,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[1,1])
		if choice==189:
			img1=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[9.5,0],size=[1,1])
		if choice==190:
			img1=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15.5,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1,1])
		if choice==191:
			img1=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15.5,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1,1])
		if choice==192:
			img1=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[9.5,0],size=[1,1])
		if choice==193:
			img1=visual.ImageStim(mywindow, image="cext_over3_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15.5,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[1,1])
		if choice==194:
			img1=visual.ImageStim(mywindow, image="cext_under2_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[9.5,0],size=[1,1])
		if choice==195:
			img1=visual.ImageStim(mywindow, image="cext_over3_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15.5,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[1,1])
		if choice==196:
			img1=visual.ImageStim(mywindow, image="cext_under2_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[9.5,0],size=[1,1])
		if choice==197:
			img1=visual.ImageStim(mywindow, image="cext_over3_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15.5,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[1,1])
		if choice==198:
			img1=visual.ImageStim(mywindow, image="cext_under2_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[9.5,0],size=[1,1])
		if choice==199:
			img1=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15.5,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1,1])
		if choice==200:
			img1=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[9.5,0],size=[1,1])
		if choice==201:
			img1=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[3,3])
		if choice==202:
			img1=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2.5,2.5])
		if choice==203:
			img1=visual.ImageStim(mywindow, image="cext_over2_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[3,3])
		if choice==204:
			img1=visual.ImageStim(mywindow, image="cext_under2_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[2.5,2.5])
		if choice==205:
			img1=visual.ImageStim(mywindow, image="cext_over2_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[3,3])
		if choice==206:
			img1=visual.ImageStim(mywindow, image="cext_under2_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[2.5,2.5])
		if choice==207:
			img1=visual.ImageStim(mywindow, image="cext_over2_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[3,3])
		if choice==208:
			img1=visual.ImageStim(mywindow, image="cext_under2_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[2.5,2.5])
		if choice==209:
			img1=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[3,3])
		if choice==210:
			img1=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2.5,2.5])
		if choice==211:
			img1=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15.5,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[9.5,0],size=[3,3])
		if choice==212:
			img1=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15.5,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[9.5,0],size=[2.5,2.5])
		if choice==213:
			img1=visual.ImageStim(mywindow, image="cext_over3_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15.5,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[9.5,0],size=[3,3])
		if choice==214:
			img1=visual.ImageStim(mywindow, image="cext_under3_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15.5,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[9.5,0],size=[2.5,2.5])
		if choice==215:
			img1=visual.ImageStim(mywindow, image="cext_over3_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15.5,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[9.5,0],size=[3,3])
		if choice==216:
			img1=visual.ImageStim(mywindow, image="cext_under3_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15.5,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[9.5,0],size=[2.5,2.5])
		if choice==217:
			img1=visual.ImageStim(mywindow, image="cext_over3_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15.5,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[9.5,0],size=[3,3])
		if choice==218:
			img1=visual.ImageStim(mywindow, image="cext_under3_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15.5,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[9.5,0],size=[2.5,2.5])
		if choice==219:
			img1=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15.5,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[9.5,0],size=[3,3])
		if choice==220:
			img1=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15.5,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[9.5,0],size=[2.5,2.5])
		if choice==221:
			img1=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[9.5,0],size=[3,3])
		if choice==222:
			img1=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15.5,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2.5,2.5])
		if choice==223:
			img1=visual.ImageStim(mywindow, image="cext_over2_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[9.5,0],size=[3,3])
		if choice==224:
			img1=visual.ImageStim(mywindow, image="cext_under3_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15.5,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[2.5,2.5])
		if choice==225:
			img1=visual.ImageStim(mywindow, image="cext_over2_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[9.5,0],size=[3,3])
		if choice==226:
			img1=visual.ImageStim(mywindow, image="cext_under3_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15.5,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[2.5,2.5])
		if choice==227:
			img1=visual.ImageStim(mywindow, image="cext_over2_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[9.5,0],size=[3,3])
		if choice==228:
			img1=visual.ImageStim(mywindow, image="cext_under3_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15.5,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[2.5,2.5])
		if choice==229:
			img1=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[9.5,0],size=[3,3])
		if choice==230:
			img1=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15.5,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2.5,2.5])
		if choice==231:
			img1=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15.5,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[3,3])
		if choice==232:
			img1=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[9.5,0],size=[2.5,2.5])
		if choice==233:
			img1=visual.ImageStim(mywindow, image="cext_over3_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15.5,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[3,3])
		if choice==234:
			img1=visual.ImageStim(mywindow, image="cext_under2_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[9.5,0],size=[2.5,2.5])
		if choice==235:
			img1=visual.ImageStim(mywindow, image="cext_over3_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15.5,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[3,3])
		if choice==236:
			img1=visual.ImageStim(mywindow, image="cext_under2_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[9.5,0],size=[2.5,2.5])
		if choice==237:
			img1=visual.ImageStim(mywindow, image="cext_over3_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15.5,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[3,3])
		if choice==238:
			img1=visual.ImageStim(mywindow, image="cext_under2_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[9.5,0],size=[2.5,2.5])
		if choice==239:
			img1=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15.5,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[3,3])
		if choice==240:
			img1=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[9.5,0],size=[2.5,2.5])
		if choice==241:
			img1=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2.5,2.5])
		if choice==242:
			img1=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2,2])
		if choice==243:
			img1=visual.ImageStim(mywindow, image="cext_over2_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[2.5,2.5])
		if choice==244:
			img1=visual.ImageStim(mywindow, image="cext_under2_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[2,2])
		if choice==245:
			img1=visual.ImageStim(mywindow, image="cext_over2_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[2.5,2.5])
		if choice==246:
			img1=visual.ImageStim(mywindow, image="cext_under2_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[2,2])
		if choice==247:
			img1=visual.ImageStim(mywindow, image="cext_over2_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[2.5,2.5])
		if choice==248:
			img1=visual.ImageStim(mywindow, image="cext_under2_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[2,2])
		if choice==249:
			img1=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2.5,2.5])
		if choice==250:
			img1=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2,2])
		if choice==251:
			img1=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15.5,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[9.5,0],size=[2.5,2.5])
		if choice==252:
			img1=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15.5,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[9.5,0],size=[2,2])
		if choice==253:
			img1=visual.ImageStim(mywindow, image="cext_over3_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15.5,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[9.5,0],size=[2.5,2.5])
		if choice==254:
			img1=visual.ImageStim(mywindow, image="cext_under3_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15.5,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[9.5,0],size=[2,2])
		if choice==255:
			img1=visual.ImageStim(mywindow, image="cext_over3_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15.5,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[9.5,0],size=[2.5,2.5])
		if choice==256:
			img1=visual.ImageStim(mywindow, image="cext_under3_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15.5,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[9.5,0],size=[2,2])
		if choice==257:
			img1=visual.ImageStim(mywindow, image="cext_over3_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15.5,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[9.5,0],size=[2.5,2.5])
		if choice==258:
			img1=visual.ImageStim(mywindow, image="cext_under3_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15.5,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[9.5,0],size=[2,2])
		if choice==259:
			img1=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15.5,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[9.5,0],size=[2.5,2.5])
		if choice==260:
			img1=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15.5,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[9.5,0],size=[2,2])
		if choice==261:
			img1=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[9.5,0],size=[2.5,2.5])
		if choice==262:
			img1=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15.5,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2,2])
		if choice==263:
			img1=visual.ImageStim(mywindow, image="cext_over2_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[9.5,0],size=[2.5,2.5])
		if choice==264:
			img1=visual.ImageStim(mywindow, image="cext_under3_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15.5,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[2,2])
		if choice==265:
			img1=visual.ImageStim(mywindow, image="cext_over2_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[9.5,0],size=[2.5,2.5])
		if choice==266:
			img1=visual.ImageStim(mywindow, image="cext_under3_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15.5,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[2,2])
		if choice==267:
			img1=visual.ImageStim(mywindow, image="cext_over2_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[9.5,0],size=[2.5,2.5])
		if choice==268:
			img1=visual.ImageStim(mywindow, image="cext_under3_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15.5,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[2,2])
		if choice==269:
			img1=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[9.5,0],size=[2.5,2.5])
		if choice==270:
			img1=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15.5,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2,2])
		if choice==271:
			img1=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15.5,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2.5,2.5])
		if choice==272:
			img1=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[9.5,0],size=[2,2])
		if choice==273:
			img1=visual.ImageStim(mywindow, image="cext_over3_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15.5,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[2.5,2.5])
		if choice==274:
			img1=visual.ImageStim(mywindow, image="cext_under2_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[9.5,0],size=[2,2])
		if choice==275:
			img1=visual.ImageStim(mywindow, image="cext_over3_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15.5,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[2.5,2.5])
		if choice==276:
			img1=visual.ImageStim(mywindow, image="cext_under2_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[9.5,0],size=[2,2])
		if choice==277:
			img1=visual.ImageStim(mywindow, image="cext_over3_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15.5,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[2.5,2.5])
		if choice==278:
			img1=visual.ImageStim(mywindow, image="cext_under2_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[9.5,0],size=[2,2])
		if choice==279:
			img1=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15.5,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2.5,2.5])
		if choice==280:
			img1=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[9.5,0],size=[2,2])
		if choice==281:
			img1=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2,2])
		if choice==282:
			img1=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1.5,1.5])
		if choice==283:
			img1=visual.ImageStim(mywindow, image="cext_over2_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[2,2])
		if choice==284:
			img1=visual.ImageStim(mywindow, image="cext_under2_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[1.5,1.5])
		if choice==285:
			img1=visual.ImageStim(mywindow, image="cext_over2_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[2,2])
		if choice==286:
			img1=visual.ImageStim(mywindow, image="cext_under2_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[1.5,1.5])
		if choice==287:
			img1=visual.ImageStim(mywindow, image="cext_over2_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[2,2])
		if choice==288:
			img1=visual.ImageStim(mywindow, image="cext_under2_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[1.5,1.5])
		if choice==289:
			img1=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2,2])
		if choice==290:
			img1=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1.5,1.5])
		if choice==291:
			img1=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15.5,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[9.5,0],size=[2,2])
		if choice==292:
			img1=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15.5,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[9.5,0],size=[1.5,1.5])
		if choice==293:
			img1=visual.ImageStim(mywindow, image="cext_over3_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15.5,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[9.5,0],size=[2,2])
		if choice==294:
			img1=visual.ImageStim(mywindow, image="cext_under3_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15.5,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[9.5,0],size=[1.5,1.5])
		if choice==295:
			img1=visual.ImageStim(mywindow, image="cext_over3_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15.5,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[9.5,0],size=[2,2])
		if choice==296:
			img1=visual.ImageStim(mywindow, image="cext_under3_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15.5,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[9.5,0],size=[1.5,1.5])
		if choice==297:
			img1=visual.ImageStim(mywindow, image="cext_over3_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15.5,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[9.5,0],size=[2,2])
		if choice==298:
			img1=visual.ImageStim(mywindow, image="cext_under3_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15.5,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[9.5,0],size=[1.5,1.5])
		if choice==299:
			img1=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15.5,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[9.5,0],size=[2,2])
		if choice==300:
			img1=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15.5,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[9.5,0],size=[1.5,1.5])
		if choice==301:
			img1=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2,2])
		if choice==302:
			img1=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1.5,1.5])
		if choice==303:
			img1=visual.ImageStim(mywindow, image="cext_over2_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[2,2])
		if choice==304:
			img1=visual.ImageStim(mywindow, image="cext_under3_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[1.5,1.5])
		if choice==305:
			img1=visual.ImageStim(mywindow, image="cext_over2_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[2,2])
		if choice==306:
			img1=visual.ImageStim(mywindow, image="cext_under3_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[1.5,1.5])
		if choice==307:
			img1=visual.ImageStim(mywindow, image="cext_over2_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[2,2])
		if choice==308:
			img1=visual.ImageStim(mywindow, image="cext_under3_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[1.5,1.5])
		if choice==309:
			img1=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2,2])
		if choice==310:
			img1=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1.5,1.5])
		if choice==311:
			img1=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15.5,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2,2])
		if choice==312:
			img1=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15.5,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1.5,1.5])
		if choice==313:
			img1=visual.ImageStim(mywindow, image="cext_over3_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15.5,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[2,2])
		if choice==314:
			img1=visual.ImageStim(mywindow, image="cext_under2_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15.5,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[1.5,1.5])
		if choice==315:
			img1=visual.ImageStim(mywindow, image="cext_over3_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15.5,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[2,2])
		if choice==316:
			img1=visual.ImageStim(mywindow, image="cext_under2_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15.5,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[1.5,1.5])
		if choice==317:
			img1=visual.ImageStim(mywindow, image="cext_over3_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15.5,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[2,2])
		if choice==318:
			img1=visual.ImageStim(mywindow, image="cext_under2_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15.5,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[1.5,1.5])
		if choice==319:
			img1=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15.5,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2,2])
		if choice==320:
			img1=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15.5,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1.5,1.5])
		if choice==321:
			img1=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1.5,1.5])
		if choice==322:
			img1=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1,1])
		if choice==323:
			img1=visual.ImageStim(mywindow, image="cext_over2_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[1.5,1.5])
		if choice==324:
			img1=visual.ImageStim(mywindow, image="cext_under2_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[1,1])
		if choice==325:
			img1=visual.ImageStim(mywindow, image="cext_over2_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[1.5,1.5])
		if choice==326:
			img1=visual.ImageStim(mywindow, image="cext_under2_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[1,1])
		if choice==327:
			img1=visual.ImageStim(mywindow, image="cext_over2_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[1.5,1.5])
		if choice==328:
			img1=visual.ImageStim(mywindow, image="cext_under2_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[1,1])
		if choice==329:
			img1=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1.5,1.5])
		if choice==330:
			img1=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1,1])
		if choice==331:
			img1=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1.5,1.5])
		if choice==332:
			img1=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1,1])
		if choice==333:
			img1=visual.ImageStim(mywindow, image="cext_over3_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[1.5,1.5])
		if choice==334:
			img1=visual.ImageStim(mywindow, image="cext_under3_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[1,1])
		if choice==335:
			img1=visual.ImageStim(mywindow, image="cext_over3_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[1.5,1.5])
		if choice==336:
			img1=visual.ImageStim(mywindow, image="cext_under3_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[1,1])
		if choice==337:
			img1=visual.ImageStim(mywindow, image="cext_over3_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[1.5,1.5])
		if choice==338:
			img1=visual.ImageStim(mywindow, image="cext_under3_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[1,1])
		if choice==339:
			img1=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1.5,1.5])
		if choice==340:
			img1=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1,1])
		if choice==341:
			img1=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1.5,1.5])
		if choice==342:
			img1=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1,1])
		if choice==343:
			img1=visual.ImageStim(mywindow, image="cext_over2_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[1.5,1.5])
		if choice==344:
			img1=visual.ImageStim(mywindow, image="cext_under3_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[1,1])
		if choice==345:
			img1=visual.ImageStim(mywindow, image="cext_over2_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[1.5,1.5])
		if choice==346:
			img1=visual.ImageStim(mywindow, image="cext_under3_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[1,1])
		if choice==347:
			img1=visual.ImageStim(mywindow, image="cext_over2_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[1.5,1.5])
		if choice==348:
			img1=visual.ImageStim(mywindow, image="cext_under3_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[1,1])
		if choice==349:
			img1=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1.5,1.5])
		if choice==350:
			img1=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1,1])
		if choice==351:
			img1=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1.5,1.5])
		if choice==352:
			img1=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1,1])
		if choice==353:
			img1=visual.ImageStim(mywindow, image="cext_over3_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[1.5,1.5])
		if choice==354:
			img1=visual.ImageStim(mywindow, image="cext_under2_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[1,1])
		if choice==355:
			img1=visual.ImageStim(mywindow, image="cext_over3_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[1.5,1.5])
		if choice==356:
			img1=visual.ImageStim(mywindow, image="cext_under2_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[1,1])
		if choice==357:
			img1=visual.ImageStim(mywindow, image="cext_over3_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[1.5,1.5])
		if choice==358:
			img1=visual.ImageStim(mywindow, image="cext_under2_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[1,1])
		if choice==359:
			img1=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1.5,1.5])
		if choice==360:
			img1=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1,1])
		if choice==361:
			img1=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2.5,2.5])
		if choice==362:
			img1=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1.5,1.5])
		if choice==363:
			img1=visual.ImageStim(mywindow, image="cext_over2_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[2.5,2.5])
		if choice==364:
			img1=visual.ImageStim(mywindow, image="cext_under2_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[1.5,1.5])
		if choice==365:
			img1=visual.ImageStim(mywindow, image="cext_over2_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[2.5,2.5])
		if choice==366:
			img1=visual.ImageStim(mywindow, image="cext_under2_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[1.5,1.5])
		if choice==367:
			img1=visual.ImageStim(mywindow, image="cext_over2_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[2.5,2.5])
		if choice==368:
			img1=visual.ImageStim(mywindow, image="cext_under2_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[1.5,1.5])
		if choice==369:
			img1=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2.5,2.5])
		if choice==370:
			img1=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1.5,1.5])
		if choice==371:
			img1=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2.5,2.5])
		if choice==372:
			img1=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1.5,1.5])
		if choice==373:
			img1=visual.ImageStim(mywindow, image="cext_over3_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[2.5,2.5])
		if choice==374:
			img1=visual.ImageStim(mywindow, image="cext_under3_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[1.5,1.5])
		if choice==375:
			img1=visual.ImageStim(mywindow, image="cext_over3_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[2.5,2.5])
		if choice==376:
			img1=visual.ImageStim(mywindow, image="cext_under3_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[1.5,1.5])
		if choice==377:
			img1=visual.ImageStim(mywindow, image="cext_over3_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[2.5,2.5])
		if choice==378:
			img1=visual.ImageStim(mywindow, image="cext_under3_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[1.5,1.5])
		if choice==379:
			img1=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2.5,2.5])
		if choice==380:
			img1=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1.5,1.5])
		if choice==381:
			img1=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2.5,2.5])
		if choice==382:
			img1=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1.5,1.5])
		if choice==383:
			img1=visual.ImageStim(mywindow, image="cext_over2_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[2.5,2.5])
		if choice==384:
			img1=visual.ImageStim(mywindow, image="cext_under3_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[1.5,1.5])
		if choice==385:
			img1=visual.ImageStim(mywindow, image="cext_over2_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[2.5,2.5])
		if choice==386:
			img1=visual.ImageStim(mywindow, image="cext_under3_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[1.5,1.5])
		if choice==387:
			img1=visual.ImageStim(mywindow, image="cext_over2_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[2.5,2.5])
		if choice==388:
			img1=visual.ImageStim(mywindow, image="cext_under3_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[1.5,1.5])
		if choice==389:
			img1=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2.5,2.5])
		if choice==390:
			img1=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1.5,1.5])
		if choice==391:
			img1=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2.5,2.5])
		if choice==392:
			img1=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1.5,1.5])
		if choice==393:
			img1=visual.ImageStim(mywindow, image="cext_over3_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[2.5,2.5])
		if choice==394:
			img1=visual.ImageStim(mywindow, image="cext_under2_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[1.5,1.5])
		if choice==395:
			img1=visual.ImageStim(mywindow, image="cext_over3_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[2.5,2.5])
		if choice==396:
			img1=visual.ImageStim(mywindow, image="cext_under2_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[1.5,1.5])
		if choice==397:
			img1=visual.ImageStim(mywindow, image="cext_over3_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[2.5,2.5])
		if choice==398:
			img1=visual.ImageStim(mywindow, image="cext_under2_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[1.5,1.5])
		if choice==399:
			img1=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2.5,2.5])
		if choice==400:
			img1=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1.5,1.5])
		if choice==401:
			img1=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[3,3])
		if choice==402:
			img1=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[3,3])
		if choice==403:
			img1=visual.ImageStim(mywindow, image="cext_over7_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[3,3])
		if choice==404:
			img1=visual.ImageStim(mywindow, image="cext_under7_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[3,3])
		if choice==405:
			img1=visual.ImageStim(mywindow, image="cext_over7_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[3,3])
		if choice==406:
			img1=visual.ImageStim(mywindow, image="cext_under7_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[3,3])
		if choice==407:
			img1=visual.ImageStim(mywindow, image="cext_over7_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[3,3])
		if choice==408:
			img1=visual.ImageStim(mywindow, image="cext_under7_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[3,3])
		if choice==409:
			img1=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[3,3])
		if choice==410:
			img1=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[3,3])
		if choice==411:
			img1=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[3,3])
		if choice==412:
			img1=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[3,3])
		if choice==413:
			img1=visual.ImageStim(mywindow, image="cext_over8_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[3,3])
		if choice==414:
			img1=visual.ImageStim(mywindow, image="cext_under8_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[3,3])
		if choice==415:
			img1=visual.ImageStim(mywindow, image="cext_over8_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[3,3])
		if choice==416:
			img1=visual.ImageStim(mywindow, image="cext_under8_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[3,3])
		if choice==417:
			img1=visual.ImageStim(mywindow, image="cext_over8_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[3,3])
		if choice==418:
			img1=visual.ImageStim(mywindow, image="cext_under8_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[3,3])
		if choice==419:
			img1=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[3,3])
		if choice==420:
			img1=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[3,3])
		if choice==421:
			img1=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[3,3])
		if choice==422:
			img1=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[3,3])
		if choice==423:
			img1=visual.ImageStim(mywindow, image="cext_over7_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[3,3])
		if choice==424:
			img1=visual.ImageStim(mywindow, image="cext_under8_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[3,3])
		if choice==425:
			img1=visual.ImageStim(mywindow, image="cext_over7_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[3,3])
		if choice==426:
			img1=visual.ImageStim(mywindow, image="cext_under8_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[3,3])
		if choice==427:
			img1=visual.ImageStim(mywindow, image="cext_over7_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[3,3])
		if choice==428:
			img1=visual.ImageStim(mywindow, image="cext_under8_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[3,3])
		if choice==429:
			img1=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[3,3])
		if choice==430:
			img1=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[3,3])
		if choice==431:
			img1=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[3,3])
		if choice==432:
			img1=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[3,3])
		if choice==433:
			img1=visual.ImageStim(mywindow, image="cext_over8_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[3,3])
		if choice==434:
			img1=visual.ImageStim(mywindow, image="cext_under7_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[3,3])
		if choice==435:
			img1=visual.ImageStim(mywindow, image="cext_over8_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[3,3])
		if choice==436:
			img1=visual.ImageStim(mywindow, image="cext_under7_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[3,3])
		if choice==437:
			img1=visual.ImageStim(mywindow, image="cext_over8_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[3,3])
		if choice==438:
			img1=visual.ImageStim(mywindow, image="cext_under7_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[3,3])
		if choice==439:
			img1=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[3,3])
		if choice==440:
			img1=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[3,3])
		if choice==441:
			img1=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2.5,2.5])
		if choice==442:
			img1=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2.5,2.5])
		if choice==443:
			img1=visual.ImageStim(mywindow, image="cext_over7_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[2.5,2.5])
		if choice==444:
			img1=visual.ImageStim(mywindow, image="cext_under7_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[2.5,2.5])
		if choice==445:
			img1=visual.ImageStim(mywindow, image="cext_over7_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[2.5,2.5])
		if choice==446:
			img1=visual.ImageStim(mywindow, image="cext_under7_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[2.5,2.5])
		if choice==447:
			img1=visual.ImageStim(mywindow, image="cext_over7_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[2.5,2.5])
		if choice==448:
			img1=visual.ImageStim(mywindow, image="cext_under7_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[2.5,2.5])
		if choice==449:
			img1=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2.5,2.5])
		if choice==450:
			img1=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2.5,2.5])
		if choice==451:
			img1=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2.5,2.5])
		if choice==452:
			img1=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2.5,2.5])
		if choice==453:
			img1=visual.ImageStim(mywindow, image="cext_over8_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[2.5,2.5])
		if choice==454:
			img1=visual.ImageStim(mywindow, image="cext_under8_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[2.5,2.5])
		if choice==455:
			img1=visual.ImageStim(mywindow, image="cext_over8_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[2.5,2.5])
		if choice==456:
			img1=visual.ImageStim(mywindow, image="cext_under8_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[2.5,2.5])
		if choice==457:
			img1=visual.ImageStim(mywindow, image="cext_over8_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[2.5,2.5])
		if choice==458:
			img1=visual.ImageStim(mywindow, image="cext_under8_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[2.5,2.5])
		if choice==459:
			img1=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2.5,2.5])
		if choice==460:
			img1=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2.5,2.5])
		if choice==461:
			img1=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2.5,2.5])
		if choice==462:
			img1=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2.5,2.5])
		if choice==463:
			img1=visual.ImageStim(mywindow, image="cext_over7_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[2.5,2.5])
		if choice==464:
			img1=visual.ImageStim(mywindow, image="cext_under8_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[2.5,2.5])
		if choice==465:
			img1=visual.ImageStim(mywindow, image="cext_over7_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[2.5,2.5])
		if choice==466:
			img1=visual.ImageStim(mywindow, image="cext_under8_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[2.5,2.5])
		if choice==467:
			img1=visual.ImageStim(mywindow, image="cext_over7_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[2.5,2.5])
		if choice==468:
			img1=visual.ImageStim(mywindow, image="cext_under8_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[2.5,2.5])
		if choice==469:
			img1=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2.5,2.5])
		if choice==470:
			img1=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2.5,2.5])
		if choice==471:
			img1=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2.5,2.5])
		if choice==472:
			img1=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2.5,2.5])
		if choice==473:
			img1=visual.ImageStim(mywindow, image="cext_over8_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[2.5,2.5])
		if choice==474:
			img1=visual.ImageStim(mywindow, image="cext_under7_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[2.5,2.5])
		if choice==475:
			img1=visual.ImageStim(mywindow, image="cext_over8_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[2.5,2.5])
		if choice==476:
			img1=visual.ImageStim(mywindow, image="cext_under7_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[2.5,2.5])
		if choice==477:
			img1=visual.ImageStim(mywindow, image="cext_over8_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[2.5,2.5])
		if choice==478:
			img1=visual.ImageStim(mywindow, image="cext_under7_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[2.5,2.5])
		if choice==479:
			img1=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2.5,2.5])
		if choice==480:
			img1=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2.5,2.5])
		if choice==481:
			img1=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2,2])
		if choice==482:
			img1=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2,2])
		if choice==483:
			img1=visual.ImageStim(mywindow, image="cext_over7_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[2,2])
		if choice==484:
			img1=visual.ImageStim(mywindow, image="cext_under7_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[2,2])
		if choice==485:
			img1=visual.ImageStim(mywindow, image="cext_over7_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[2,2])
		if choice==486:
			img1=visual.ImageStim(mywindow, image="cext_under7_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[2,2])
		if choice==487:
			img1=visual.ImageStim(mywindow, image="cext_over7_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[2,2])
		if choice==488:
			img1=visual.ImageStim(mywindow, image="cext_under7_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[2,2])
		if choice==489:
			img1=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2,2])
		if choice==490:
			img1=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2,2])
		if choice==491:
			img1=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2,2])
		if choice==492:
			img1=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2,2])
		if choice==493:
			img1=visual.ImageStim(mywindow, image="cext_over8_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[2,2])
		if choice==494:
			img1=visual.ImageStim(mywindow, image="cext_under8_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[2,2])
		if choice==495:
			img1=visual.ImageStim(mywindow, image="cext_over8_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[2,2])
		if choice==496:
			img1=visual.ImageStim(mywindow, image="cext_under8_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[2,2])
		if choice==497:
			img1=visual.ImageStim(mywindow, image="cext_over8_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[2,2])
		if choice==498:
			img1=visual.ImageStim(mywindow, image="cext_under8_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[2,2])
		if choice==499:
			img1=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2,2])
		if choice==500:
			img1=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2,2])
		if choice==501:
			img1=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2,2])
		if choice==502:
			img1=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2,2])
		if choice==503:
			img1=visual.ImageStim(mywindow, image="cext_over7_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[2,2])
		if choice==504:
			img1=visual.ImageStim(mywindow, image="cext_under8_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[2,2])
		if choice==505:
			img1=visual.ImageStim(mywindow, image="cext_over7_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[2,2])
		if choice==506:
			img1=visual.ImageStim(mywindow, image="cext_under8_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[2,2])
		if choice==507:
			img1=visual.ImageStim(mywindow, image="cext_over7_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[2,2])
		if choice==508:
			img1=visual.ImageStim(mywindow, image="cext_under8_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[2,2])
		if choice==509:
			img1=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2,2])
		if choice==510:
			img1=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2,2])
		if choice==511:
			img1=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2,2])
		if choice==512:
			img1=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2,2])
		if choice==513:
			img1=visual.ImageStim(mywindow, image="cext_over8_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[2,2])
		if choice==514:
			img1=visual.ImageStim(mywindow, image="cext_under7_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[2,2])
		if choice==515:
			img1=visual.ImageStim(mywindow, image="cext_over8_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[2,2])
		if choice==516:
			img1=visual.ImageStim(mywindow, image="cext_under7_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[2,2])
		if choice==517:
			img1=visual.ImageStim(mywindow, image="cext_over8_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[2,2])
		if choice==518:
			img1=visual.ImageStim(mywindow, image="cext_under7_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[2,2])
		if choice==519:
			img1=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2,2])
		if choice==520:
			img1=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2,2])
		if choice==521:
			img1=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1.5,1.5])
		if choice==522:
			img1=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1.5,1.5])
		if choice==523:
			img1=visual.ImageStim(mywindow, image="cext_over7_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[1.5,1.5])
		if choice==524:
			img1=visual.ImageStim(mywindow, image="cext_under7_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[1.5,1.5])
		if choice==525:
			img1=visual.ImageStim(mywindow, image="cext_over7_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[1.5,1.5])
		if choice==526:
			img1=visual.ImageStim(mywindow, image="cext_under7_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[1.5,1.5])
		if choice==527:
			img1=visual.ImageStim(mywindow, image="cext_over7_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[1.5,1.5])
		if choice==528:
			img1=visual.ImageStim(mywindow, image="cext_under7_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[1.5,1.5])
		if choice==529:
			img1=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1.5,1.5])
		if choice==530:
			img1=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1.5,1.5])
		if choice==531:
			img1=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1.5,1.5])
		if choice==532:
			img1=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1.5,1.5])
		if choice==533:
			img1=visual.ImageStim(mywindow, image="cext_over8_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[1.5,1.5])
		if choice==534:
			img1=visual.ImageStim(mywindow, image="cext_under8_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[1.5,1.5])
		if choice==535:
			img1=visual.ImageStim(mywindow, image="cext_over8_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[1.5,1.5])
		if choice==536:
			img1=visual.ImageStim(mywindow, image="cext_under8_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[1.5,1.5])
		if choice==537:
			img1=visual.ImageStim(mywindow, image="cext_over8_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[1.5,1.5])
		if choice==538:
			img1=visual.ImageStim(mywindow, image="cext_under8_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[1.5,1.5])
		if choice==539:
			img1=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1.5,1.5])
		if choice==540:
			img1=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1.5,1.5])
		if choice==541:
			img1=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1.5,1.5])
		if choice==542:
			img1=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1.5,1.5])
		if choice==543:
			img1=visual.ImageStim(mywindow, image="cext_over7_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[1.5,1.5])
		if choice==544:
			img1=visual.ImageStim(mywindow, image="cext_under8_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[1.5,1.5])
		if choice==545:
			img1=visual.ImageStim(mywindow, image="cext_over7_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[1.5,1.5])
		if choice==546:
			img1=visual.ImageStim(mywindow, image="cext_under8_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[1.5,1.5])
		if choice==547:
			img1=visual.ImageStim(mywindow, image="cext_over7_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[1.5,1.5])
		if choice==548:
			img1=visual.ImageStim(mywindow, image="cext_under8_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[1.5,1.5])
		if choice==549:
			img1=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1.5,1.5])
		if choice==550:
			img1=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1.5,1.5])
		if choice==551:
			img1=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1.5,1.5])
		if choice==552:
			img1=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1.5,1.5])
		if choice==553:
			img1=visual.ImageStim(mywindow, image="cext_over8_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[1.5,1.5])
		if choice==554:
			img1=visual.ImageStim(mywindow, image="cext_under7_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[1.5,1.5])
		if choice==555:
			img1=visual.ImageStim(mywindow, image="cext_over8_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[1.5,1.5])
		if choice==556:
			img1=visual.ImageStim(mywindow, image="cext_under7_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[1.5,1.5])
		if choice==557:
			img1=visual.ImageStim(mywindow, image="cext_over8_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[1.5,1.5])
		if choice==558:
			img1=visual.ImageStim(mywindow, image="cext_under7_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[1.5,1.5])
		if choice==559:
			img1=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1.5,1.5])
		if choice==560:
			img1=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1.5,1.5])
		if choice==561:
			img1=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1,1])
		if choice==562:
			img1=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1,1])
		if choice==563:
			img1=visual.ImageStim(mywindow, image="cext_over7_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[1,1])
		if choice==564:
			img1=visual.ImageStim(mywindow, image="cext_under7_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[1,1])
		if choice==565:
			img1=visual.ImageStim(mywindow, image="cext_over7_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[1,1])
		if choice==566:
			img1=visual.ImageStim(mywindow, image="cext_under7_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[1,1])
		if choice==567:
			img1=visual.ImageStim(mywindow, image="cext_over7_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[1,1])
		if choice==568:
			img1=visual.ImageStim(mywindow, image="cext_under7_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[1,1])
		if choice==569:
			img1=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1,1])
		if choice==570:
			img1=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1,1])
		if choice==571:
			img1=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1,1])
		if choice==572:
			img1=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1,1])
		if choice==573:
			img1=visual.ImageStim(mywindow, image="cext_over8_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[1,1])
		if choice==574:
			img1=visual.ImageStim(mywindow, image="cext_under8_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[1,1])
		if choice==575:
			img1=visual.ImageStim(mywindow, image="cext_over8_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[1,1])
		if choice==576:
			img1=visual.ImageStim(mywindow, image="cext_under8_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[1,1])
		if choice==577:
			img1=visual.ImageStim(mywindow, image="cext_over8_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[1,1])
		if choice==578:
			img1=visual.ImageStim(mywindow, image="cext_under8_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[1,1])
		if choice==579:
			img1=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1,1])
		if choice==580:
			img1=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1,1])
		if choice==581:
			img1=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1,1])
		if choice==582:
			img1=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1,1])
		if choice==583:
			img1=visual.ImageStim(mywindow, image="cext_over7_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[1,1])
		if choice==584:
			img1=visual.ImageStim(mywindow, image="cext_under8_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[1,1])
		if choice==585:
			img1=visual.ImageStim(mywindow, image="cext_over7_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[1,1])
		if choice==586:
			img1=visual.ImageStim(mywindow, image="cext_under8_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[1,1])
		if choice==587:
			img1=visual.ImageStim(mywindow, image="cext_over7_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[1,1])
		if choice==588:
			img1=visual.ImageStim(mywindow, image="cext_under8_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[1,1])
		if choice==589:
			img1=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1,1])
		if choice==590:
			img1=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1,1])
		if choice==591:
			img1=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1,1])
		if choice==592:
			img1=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1,1])
		if choice==593:
			img1=visual.ImageStim(mywindow, image="cext_over8_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[1,1])
		if choice==594:
			img1=visual.ImageStim(mywindow, image="cext_under7_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[1,1])
		if choice==595:
			img1=visual.ImageStim(mywindow, image="cext_over8_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[1,1])
		if choice==596:
			img1=visual.ImageStim(mywindow, image="cext_under7_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[1,1])
		if choice==597:
			img1=visual.ImageStim(mywindow, image="cext_over8_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[1,1])
		if choice==598:
			img1=visual.ImageStim(mywindow, image="cext_under7_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[1,1])
		if choice==599:
			img1=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1,1])
		if choice==600:
			img1=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1,1])
		if choice==601:
			img1=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[3,3])
		if choice==602:
			img1=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2.5,2.5])
		if choice==603:
			img1=visual.ImageStim(mywindow, image="cext_over7_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[3,3])
		if choice==604:
			img1=visual.ImageStim(mywindow, image="cext_under7_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[2.5,2.5])
		if choice==605:
			img1=visual.ImageStim(mywindow, image="cext_over7_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[3,3])
		if choice==606:
			img1=visual.ImageStim(mywindow, image="cext_under7_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[2.5,2.5])
		if choice==607:
			img1=visual.ImageStim(mywindow, image="cext_over7_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[3,3])
		if choice==608:
			img1=visual.ImageStim(mywindow, image="cext_under7_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[2.5,2.5])
		if choice==609:
			img1=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[3,3])
		if choice==610:
			img1=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2.5,2.5])
		if choice==611:
			img1=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[3,3])
		if choice==612:
			img1=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2.5,2.5])
		if choice==613:
			img1=visual.ImageStim(mywindow, image="cext_over8_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[3,3])
		if choice==614:
			img1=visual.ImageStim(mywindow, image="cext_under8_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[2.5,2.5])
		if choice==615:
			img1=visual.ImageStim(mywindow, image="cext_over8_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[3,3])
		if choice==616:
			img1=visual.ImageStim(mywindow, image="cext_under8_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[2.5,2.5])
		if choice==617:
			img1=visual.ImageStim(mywindow, image="cext_over8_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[3,3])
		if choice==618:
			img1=visual.ImageStim(mywindow, image="cext_under8_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[2.5,2.5])
		if choice==619:
			img1=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[3,3])
		if choice==620:
			img1=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2.5,2.5])
		if choice==621:
			img1=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[3,3])
		if choice==622:
			img1=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2.5,2.5])
		if choice==623:
			img1=visual.ImageStim(mywindow, image="cext_over7_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[3,3])
		if choice==624:
			img1=visual.ImageStim(mywindow, image="cext_under8_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[2.5,2.5])
		if choice==625:
			img1=visual.ImageStim(mywindow, image="cext_over7_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[3,3])
		if choice==626:
			img1=visual.ImageStim(mywindow, image="cext_under8_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[2.5,2.5])
		if choice==627:
			img1=visual.ImageStim(mywindow, image="cext_over7_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[3,3])
		if choice==628:
			img1=visual.ImageStim(mywindow, image="cext_under8_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[2.5,2.5])
		if choice==629:
			img1=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[3,3])
		if choice==630:
			img1=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2.5,2.5])
		if choice==631:
			img1=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[3,3])
		if choice==632:
			img1=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2.5,2.5])
		if choice==633:
			img1=visual.ImageStim(mywindow, image="cext_over8_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[3,3])
		if choice==634:
			img1=visual.ImageStim(mywindow, image="cext_under7_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[2.5,2.5])
		if choice==635:
			img1=visual.ImageStim(mywindow, image="cext_over8_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[3,3])
		if choice==636:
			img1=visual.ImageStim(mywindow, image="cext_under7_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[2.5,2.5])
		if choice==637:
			img1=visual.ImageStim(mywindow, image="cext_over8_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[3,3])
		if choice==638:
			img1=visual.ImageStim(mywindow, image="cext_under7_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[2.5,2.5])
		if choice==639:
			img1=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[3,3])
		if choice==640:
			img1=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2.5,2.5])
		if choice==641:
			img1=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2.5,2.5])
		if choice==642:
			img1=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2,2])
		if choice==643:
			img1=visual.ImageStim(mywindow, image="cext_over7_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[2.5,2.5])
		if choice==644:
			img1=visual.ImageStim(mywindow, image="cext_under7_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[2,2])
		if choice==645:
			img1=visual.ImageStim(mywindow, image="cext_over7_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[2.5,2.5])
		if choice==646:
			img1=visual.ImageStim(mywindow, image="cext_under7_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[2,2])
		if choice==647:
			img1=visual.ImageStim(mywindow, image="cext_over7_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[2.5,2.5])
		if choice==648:
			img1=visual.ImageStim(mywindow, image="cext_under7_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[2,2])
		if choice==649:
			img1=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2.5,2.5])
		if choice==650:
			img1=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2,2])
		if choice==651:
			img1=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2.5,2.5])
		if choice==652:
			img1=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2,2])
		if choice==653:
			img1=visual.ImageStim(mywindow, image="cext_over8_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[2.5,2.5])
		if choice==654:
			img1=visual.ImageStim(mywindow, image="cext_under8_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[2,2])
		if choice==655:
			img1=visual.ImageStim(mywindow, image="cext_over8_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[2.5,2.5])
		if choice==656:
			img1=visual.ImageStim(mywindow, image="cext_under8_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[2,2])
		if choice==657:
			img1=visual.ImageStim(mywindow, image="cext_over8_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[2.5,2.5])
		if choice==658:
			img1=visual.ImageStim(mywindow, image="cext_under8_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[2,2])
		if choice==659:
			img1=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2.5,2.5])
		if choice==660:
			img1=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2,2])
		if choice==661:
			img1=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2.5,2.5])
		if choice==662:
			img1=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2,2])
		if choice==663:
			img1=visual.ImageStim(mywindow, image="cext_over7_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[2.5,2.5])
		if choice==664:
			img1=visual.ImageStim(mywindow, image="cext_under8_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[2,2])
		if choice==665:
			img1=visual.ImageStim(mywindow, image="cext_over7_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[2.5,2.5])
		if choice==666:
			img1=visual.ImageStim(mywindow, image="cext_under8_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[2,2])
		if choice==667:
			img1=visual.ImageStim(mywindow, image="cext_over7_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[2.5,2.5])
		if choice==668:
			img1=visual.ImageStim(mywindow, image="cext_under8_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[2,2])
		if choice==669:
			img1=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2.5,2.5])
		if choice==670:
			img1=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2,2])
		if choice==671:
			img1=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2.5,2.5])
		if choice==672:
			img1=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2,2])
		if choice==673:
			img1=visual.ImageStim(mywindow, image="cext_over8_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[2.5,2.5])
		if choice==674:
			img1=visual.ImageStim(mywindow, image="cext_under7_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[2,2])
		if choice==675:
			img1=visual.ImageStim(mywindow, image="cext_over8_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[2.5,2.5])
		if choice==676:
			img1=visual.ImageStim(mywindow, image="cext_under7_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[2,2])
		if choice==677:
			img1=visual.ImageStim(mywindow, image="cext_over8_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[2.5,2.5])
		if choice==678:
			img1=visual.ImageStim(mywindow, image="cext_under7_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[2,2])
		if choice==679:
			img1=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2.5,2.5])
		if choice==680:
			img1=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2,2])
		if choice==681:
			img1=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2,2])
		if choice==682:
			img1=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1.5,1.5])
		if choice==683:
			img1=visual.ImageStim(mywindow, image="cext_over7_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[2,2])
		if choice==684:
			img1=visual.ImageStim(mywindow, image="cext_under7_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[1.5,1.5])
		if choice==685:
			img1=visual.ImageStim(mywindow, image="cext_over7_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[2,2])
		if choice==686:
			img1=visual.ImageStim(mywindow, image="cext_under7_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[1.5,1.5])
		if choice==687:
			img1=visual.ImageStim(mywindow, image="cext_over7_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[2,2])
		if choice==688:
			img1=visual.ImageStim(mywindow, image="cext_under7_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[1.5,1.5])
		if choice==689:
			img1=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2,2])
		if choice==690:
			img1=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1.5,1.5])
		if choice==691:
			img1=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2,2])
		if choice==692:
			img1=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1.5,1.5])
		if choice==693:
			img1=visual.ImageStim(mywindow, image="cext_over8_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[2,2])
		if choice==694:
			img1=visual.ImageStim(mywindow, image="cext_under8_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[1.5,1.5])
		if choice==695:
			img1=visual.ImageStim(mywindow, image="cext_over8_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[2,2])
		if choice==696:
			img1=visual.ImageStim(mywindow, image="cext_under8_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[1.5,1.5])
		if choice==697:
			img1=visual.ImageStim(mywindow, image="cext_over8_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[2,2])
		if choice==698:
			img1=visual.ImageStim(mywindow, image="cext_under8_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[1.5,1.5])
		if choice==699:
			img1=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2,2])
		if choice==700:
			img1=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1.5,1.5])
		if choice==701:
			img1=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2,2])
		if choice==702:
			img1=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1.5,1.5])
		if choice==703:
			img1=visual.ImageStim(mywindow, image="cext_over7_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[2,2])
		if choice==704:
			img1=visual.ImageStim(mywindow, image="cext_under8_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[1.5,1.5])
		if choice==705:
			img1=visual.ImageStim(mywindow, image="cext_over7_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[2,2])
		if choice==706:
			img1=visual.ImageStim(mywindow, image="cext_under8_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[1.5,1.5])
		if choice==707:
			img1=visual.ImageStim(mywindow, image="cext_over7_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[2,2])
		if choice==708:
			img1=visual.ImageStim(mywindow, image="cext_under8_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[1.5,1.5])
		if choice==709:
			img1=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2,2])
		if choice==710:
			img1=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1.5,1.5])
		if choice==711:
			img1=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2,2])
		if choice==712:
			img1=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1.5,1.5])
		if choice==713:
			img1=visual.ImageStim(mywindow, image="cext_over8_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[2,2])
		if choice==714:
			img1=visual.ImageStim(mywindow, image="cext_under7_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[1.5,1.5])
		if choice==715:
			img1=visual.ImageStim(mywindow, image="cext_over8_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[2,2])
		if choice==716:
			img1=visual.ImageStim(mywindow, image="cext_under7_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[1.5,1.5])
		if choice==717:
			img1=visual.ImageStim(mywindow, image="cext_over8_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[2,2])
		if choice==718:
			img1=visual.ImageStim(mywindow, image="cext_under7_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[1.5,1.5])
		if choice==719:
			img1=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2,2])
		if choice==720:
			img1=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1.5,1.5])
		if choice==721:
			img1=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1.5,1.5])
		if choice==722:
			img1=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1,1])
		if choice==723:
			img1=visual.ImageStim(mywindow, image="cext_over7_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[1.5,1.5])
		if choice==724:
			img1=visual.ImageStim(mywindow, image="cext_under7_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[1,1])
		if choice==725:
			img1=visual.ImageStim(mywindow, image="cext_over7_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[1.5,1.5])
		if choice==726:
			img1=visual.ImageStim(mywindow, image="cext_under7_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[1,1])
		if choice==727:
			img1=visual.ImageStim(mywindow, image="cext_over7_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[1.5,1.5])
		if choice==728:
			img1=visual.ImageStim(mywindow, image="cext_under7_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[1,1])
		if choice==729:
			img1=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1.5,1.5])
		if choice==730:
			img1=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1,1])
		if choice==731:
			img1=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1.5,1.5])
		if choice==732:
			img1=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1,1])
		if choice==733:
			img1=visual.ImageStim(mywindow, image="cext_over8_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[1.5,1.5])
		if choice==734:
			img1=visual.ImageStim(mywindow, image="cext_under8_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[1,1])
		if choice==735:
			img1=visual.ImageStim(mywindow, image="cext_over8_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[1.5,1.5])
		if choice==736:
			img1=visual.ImageStim(mywindow, image="cext_under8_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[1,1])
		if choice==737:
			img1=visual.ImageStim(mywindow, image="cext_over8_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[1.5,1.5])
		if choice==738:
			img1=visual.ImageStim(mywindow, image="cext_under8_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[1,1])
		if choice==739:
			img1=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1.5,1.5])
		if choice==740:
			img1=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1,1])
		if choice==741:
			img1=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1.5,1.5])
		if choice==742:
			img1=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1,1])
		if choice==743:
			img1=visual.ImageStim(mywindow, image="cext_over7_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[1.5,1.5])
		if choice==744:
			img1=visual.ImageStim(mywindow, image="cext_under8_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[1,1])
		if choice==745:
			img1=visual.ImageStim(mywindow, image="cext_over7_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[1.5,1.5])
		if choice==746:
			img1=visual.ImageStim(mywindow, image="cext_under8_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[1,1])
		if choice==747:
			img1=visual.ImageStim(mywindow, image="cext_over7_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[1.5,1.5])
		if choice==748:
			img1=visual.ImageStim(mywindow, image="cext_under8_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[1,1])
		if choice==749:
			img1=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1.5,1.5])
		if choice==750:
			img1=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1,1])
		if choice==751:
			img1=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1.5,1.5])
		if choice==752:
			img1=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1,1])
		if choice==753:
			img1=visual.ImageStim(mywindow, image="cext_over8_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[1.5,1.5])
		if choice==754:
			img1=visual.ImageStim(mywindow, image="cext_under7_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[1,1])
		if choice==755:
			img1=visual.ImageStim(mywindow, image="cext_over8_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[1.5,1.5])
		if choice==756:
			img1=visual.ImageStim(mywindow, image="cext_under7_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[1,1])
		if choice==757:
			img1=visual.ImageStim(mywindow, image="cext_over8_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[1.5,1.5])
		if choice==758:
			img1=visual.ImageStim(mywindow, image="cext_under7_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[1,1])
		if choice==759:
			img1=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1.5,1.5])
		if choice==760:
			img1=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1,1])
		if choice==761:
			img1=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2.5,2.5])
		if choice==762:
			img1=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1.5,1.5])
		if choice==763:
			img1=visual.ImageStim(mywindow, image="cext_over7_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[2.5,2.5])
		if choice==764:
			img1=visual.ImageStim(mywindow, image="cext_under7_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[1.5,1.5])
		if choice==765:
			img1=visual.ImageStim(mywindow, image="cext_over7_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[2.5,2.5])
		if choice==766:
			img1=visual.ImageStim(mywindow, image="cext_under7_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[1.5,1.5])
		if choice==767:
			img1=visual.ImageStim(mywindow, image="cext_over7_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[2.5,2.5])
		if choice==768:
			img1=visual.ImageStim(mywindow, image="cext_under7_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[1.5,1.5])
		if choice==769:
			img1=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2.5,2.5])
		if choice==770:
			img1=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1.5,1.5])
		if choice==771:
			img1=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2.5,2.5])
		if choice==772:
			img1=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1.5,1.5])
		if choice==773:
			img1=visual.ImageStim(mywindow, image="cext_over8_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[2.5,2.5])
		if choice==774:
			img1=visual.ImageStim(mywindow, image="cext_under8_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[1.5,1.5])
		if choice==775:
			img1=visual.ImageStim(mywindow, image="cext_over8_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[2.5,2.5])
		if choice==776:
			img1=visual.ImageStim(mywindow, image="cext_under8_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[1.5,1.5])
		if choice==777:
			img1=visual.ImageStim(mywindow, image="cext_over8_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[2.5,2.5])
		if choice==778:
			img1=visual.ImageStim(mywindow, image="cext_under8_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[1.5,1.5])
		if choice==779:
			img1=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2.5,2.5])
		if choice==780:
			img1=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1.5,1.5])
		if choice==781:
			img1=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2.5,2.5])
		if choice==782:
			img1=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1.5,1.5])
		if choice==783:
			img1=visual.ImageStim(mywindow, image="cext_over7_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[2.5,2.5])
		if choice==784:
			img1=visual.ImageStim(mywindow, image="cext_under8_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[1.5,1.5])
		if choice==785:
			img1=visual.ImageStim(mywindow, image="cext_over7_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[2.5,2.5])
		if choice==786:
			img1=visual.ImageStim(mywindow, image="cext_under8_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[1.5,1.5])
		if choice==787:
			img1=visual.ImageStim(mywindow, image="cext_over7_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[2.5,2.5])
		if choice==788:
			img1=visual.ImageStim(mywindow, image="cext_under8_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[1.5,1.5])
		if choice==789:
			img1=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2.5,2.5])
		if choice==790:
			img1=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1.5,1.5])
		if choice==791:
			img1=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2.5,2.5])
		if choice==792:
			img1=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1.5,1.5])
		if choice==793:
			img1=visual.ImageStim(mywindow, image="cext_over8_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[2.5,2.5])
		if choice==794:
			img1=visual.ImageStim(mywindow, image="cext_under7_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_az.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[1.5,1.5])
		if choice==795:
			img1=visual.ImageStim(mywindow, image="cext_over8_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[2.5,2.5])
		if choice==796:
			img1=visual.ImageStim(mywindow, image="cext_under7_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_ver.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[1.5,1.5])
		if choice==797:
			img1=visual.ImageStim(mywindow, image="cext_over8_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[2.5,2.5])
		if choice==798:
			img1=visual.ImageStim(mywindow, image="cext_under7_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_pur.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[1.5,1.5])
		if choice==799:
			img1=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2.5,2.5])
		if choice==800:
			img1=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[10,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1.5,1.5])
		txtRecordat1=visual.TextStim(mywindow,text="Los circulos centrales son iguales?",wrapWidth = 45,color=[0,0,0], pos=[0,10], bold="True", colorSpace="rgb255")
		txtRecordat2=visual.TextStim(mywindow,text="S = Si",wrapWidth = 45,color=[0,0,0], pos=[0,-10], bold="True", colorSpace="rgb255")
		txtRecordat3=visual.TextStim(mywindow,text="N = No",wrapWidth = 45,color=[0,0,0], pos=[0,-15], bold="True", colorSpace="rgb255")
		txtRecordat1.draw()
		txtRecordat2.draw()
		txtRecordat3.draw()
		img1.draw()
		img2.draw()
		img3.draw()
		img4.draw()
		mybaseline.close
		mywindow.update()
		core.wait(2)
		mywindow.setColor(color=[255,255,255], colorSpace="rgb255")
		mywindow.update()
		mywindow.setColor(color=[255,255,255], colorSpace="rgb255")
		mywindow.update()
		userSel=" "
		validkeys=['5', '8', '6', '4', '2', '7', 'd', 'f', 's', 'e', 'x']
		while userSel !='5' and userSel !='8' and userSel !='6' and userSel !='4' and userSel !='2' and userSel !='d' and userSel !='f' and userSel !='s' and userSel !='e' and userSel !='x' and userSel !='7':
			keys=event.getKeys()
			for k in keys:
				if k in validkeys:
					userSel=k
				elif k=='escape': 
					mytestline.Close()
					core.quit()
			core.wait(0.1)
		isCorrect=(choice in right and userSel =='6') or (choice not in right and userSel =='8')
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
