from psychopy import visual, core, event, gui
import random, time

options={"Experimento":"1a","Descripcion":"Dos Figuras", "Procedimiento":"Y/N +Rating","Participante":"Usuario1"}
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
print "Total Time"
total_time = time.time()
mywindow.setColor(color=[255,255,255], colorSpace="rgb255")
mywindow.update()
mywindow.setColor(color=[255,255,255], colorSpace="rgb255")
mywindow.update()
Instrucciones1=visual.ImageStim(mywindow, image="Inst_1.png", pos=[0,0])
Instrucciones1.draw()
#txtResults=visual.TextStim(mywindow,text="Instrucciones:"+"\n"+"\n"+"\n"+"\n"+"Se te mostraran dos circulos de color claro rodeados por circulos de distinto tamano" +"\n"+"\n"+"\n"+"\n"+"Presiona la tecla S cuando los circulos claros SI sean del mismo tamano. "+"\n"+"\n"+"Si NO son iguales, oprime N"+"\n"+"\n"+"\n"+"\n"+"\n"+"\n"+"Presiona la barra espaciadora para continuar",wrapWidth = 45,color=[0,0,0], colorSpace="rgb255")
#txtResults.draw()
mywindow.update()
while 'space' not in event.getKeys(): 
	core.wait(0.1)

#
#FIRST EXAMPLE
#
mywindow.update()
img1=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[16,-5])
img2=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[-10,-5])
img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-10.2,-5], size=[2.5,2.5])
img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[16,-5.2], size=[2,2])
txtResults=visual.TextStim(mywindow,text="Ejemplo: "+"\n"+"\n"+"\n"+"\n"+"En este caso el circulo claro de la figura derecha (el circulo central) es mas chico que el del lado izquierdo."+"\n"+"\n"+"Deberias presionar la tecla N porque NO son iguales",wrapWidth = 40,pos=[0,13], color=[0,0,0], colorSpace="rgb255")
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
Instrucciones2=visual.ImageStim(mywindow, image="Inst_3.png", pos=[0,0])
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
mybaseline=open("MirrEx1a_V2"+"_"+options["Participante"]+"_"+time.strftime("%Y-%m-%d")+"_"+"Y_N+R.csv", 'w')
right=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 453, 454, 455, 456, 457, 458, 459, 460, 461, 462, 463, 464, 465, 466, 467, 468, 469, 470, 471, 472, 473, 474, 475, 476, 477, 478, 479, 480]

Ver=[2, 5, 12, 15, 18, 21, 28, 31, 34, 37, 44, 47, 50, 53, 60, 63, 66, 69, 76, 79, 82, 85, 92, 95, 98, 101, 108, 111, 114, 117, 124, 127, 130, 133, 140, 143, 146, 149, 156, 159, 162, 165, 172, 175, 178, 181, 188, 191, 194, 197, 204, 207, 210, 213, 220, 223, 226, 229, 236, 239, 242, 245, 252, 255, 258, 261, 268, 271, 274, 277, 284, 287, 290, 293, 306, 309, 312, 315, 322, 325, 328, 331, 338, 341, 344, 347, 354, 357, 360, 363, 370, 373, 376, 379, 386, 389, 392, 395, 402, 405, 408, 411, 417, 420, 422, 425, 432, 435, 438, 441, 448, 451, 454, 457, 464, 467, 470, 473, 480, 483, 486, 489, 496, 499, 502, 505, 512, 515, 518, 521, 528, 531, 534, 537, 544, 547, 550, 553, 560, 563, 566, 569, 576, 579, 582, 585, 592, 595, 598, 601, 608, 611, 614, 617, 624, 627, 630, 633, 640, 638]
Az=[4, 7, 10, 13, 20, 23, 26, 29, 36, 39, 42, 45, 52, 55, 58, 61, 68, 71, 74, 77, 84, 87, 90, 93, 100, 103, 106, 109, 116, 119, 122, 125, 132, 135, 138, 141, 148, 151, 154, 157, 164, 167, 170, 173, 180, 183, 186, 189, 196, 199, 202, 205, 212, 215, 218, 221, 228, 231, 234, 237, 244, 247, 250, 253, 260, 263, 266, 269, 276, 279, 282, 285, 292, 295, 298, 301, 304, 307, 314, 317, 320, 323, 330, 333, 336, 339, 346, 349, 352, 355, 362, 365, 368, 371, 378, 381, 384, 387, 394, 397, 400, 403, 410, 412, 415, 418, 424, 427, 430, 433, 440, 443, 446, 449, 455, 459, 462, 465, 472, 475, 478, 481, 488, 491, 494, 497, 504, 507, 510, 513, 520, 523, 526, 529, 536, 539, 542, 545, 552, 555, 558, 561, 568, 571, 574, 577, 584, 587, 590, 593, 600, 603, 606, 609, 616, 619, 622, 625, 632, 636] 
Nar=[1, 8, 11, 14, 17, 24, 27, 30, 33, 40, 43, 46, 49, 56, 59, 62, 65, 72, 75, 78, 81, 88, 91, 94, 97, 104, 107, 110, 113, 120, 123, 126, 129, 136, 139, 142, 145, 152, 155, 158, 161, 168, 171, 174, 177, 184, 187, 190, 193, 200, 203, 206, 209, 216, 219, 222, 225, 232, 235, 238, 241, 248, 251, 254, 257, 264, 267, 270, 273, 280, 283, 286, 289, 296, 299, 302, 305, 308, 311, 318, 321, 324, 327, 334, 337, 340, 343, 350, 353, 356, 359, 366, 369, 372, 375, 382, 385, 388, 391, 398, 401, 404, 407, 413, 416, 419, 428, 431, 434, 437, 444, 447, 450, 453, 460, 463, 466, 469, 476, 479, 482, 485, 492, 495, 498, 501, 508, 511, 514, 517, 524, 527, 530, 533, 540, 543, 546, 549, 556, 559, 562, 565, 572, 575, 578, 581, 588, 591, 594, 597, 604, 607, 610, 613, 620, 623, 626, 629, 635, 639]
Pur=[3, 6, 9, 16, 19, 22, 25, 32, 35, 38, 41, 48, 51, 54, 57, 64, 67, 70, 73, 80, 83, 86, 89, 96, 99, 102, 105, 112, 115, 118, 121, 128, 131, 134, 137, 144, 147, 150, 153, 160, 163, 166, 169, 176, 179, 182, 185, 192, 195, 198, 201, 208, 211, 214, 217, 224, 227, 230, 233, 240, 243, 246, 249, 256, 259, 262, 265, 272, 275, 278, 281, 288, 291, 294, 297, 300, 303, 310, 313, 316, 319, 326, 329, 332, 335, 342, 345, 348, 351, 358, 361, 364, 367, 374, 377, 380, 383, 390, 393, 396, 399, 406, 409,  414, 421, 423, 426, 429, 436, 439, 442, 445, 452, 456, 458, 461, 468, 471, 474, 477, 484, 487, 490, 493, 500, 503, 506, 509, 516, 519, 522, 525, 532, 535, 538, 541, 548, 551, 554, 557, 564, 567, 570, 573, 580, 583, 586, 589, 596, 599, 602, 605, 612, 615, 618, 621, 628, 631, 634, 637]
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
mybaseline.write("Ensayo, Estimulo, Respuesta, Correcto, Aciertos, Errores, Hits, ContadorH, Rechazos, ContadorR, Falsas alarmas, ContadorF, Omisiones, ContadorM, Confidence, RTime1, RTime1b, RTime2, Color, \n")
mywindow.update()

#
#BEGIN OF FIRST BLOCK
#
for j in range(1):
	central = list()
	for i in range (640):
		central.append (i+1)
	for i in range (640):
#		choice=779
		choice=central.pop(random.randint(0,len(central)-1))
		if choice==1:
			img1=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[11,0],size=[3,3])
		if choice==2:
			img1=visual.ImageStim(mywindow, image="cext_under2_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[11,0],size=[3,3])
		if choice==3:
			img1=visual.ImageStim(mywindow, image="cext_over2_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[11,0],size=[3,3])
		if choice==4:
			img1=visual.ImageStim(mywindow, image="cext_under2_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[11,0],size=[3,3])
		if choice==5:
			img1=visual.ImageStim(mywindow, image="cext_over2_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[11,0],size=[3,3])
		if choice==6:
			img1=visual.ImageStim(mywindow, image="cext_under2_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[11,0],size=[3,3])
		if choice==7:
			img1=visual.ImageStim(mywindow, image="cext_over2_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[11,0],size=[3,3])
		if choice==8:
			img1=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[11,0],size=[3,3])
		if choice==9:
			img1=visual.ImageStim(mywindow, image="cext_over3_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15.5,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[3,3])
		if choice==10:
			img1=visual.ImageStim(mywindow, image="cext_under3_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-16,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10.5,0],size=[3,3])
		if choice==11:
			img1=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15.5,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[3,3])
		if choice==12:
			img1=visual.ImageStim(mywindow, image="cext_under3_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-16,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10.5,0],size=[3,3])
		if choice==13:
			img1=visual.ImageStim(mywindow, image="cext_over3_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15.5,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[3,3])
		if choice==14:
			img1=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-16,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10.5,0],size=[3,3])
		if choice==15:
			img1=visual.ImageStim(mywindow, image="cext_over3_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15.5,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[3,3])
		if choice==16:
			img1=visual.ImageStim(mywindow, image="cext_under3_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-16,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10.5,0],size=[3,3])
		if choice==17:
			img1=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[3,3])
		if choice==18:
			img1=visual.ImageStim(mywindow, image="cext_under3_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-16,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[11,0],size=[3,3])
		if choice==19:
			img1=visual.ImageStim(mywindow, image="cext_over2_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[3,3])
		if choice==20:
			img1=visual.ImageStim(mywindow, image="cext_under3_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-16,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[11,0],size=[3,3])
		if choice==21:
			img1=visual.ImageStim(mywindow, image="cext_over2_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[3,3])
		if choice==22:
			img1=visual.ImageStim(mywindow, image="cext_under3_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-16,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[11,0],size=[3,3])
		if choice==23:
			img1=visual.ImageStim(mywindow, image="cext_over2_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[3,3])
		if choice==24:
			img1=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-16,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[11,0],size=[3,3])
		if choice==25:
			img1=visual.ImageStim(mywindow, image="cext_over3_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15.5,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[11,0],size=[3,3])
		if choice==26:
			img1=visual.ImageStim(mywindow, image="cext_under2_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10.5,0],size=[3,3])
		if choice==27:
			img1=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15.5,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[11,0],size=[3,3])
		if choice==28:
			img1=visual.ImageStim(mywindow, image="cext_under2_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10.5,0],size=[3,3])
		if choice==29:
			img1=visual.ImageStim(mywindow, image="cext_over3_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15.5,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[11,0],size=[3,3])
		if choice==30:
			img1=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10.5,0],size=[3,3])
		if choice==31:
			img1=visual.ImageStim(mywindow, image="cext_over3_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15.5,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[11,0],size=[3,3])
		if choice==32:
			img1=visual.ImageStim(mywindow, image="cext_under2_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10.5,0],size=[3,3])
		if choice==33:
			img1=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[11,0],size=[2.5,2.5])
		if choice==34:
			img1=visual.ImageStim(mywindow, image="cext_under2_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[11,0],size=[2.5,2.5])
		if choice==35:
			img1=visual.ImageStim(mywindow, image="cext_over2_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[11,0],size=[2.5,2.5])
		if choice==36:
			img1=visual.ImageStim(mywindow, image="cext_under2_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[11,0],size=[2.5,2.5])
		if choice==37:
			img1=visual.ImageStim(mywindow, image="cext_over2_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[11,0],size=[2.5,2.5])
		if choice==38:
			img1=visual.ImageStim(mywindow, image="cext_under2_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[11,0],size=[2.5,2.5])
		if choice==39:
			img1=visual.ImageStim(mywindow, image="cext_over2_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[11,0],size=[2.5,2.5])
		if choice==40:
			img1=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[11,0],size=[2.5,2.5])
		if choice==41:
			img1=visual.ImageStim(mywindow, image="cext_over3_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15.5,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[2.5,2.5])
		if choice==42:
			img1=visual.ImageStim(mywindow, image="cext_under3_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-16,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10.5,0],size=[2.5,2.5])
		if choice==43:
			img1=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15.5,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2.5,2.5])
		if choice==44:
			img1=visual.ImageStim(mywindow, image="cext_under3_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-16,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10.5,0],size=[2.5,2.5])
		if choice==45:
			img1=visual.ImageStim(mywindow, image="cext_over3_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15.5,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[2.5,2.5])
		if choice==46:
			img1=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-16,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10.5,0],size=[2.5,2.5])
		if choice==47:
			img1=visual.ImageStim(mywindow, image="cext_over3_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15.5,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[2.5,2.5])
		if choice==48:
			img1=visual.ImageStim(mywindow, image="cext_under3_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-16,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10.5,0],size=[2.5,2.5])
		if choice==49:
			img1=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2.5,2.5])
		if choice==50:
			img1=visual.ImageStim(mywindow, image="cext_under3_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-16,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[11,0],size=[2.5,2.5])
		if choice==51:
			img1=visual.ImageStim(mywindow, image="cext_over2_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[2.5,2.5])
		if choice==52:
			img1=visual.ImageStim(mywindow, image="cext_under3_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-16,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[11,0],size=[2.5,2.5])
		if choice==53:
			img1=visual.ImageStim(mywindow, image="cext_over2_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[2.5,2.5])
		if choice==54:
			img1=visual.ImageStim(mywindow, image="cext_under3_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-16,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[11,0],size=[2.5,2.5])
		if choice==55:
			img1=visual.ImageStim(mywindow, image="cext_over2_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[2.5,2.5])
		if choice==56:
			img1=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-16,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[11,0],size=[2.5,2.5])
		if choice==57:
			img1=visual.ImageStim(mywindow, image="cext_over3_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15.5,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[11,0],size=[2.5,2.5])
		if choice==58:
			img1=visual.ImageStim(mywindow, image="cext_under2_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10.5,0],size=[2.5,2.5])
		if choice==59:
			img1=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15.5,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[11,0],size=[2.5,2.5])
		if choice==60:
			img1=visual.ImageStim(mywindow, image="cext_under2_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10.5,0],size=[2.5,2.5])
		if choice==61:
			img1=visual.ImageStim(mywindow, image="cext_over3_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15.5,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[11,0],size=[2.5,2.5])
		if choice==62:
			img1=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10.5,0],size=[2.5,2.5])
		if choice==63:
			img1=visual.ImageStim(mywindow, image="cext_over3_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15.5,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[11,0],size=[2.5,2.5])
		if choice==64:
			img1=visual.ImageStim(mywindow, image="cext_under2_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10.5,0],size=[2.5,2.5])
		if choice==65:
			img1=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[11,0],size=[2,2])
		if choice==66:
			img1=visual.ImageStim(mywindow, image="cext_under2_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[11,0],size=[2,2])
		if choice==67:
			img1=visual.ImageStim(mywindow, image="cext_over2_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[11,0],size=[2,2])
		if choice==68:
			img1=visual.ImageStim(mywindow, image="cext_under2_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[11,0],size=[2,2])
		if choice==69:
			img1=visual.ImageStim(mywindow, image="cext_over2_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[11,0],size=[2,2])
		if choice==70:
			img1=visual.ImageStim(mywindow, image="cext_under2_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[11,0],size=[2,2])
		if choice==71:
			img1=visual.ImageStim(mywindow, image="cext_over2_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[11,0],size=[2,2])
		if choice==72:
			img1=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[11,0],size=[2,2])
		if choice==73:
			img1=visual.ImageStim(mywindow, image="cext_over3_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15.5,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[2,2])
		if choice==74:
			img1=visual.ImageStim(mywindow, image="cext_under3_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-16,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10.5,0],size=[2,2])
		if choice==75:
			img1=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15.5,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2,2])
		if choice==76:
			img1=visual.ImageStim(mywindow, image="cext_under3_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-16,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10.5,0],size=[2,2])
		if choice==77:
			img1=visual.ImageStim(mywindow, image="cext_over3_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15.5,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[2,2])
		if choice==78:
			img1=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-16,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10.5,0],size=[2,2])
		if choice==79:
			img1=visual.ImageStim(mywindow, image="cext_over3_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15.5,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[2,2])
		if choice==80:
			img1=visual.ImageStim(mywindow, image="cext_under3_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-16,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10.5,0],size=[2,2])
		if choice==81:
			img1=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2,2])
		if choice==82:
			img1=visual.ImageStim(mywindow, image="cext_under3_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-16,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[11,0],size=[2,2])
		if choice==83:
			img1=visual.ImageStim(mywindow, image="cext_over2_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[2,2])
		if choice==84:
			img1=visual.ImageStim(mywindow, image="cext_under3_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-16,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[11,0],size=[2,2])
		if choice==85:
			img1=visual.ImageStim(mywindow, image="cext_over2_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[2,2])
		if choice==86:
			img1=visual.ImageStim(mywindow, image="cext_under3_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-16,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[11,0],size=[2,2])
		if choice==87:
			img1=visual.ImageStim(mywindow, image="cext_over2_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[2,2])
		if choice==88:
			img1=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-16,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[11,0],size=[2,2])
		if choice==89:
			img1=visual.ImageStim(mywindow, image="cext_over3_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15.5,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[11,0],size=[2,2])
		if choice==90:
			img1=visual.ImageStim(mywindow, image="cext_under2_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10.5,0],size=[2,2])
		if choice==91:
			img1=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15.5,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[11,0],size=[2,2])
		if choice==92:
			img1=visual.ImageStim(mywindow, image="cext_under2_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10.5,0],size=[2,2])
		if choice==93:
			img1=visual.ImageStim(mywindow, image="cext_over3_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15.5,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[11,0],size=[2,2])
		if choice==94:
			img1=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10.5,0],size=[2,2])
		if choice==95:
			img1=visual.ImageStim(mywindow, image="cext_over3_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15.5,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[11,0],size=[2,2])
		if choice==96:
			img1=visual.ImageStim(mywindow, image="cext_under2_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10.5,0],size=[2,2])
		if choice==97:
			img1=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[11,0],size=[1.5,1.5])
		if choice==98:
			img1=visual.ImageStim(mywindow, image="cext_under2_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[11,0],size=[1.5,1.5])
		if choice==99:
			img1=visual.ImageStim(mywindow, image="cext_over2_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[11,0],size=[1.5,1.5])
		if choice==100:
			img1=visual.ImageStim(mywindow, image="cext_under2_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[11,0],size=[1.5,1.5])
		if choice==101:
			img1=visual.ImageStim(mywindow, image="cext_over2_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[11,0],size=[1.5,1.5])
		if choice==102:
			img1=visual.ImageStim(mywindow, image="cext_under2_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[11,0],size=[1.5,1.5])
		if choice==103:
			img1=visual.ImageStim(mywindow, image="cext_over2_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[11,0],size=[1.5,1.5])
		if choice==104:
			img1=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[11,0],size=[1.5,1.5])
		if choice==105:
			img1=visual.ImageStim(mywindow, image="cext_over3_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15.5,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[1.5,1.5])
		if choice==106:
			img1=visual.ImageStim(mywindow, image="cext_under3_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-16,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10.5,0],size=[1.5,1.5])
		if choice==107:
			img1=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15.5,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1.5,1.5])
		if choice==108:
			img1=visual.ImageStim(mywindow, image="cext_under3_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-16,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10.5,0],size=[1.5,1.5])
		if choice==109:
			img1=visual.ImageStim(mywindow, image="cext_over3_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15.5,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[1.5,1.5])
		if choice==110:
			img1=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-16,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10.5,0],size=[1.5,1.5])
		if choice==111:
			img1=visual.ImageStim(mywindow, image="cext_over3_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15.5,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[1.5,1.5])
		if choice==112:
			img1=visual.ImageStim(mywindow, image="cext_under3_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-16,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10.5,0],size=[1.5,1.5])
		if choice==113:
			img1=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1.5,1.5])
		if choice==114:
			img1=visual.ImageStim(mywindow, image="cext_under3_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-16,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[11,0],size=[1.5,1.5])
		if choice==115:
			img1=visual.ImageStim(mywindow, image="cext_over2_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[1.5,1.5])
		if choice==116:
			img1=visual.ImageStim(mywindow, image="cext_under3_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-16,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[11,0],size=[1.5,1.5])
		if choice==117:
			img1=visual.ImageStim(mywindow, image="cext_over2_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[1.5,1.5])
		if choice==118:
			img1=visual.ImageStim(mywindow, image="cext_under3_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-16,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[11,0],size=[1.5,1.5])
		if choice==119:
			img1=visual.ImageStim(mywindow, image="cext_over2_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[1.5,1.5])
		if choice==120:
			img1=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-16,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[11,0],size=[1.5,1.5])
		if choice==121:
			img1=visual.ImageStim(mywindow, image="cext_over3_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15.5,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[11,0],size=[1.5,1.5])
		if choice==122:
			img1=visual.ImageStim(mywindow, image="cext_under2_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10.5,0],size=[1.5,1.5])
		if choice==123:
			img1=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15.5,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[11,0],size=[1.5,1.5])
		if choice==124:
			img1=visual.ImageStim(mywindow, image="cext_under2_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10.5,0],size=[1.5,1.5])
		if choice==125:
			img1=visual.ImageStim(mywindow, image="cext_over3_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15.5,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[11,0],size=[1.5,1.5])
		if choice==126:
			img1=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10.5,0],size=[1.5,1.5])
		if choice==127:
			img1=visual.ImageStim(mywindow, image="cext_over3_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15.5,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[11,0],size=[1.5,1.5])
		if choice==128:
			img1=visual.ImageStim(mywindow, image="cext_under2_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10.5,0],size=[1.5,1.5])
		if choice==129:
			img1=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[11,0],size=[1,1])
		if choice==130:
			img1=visual.ImageStim(mywindow, image="cext_under2_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[11,0],size=[1,1])
		if choice==131:
			img1=visual.ImageStim(mywindow, image="cext_over2_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[11,0],size=[1,1])
		if choice==132:
			img1=visual.ImageStim(mywindow, image="cext_under2_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[11,0],size=[1,1])
		if choice==133:
			img1=visual.ImageStim(mywindow, image="cext_over2_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[11,0],size=[1,1])
		if choice==134:
			img1=visual.ImageStim(mywindow, image="cext_under2_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[11,0],size=[1,1])
		if choice==135:
			img1=visual.ImageStim(mywindow, image="cext_over2_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[11,0],size=[1,1])
		if choice==136:
			img1=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[11,0],size=[1,1])
		if choice==137:
			img1=visual.ImageStim(mywindow, image="cext_over3_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15.5,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[1,1])
		if choice==138:
			img1=visual.ImageStim(mywindow, image="cext_under3_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-16,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10.5,0],size=[1,1])
		if choice==139:
			img1=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15.5,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1,1])
		if choice==140:
			img1=visual.ImageStim(mywindow, image="cext_under3_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-16,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10.5,0],size=[1,1])
		if choice==141:
			img1=visual.ImageStim(mywindow, image="cext_over3_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15.5,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[1,1])
		if choice==142:
			img1=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-16,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10.5,0],size=[1,1])
		if choice==143:
			img1=visual.ImageStim(mywindow, image="cext_over3_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15.5,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[1,1])
		if choice==144:
			img1=visual.ImageStim(mywindow, image="cext_under3_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-16,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10.5,0],size=[1,1])
		if choice==145:
			img1=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1,1])
		if choice==146:
			img1=visual.ImageStim(mywindow, image="cext_under3_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-16,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[11,0],size=[1,1])
		if choice==147:
			img1=visual.ImageStim(mywindow, image="cext_over2_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[1,1])
		if choice==148:
			img1=visual.ImageStim(mywindow, image="cext_under3_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-16,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[11,0],size=[1,1])
		if choice==149:
			img1=visual.ImageStim(mywindow, image="cext_over2_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[1,1])
		if choice==150:
			img1=visual.ImageStim(mywindow, image="cext_under3_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-16,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[11,0],size=[1,1])
		if choice==151:
			img1=visual.ImageStim(mywindow, image="cext_over2_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[1,1])
		if choice==152:
			img1=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-16,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[11,0],size=[1,1])
		if choice==153:
			img1=visual.ImageStim(mywindow, image="cext_over3_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15.5,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[11,0],size=[1,1])
		if choice==154:
			img1=visual.ImageStim(mywindow, image="cext_under2_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10.5,0],size=[1,1])
		if choice==155:
			img1=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15.5,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[11,0],size=[1,1])
		if choice==156:
			img1=visual.ImageStim(mywindow, image="cext_under2_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10.5,0],size=[1,1])
		if choice==157:
			img1=visual.ImageStim(mywindow, image="cext_over3_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15.5,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[11,0],size=[1,1])
		if choice==158:
			img1=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10.5,0],size=[1,1])
		if choice==159:
			img1=visual.ImageStim(mywindow, image="cext_over3_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15.5,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[11,0],size=[1,1])
		if choice==160:
			img1=visual.ImageStim(mywindow, image="cext_under2_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10.5,0],size=[1,1])
		if choice==161:
			img1=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[11,0],size=[3,3])
		if choice==162:
			img1=visual.ImageStim(mywindow, image="cext_under2_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[11,0],size=[2.5,2.5])
		if choice==163:
			img1=visual.ImageStim(mywindow, image="cext_over2_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[11,0],size=[3,3])
		if choice==164:
			img1=visual.ImageStim(mywindow, image="cext_under2_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[11,0],size=[2.5,2.5])
		if choice==165:
			img1=visual.ImageStim(mywindow, image="cext_over2_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[11,0],size=[2.5,2.5])
		if choice==166:
			img1=visual.ImageStim(mywindow, image="cext_under2_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[11,0],size=[3,3])
		if choice==167:
			img1=visual.ImageStim(mywindow, image="cext_over2_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[11,0],size=[2.5,2.5])
		if choice==168:
			img1=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[11,0],size=[3,3])
		if choice==169:
			img1=visual.ImageStim(mywindow, image="cext_over3_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15.5,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[3,3])
		if choice==170:
			img1=visual.ImageStim(mywindow, image="cext_under3_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-16,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10.5,0],size=[2.5,2.5])
		if choice==171:
			img1=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15.5,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[3,3])
		if choice==172:
			img1=visual.ImageStim(mywindow, image="cext_under3_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-16,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10.5,0],size=[2.5,2.5])
		if choice==173:
			img1=visual.ImageStim(mywindow, image="cext_over3_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15.5,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[2.5,2.5])
		if choice==174:
			img1=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-16,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10.5,0],size=[3,3])
		if choice==175:
			img1=visual.ImageStim(mywindow, image="cext_over3_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15.5,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[2.5,2.5])
		if choice==176:
			img1=visual.ImageStim(mywindow, image="cext_under3_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-16,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10.5,0],size=[3,3])
		if choice==177:
			img1=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[3,3])
		if choice==178:
			img1=visual.ImageStim(mywindow, image="cext_under3_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-16,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[11,0],size=[2.5,2.5])
		if choice==179:
			img1=visual.ImageStim(mywindow, image="cext_over2_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[3,3])
		if choice==180:
			img1=visual.ImageStim(mywindow, image="cext_under3_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-16,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[11,0],size=[2.5,2.5])
		if choice==181:
			img1=visual.ImageStim(mywindow, image="cext_over2_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[2.5,2.5])
		if choice==182:
			img1=visual.ImageStim(mywindow, image="cext_under3_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-16,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[11,0],size=[3,3])
		if choice==183:
			img1=visual.ImageStim(mywindow, image="cext_over2_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[2.5,2.5])
		if choice==184:
			img1=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-16,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[11,0],size=[3,3])
		if choice==185:
			img1=visual.ImageStim(mywindow, image="cext_over3_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15.5,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[11,0],size=[3,3])
		if choice==186:
			img1=visual.ImageStim(mywindow, image="cext_under2_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10.5,0],size=[2.5,2.5])
		if choice==187:
			img1=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15.5,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[11,0],size=[3,3])
		if choice==188:
			img1=visual.ImageStim(mywindow, image="cext_under2_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10.5,0],size=[2.5,2.5])
		if choice==189:
			img1=visual.ImageStim(mywindow, image="cext_over3_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15.5,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[11,0],size=[2.5,2.5])
		if choice==190:
			img1=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10.5,0],size=[3,3])
		if choice==191:
			img1=visual.ImageStim(mywindow, image="cext_over3_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15.5,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[11,0],size=[2.5,2.5])
		if choice==192:
			img1=visual.ImageStim(mywindow, image="cext_under2_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10.5,0],size=[3,3])
		if choice==193:
			img1=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[11,0],size=[2.5,2.5])
		if choice==194:
			img1=visual.ImageStim(mywindow, image="cext_under2_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[11,0],size=[2,2])
		if choice==195:
			img1=visual.ImageStim(mywindow, image="cext_over2_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[11,0],size=[2.5,2.5])
		if choice==196:
			img1=visual.ImageStim(mywindow, image="cext_under2_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[11,0],size=[2,2])
		if choice==197:
			img1=visual.ImageStim(mywindow, image="cext_over2_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[11,0],size=[2,2])
		if choice==198:
			img1=visual.ImageStim(mywindow, image="cext_under2_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[11,0],size=[2.5,2.5])
		if choice==199:
			img1=visual.ImageStim(mywindow, image="cext_over2_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[11,0],size=[2,2])
		if choice==200:
			img1=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[11,0],size=[2.5,2.5])
		if choice==201:
			img1=visual.ImageStim(mywindow, image="cext_over3_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15.5,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[2.5,2.5])
		if choice==202:
			img1=visual.ImageStim(mywindow, image="cext_under3_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-16,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10.5,0],size=[2,2])
		if choice==203:
			img1=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15.5,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2.5,2.5])
		if choice==204:
			img1=visual.ImageStim(mywindow, image="cext_under3_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-16,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10.5,0],size=[2,2])
		if choice==205:
			img1=visual.ImageStim(mywindow, image="cext_over3_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15.5,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[2,2])
		if choice==206:
			img1=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-16,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10.5,0],size=[2.5,2.5])
		if choice==207:
			img1=visual.ImageStim(mywindow, image="cext_over3_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15.5,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[2,2])
		if choice==208:
			img1=visual.ImageStim(mywindow, image="cext_under3_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-16,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10.5,0],size=[2.5,2.5])
		if choice==209:
			img1=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2.5,2.5])
		if choice==210:
			img1=visual.ImageStim(mywindow, image="cext_under3_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-16,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[11,0],size=[2,2])
		if choice==211:
			img1=visual.ImageStim(mywindow, image="cext_over2_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[2.5,2.5])
		if choice==212:
			img1=visual.ImageStim(mywindow, image="cext_under3_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-16,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[11,0],size=[2,2])
		if choice==213:
			img1=visual.ImageStim(mywindow, image="cext_over2_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[2,2])
		if choice==214:
			img1=visual.ImageStim(mywindow, image="cext_under3_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-16,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[11,0],size=[2.5,2.5])
		if choice==215:
			img1=visual.ImageStim(mywindow, image="cext_over2_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[2,2])
		if choice==216:
			img1=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-16,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[11,0],size=[2.5,2.5])
		if choice==217:
			img1=visual.ImageStim(mywindow, image="cext_over3_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15.5,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[11,0],size=[2.5,2.5])
		if choice==218:
			img1=visual.ImageStim(mywindow, image="cext_under2_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10.5,0],size=[2,2])
		if choice==219:
			img1=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15.5,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[11,0],size=[2.5,2.5])
		if choice==220:
			img1=visual.ImageStim(mywindow, image="cext_under2_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10.5,0],size=[2,2])
		if choice==221:
			img1=visual.ImageStim(mywindow, image="cext_over3_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15.5,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[11,0],size=[2,2])
		if choice==222:
			img1=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10.5,0],size=[2.5,2.5])
		if choice==223:
			img1=visual.ImageStim(mywindow, image="cext_over3_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15.5,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[11,0],size=[2,2])
		if choice==224:
			img1=visual.ImageStim(mywindow, image="cext_under2_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10.5,0],size=[2.5,2.5])
		if choice==225:
			img1=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[11,0],size=[2,2])
		if choice==226:
			img1=visual.ImageStim(mywindow, image="cext_under2_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[11,0],size=[1.5,1.5])
		if choice==227:
			img1=visual.ImageStim(mywindow, image="cext_over2_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[11,0],size=[2,2])
		if choice==228:
			img1=visual.ImageStim(mywindow, image="cext_under2_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[11,0],size=[1.5,1.5])
		if choice==229:
			img1=visual.ImageStim(mywindow, image="cext_over2_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[11,0],size=[1.5,1.5])
		if choice==230:
			img1=visual.ImageStim(mywindow, image="cext_under2_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[11,0],size=[2,2])
		if choice==231:
			img1=visual.ImageStim(mywindow, image="cext_over2_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[11,0],size=[1.5,1.5])
		if choice==232:
			img1=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[11,0],size=[2,2])
		if choice==233:
			img1=visual.ImageStim(mywindow, image="cext_over3_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15.5,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[2,2])
		if choice==234:
			img1=visual.ImageStim(mywindow, image="cext_under3_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-16,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10.5,0],size=[1.5,1.5])
		if choice==235:
			img1=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15.5,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2,2])
		if choice==236:
			img1=visual.ImageStim(mywindow, image="cext_under3_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-16,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10.5,0],size=[1.5,1.5])
		if choice==237:
			img1=visual.ImageStim(mywindow, image="cext_over3_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15.5,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[1.5,1.5])
		if choice==238:
			img1=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-16,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10.5,0],size=[2,2])
		if choice==239:
			img1=visual.ImageStim(mywindow, image="cext_over3_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15.5,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[1.5,1.5])
		if choice==240:
			img1=visual.ImageStim(mywindow, image="cext_under3_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-16.7,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10.5,0],size=[2,2])
		if choice==241:
			img1=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2,2])
		if choice==242:
			img1=visual.ImageStim(mywindow, image="cext_under3_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-16,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[11,0],size=[1.5,1.5])
		if choice==343:
			img1=visual.ImageStim(mywindow, image="cext_over2_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[2,2])
		if choice==244:
			img1=visual.ImageStim(mywindow, image="cext_under3_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-16,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[11,0],size=[1.5,1.5])
		if choice==245:
			img1=visual.ImageStim(mywindow, image="cext_over2_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[1.5,1.5])
		if choice==246:
			img1=visual.ImageStim(mywindow, image="cext_under3_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-16,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[11,0],size=[2,2])
		if choice==247:
			img1=visual.ImageStim(mywindow, image="cext_over2_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[1.5,1.5])
		if choice==248:
			img1=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-16,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[11,0],size=[2,2])
		if choice==249:
			img1=visual.ImageStim(mywindow, image="cext_over3_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15.5,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[11,0],size=[2,2])
		if choice==250:
			img1=visual.ImageStim(mywindow, image="cext_under3_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-16,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[11,0],size=[1.5,1.5])
		if choice==251:
			img1=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15.5,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[11,0],size=[2,2])
		if choice==252:
			img1=visual.ImageStim(mywindow, image="cext_under2_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10.5,0],size=[1.5,1.5])
		if choice==253:
			img1=visual.ImageStim(mywindow, image="cext_over3_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15.5,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[11,0],size=[1.5,1.5])
		if choice==254:
			img1=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10.5,0],size=[2,2])
		if choice==255:
			img1=visual.ImageStim(mywindow, image="cext_over3_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15.5,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[11,0],size=[1.5,1.5])
		if choice==256:
			img1=visual.ImageStim(mywindow, image="cext_under2_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10.5,0],size=[2,2])
		if choice==257:
			img1=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[11,0],size=[1.5,1.5])
		if choice==258:
			img1=visual.ImageStim(mywindow, image="cext_under2_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[11,0],size=[1,1])
		if choice==259:
			img1=visual.ImageStim(mywindow, image="cext_over2_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[11,0],size=[1.5,1.5])
		if choice==260:
			img1=visual.ImageStim(mywindow, image="cext_under2_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[11,0],size=[1,1])
		if choice==261:
			img1=visual.ImageStim(mywindow, image="cext_over2_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[11,0],size=[1,1])
		if choice==262:
			img1=visual.ImageStim(mywindow, image="cext_under2_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[11,0],size=[1.5,1.5])
		if choice==263:
			img1=visual.ImageStim(mywindow, image="cext_over2_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[11,0],size=[1,1])
		if choice==264:
			img1=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[11,0],size=[1.5,1.5])
		if choice==265:
			img1=visual.ImageStim(mywindow, image="cext_over3_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15.5,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[1.5,1.5])
		if choice==266:
			img1=visual.ImageStim(mywindow, image="cext_under3_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-16,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10.5,0],size=[1,1])
		if choice==267:
			img1=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15.5,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1.5,1.5])
		if choice==268:
			img1=visual.ImageStim(mywindow, image="cext_under3_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-16,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10.5,0],size=[1,1])
		if choice==269:
			img1=visual.ImageStim(mywindow, image="cext_over3_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15.5,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[1,1])
		if choice==270:
			img1=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-16,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10.5,0],size=[1.5,1.5])
		if choice==271:
			img1=visual.ImageStim(mywindow, image="cext_over3_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15.5,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[1,1])
		if choice==272:
			img1=visual.ImageStim(mywindow, image="cext_under3_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-16,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10.5,0],size=[1.5,1.5])
		if choice==273:
			img1=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1.5,1.5])
		if choice==274:
			img1=visual.ImageStim(mywindow, image="cext_under3_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-16,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[11,0],size=[1,1])
		if choice==275:
			img1=visual.ImageStim(mywindow, image="cext_over2_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[1.5,1.5])
		if choice==276:
			img1=visual.ImageStim(mywindow, image="cext_under3_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-16,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[11,0],size=[1,1])
		if choice==277:
			img1=visual.ImageStim(mywindow, image="cext_over2_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[1,1])
		if choice==278:
			img1=visual.ImageStim(mywindow, image="cext_under3_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-16,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[11,0],size=[1.5,1.5])
		if choice==279:
			img1=visual.ImageStim(mywindow, image="cext_over2_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[1,1])
		if choice==280:
			img1=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-16,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[11,0],size=[1.5,1.5])
		if choice==281:
			img1=visual.ImageStim(mywindow, image="cext_over3_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15.5,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[11,0],size=[1.5,1.5])
		if choice==282:
			img1=visual.ImageStim(mywindow, image="cext_under2_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10.5,0],size=[1,1])
		if choice==283:
			img1=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15.5,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[11,0],size=[1.5,1.5])
		if choice==284:
			img1=visual.ImageStim(mywindow, image="cext_under2_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10.5,0],size=[1,1])
		if choice==285:
			img1=visual.ImageStim(mywindow, image="cext_over3_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15.5,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[11,0],size=[1,1])
		if choice==286:
			img1=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10.5,0],size=[1.5,1.5])
		if choice==287:
			img1=visual.ImageStim(mywindow, image="cext_over3_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15.5,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[11,0],size=[1,1])
		if choice==288:
			img1=visual.ImageStim(mywindow, image="cext_under2_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10.5,0],size=[1.5,1.5])
		if choice==289:
			img1=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[11,0],size=[2.5,2.5])
		if choice==290:
			img1=visual.ImageStim(mywindow, image="cext_under2_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[11,0],size=[1.5,1.5])
		if choice==291:
			img1=visual.ImageStim(mywindow, image="cext_over2_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[11,0],size=[2.5,2.5])
		if choice==292:
			img1=visual.ImageStim(mywindow, image="cext_under2_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[11,0],size=[1.5,1.5])
		if choice==293:
			img1=visual.ImageStim(mywindow, image="cext_over2_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[11,0],size=[1.5,1.5])
		if choice==294:
			img1=visual.ImageStim(mywindow, image="cext_under2_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[11,0],size=[2.5,2.5])
		if choice==295:
			img1=visual.ImageStim(mywindow, image="cext_over2_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[11,0],size=[1.5,1.5])
		if choice==296:
			img1=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[11,0],size=[2.5,2.5])
		if choice==297:
			img1=visual.ImageStim(mywindow, image="cext_over3_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15.5,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[2.5,2.5])
		if choice==298:
			img1=visual.ImageStim(mywindow, image="cext_under3_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-16,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10.5,0],size=[1.5,1.5])
		if choice==299:
			img1=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15.5,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2.5,2.5])
		if choice==300:
			img1=visual.ImageStim(mywindow, image="cext_under3_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-16,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10.5,0],size=[1.5,1.5])
		if choice==301:
			img1=visual.ImageStim(mywindow, image="cext_over3_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15.5,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[1.5,1.5])
		if choice==302:
			img1=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-16,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10.5,0],size=[2.5,2.5])
		if choice==303:
			img1=visual.ImageStim(mywindow, image="cext_over3_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15.5,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10,0],size=[1.5,1.5])
		if choice==304:
			img1=visual.ImageStim(mywindow, image="cext_under3_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-16,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10.5,0],size=[2.5,2.5])
		if choice==305:
			img1=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[2.5,2.5])
		if choice==306:
			img1=visual.ImageStim(mywindow, image="cext_under3_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-16,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[11,0],size=[1.5,1.5])
		if choice==307:
			img1=visual.ImageStim(mywindow, image="cext_over2_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10,0],size=[2.5,2.5])
		if choice==308:
			img1=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-16,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[11,0],size=[1.5,1.5])
		if choice==309:
			img1=visual.ImageStim(mywindow, image="cext_over2_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10,0],size=[1.5,1.5])
		if choice==310:
			img1=visual.ImageStim(mywindow, image="cext_under3_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-16,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[11,0],size=[2.5,2.5])
		if choice==311:
			img1=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10,0],size=[1.5,1.5])
		if choice==312:
			img1=visual.ImageStim(mywindow, image="cext_under3_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over2_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-16,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[11,0],size=[2.5,2.5])
		if choice==313:
			img1=visual.ImageStim(mywindow, image="cext_over3_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15.5,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[11,0],size=[2.5,2.5])
		if choice==314:
			img1=visual.ImageStim(mywindow, image="cext_under2_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10.5,0],size=[1.5,1.5])
		if choice==315:
			img1=visual.ImageStim(mywindow, image="cext_over3_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15.5,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[11,0],size=[2.5,2.5])
		if choice==316:
			img1=visual.ImageStim(mywindow, image="cext_under2_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10.5,0],size=[1.5,1.5])
		if choice==317:
			img1=visual.ImageStim(mywindow, image="cext_over3_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15.5,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[11,0],size=[1.5,1.5])
		if choice==318:
			img1=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10.5,0],size=[2.5,2.5])
		if choice==319:
			img1=visual.ImageStim(mywindow, image="cext_over3_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under2_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15.5,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[11,0],size=[1.5,1.5])
		if choice==320:
			img1=visual.ImageStim(mywindow, image="cext_under2_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over3_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10.5,0],size=[2.5,2.5])
		if choice==321:
			img1=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10.5,0],size=[3,3])
		if choice==322:
			img1=visual.ImageStim(mywindow, image="cext_under7_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15.5,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[11,0],size=[3,3])
		if choice==323:
			img1=visual.ImageStim(mywindow, image="cext_over7_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10.5,0],size=[3,3])
		if choice==324:
			img1=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15.5,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[11,0],size=[3,3])
		if choice==325:
			img1=visual.ImageStim(mywindow, image="cext_over7_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10.5,0],size=[3,3])
		if choice==326:
			img1=visual.ImageStim(mywindow, image="cext_under7_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15.5,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[11,0],size=[3,3])
		if choice==327:
			img1=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10.5,0],size=[3,3])
		if choice==328:
			img1=visual.ImageStim(mywindow, image="cext_under7_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15.5,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[11,0],size=[3,3])
		if choice==329:
			img1=visual.ImageStim(mywindow, image="cext_over8_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[11,0],size=[3,3])
		if choice==330:
			img1=visual.ImageStim(mywindow, image="cext_under8_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[11,0],size=[3,3])
		if choice==331:
			img1=visual.ImageStim(mywindow, image="cext_over8_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[11,0],size=[3,3])
		if choice==332:
			img1=visual.ImageStim(mywindow, image="cext_under8_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[11,0],size=[3,3])
		if choice==333:
			img1=visual.ImageStim(mywindow, image="cext_over8_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[11,0],size=[3,3])
		if choice==334:
			img1=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[11,0],size=[3,3])
		if choice==335:
			img1=visual.ImageStim(mywindow, image="cext_over8_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[11,0],size=[3,3])
		if choice==336:
			img1=visual.ImageStim(mywindow, image="cext_under8_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[11,0],size=[3,3])
		if choice==337:
			img1=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[11,0],size=[3,3])
		if choice==338:
			img1=visual.ImageStim(mywindow, image="cext_under8_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[11,0],size=[3,3])
		if choice==339:
			img1=visual.ImageStim(mywindow, image="cext_over7_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[11,0],size=[3,3])
		if choice==340:
			img1=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[11,0],size=[3,3])
		if choice==341:
			img1=visual.ImageStim(mywindow, image="cext_over7_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[11,0],size=[3,3])
		if choice==342:
			img1=visual.ImageStim(mywindow, image="cext_under8_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[11,0],size=[3,3])
		if choice==343:
			img1=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[11,0],size=[3,3])
		if choice==344:
			img1=visual.ImageStim(mywindow, image="cext_under8_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[11,0],size=[3,3])
		if choice==345:
			img1=visual.ImageStim(mywindow, image="cext_over8_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10.5,0],size=[3,3])
		if choice==346:
			img1=visual.ImageStim(mywindow, image="cext_under7_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15.5,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[11,0],size=[3,3])
		if choice==347:
			img1=visual.ImageStim(mywindow, image="cext_over8_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10.5,0],size=[3,3])
		if choice==348:
			img1=visual.ImageStim(mywindow, image="cext_under7_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15.5,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[11,0],size=[3,3])
		if choice==349:
			img1=visual.ImageStim(mywindow, image="cext_over8_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10.5,0],size=[3,3])
		if choice==350:
			img1=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15.5,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[11,0],size=[3,3])
		if choice==351:
			img1=visual.ImageStim(mywindow, image="cext_over8_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10.5,0],size=[3,3])
		if choice==352:
			img1=visual.ImageStim(mywindow, image="cext_under7_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15.5,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[11,0],size=[3,3])
		if choice==353:
			img1=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10.5,0],size=[2.5,2.5])
		if choice==354:
			img1=visual.ImageStim(mywindow, image="cext_under7_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15.5,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[11,0],size=[2.5,2.5])
		if choice==355:
			img1=visual.ImageStim(mywindow, image="cext_over7_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10.5,0],size=[2.5,2.5])
		if choice==356:
			img1=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15.5,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[11,0],size=[2.5,2.5])
		if choice==357:
			img1=visual.ImageStim(mywindow, image="cext_over7_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10.5,0],size=[2.5,2.5])
		if choice==358:
			img1=visual.ImageStim(mywindow, image="cext_under7_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15.5,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[11,0],size=[2.5,2.5])
		if choice==359:
			img1=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10.5,0],size=[2.5,2.5])
		if choice==360:
			img1=visual.ImageStim(mywindow, image="cext_under7_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15.5,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[11,0],size=[2.5,2.5])
		if choice==361:
			img1=visual.ImageStim(mywindow, image="cext_over8_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[11,0],size=[2.5,2.5])
		if choice==362:
			img1=visual.ImageStim(mywindow, image="cext_under8_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[11,0],size=[2.5,2.5])
		if choice==363:
			img1=visual.ImageStim(mywindow, image="cext_over8_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[11,0],size=[2.5,2.5])
		if choice==364:
			img1=visual.ImageStim(mywindow, image="cext_under8_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[11,0],size=[2.5,2.5])
		if choice==365:
			img1=visual.ImageStim(mywindow, image="cext_over8_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[11,0],size=[2.5,2.5])
		if choice==366:
			img1=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[11,0],size=[2.5,2.5])
		if choice==367:
			img1=visual.ImageStim(mywindow, image="cext_over8_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[11,0],size=[2.5,2.5])
		if choice==368:
			img1=visual.ImageStim(mywindow, image="cext_under8_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[11,0],size=[2.5,2.5])
		if choice==369:
			img1=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[11,0],size=[2.5,2.5])
		if choice==370:
			img1=visual.ImageStim(mywindow, image="cext_under8_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[11,0],size=[2.5,2.5])
		if choice==371:
			img1=visual.ImageStim(mywindow, image="cext_over7_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[11,0],size=[2.5,2.5])
		if choice==372:
			img1=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[11,0],size=[2.5,2.5])
		if choice==373:
			img1=visual.ImageStim(mywindow, image="cext_over7_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[11,0],size=[2.5,2.5])
		if choice==374:
			img1=visual.ImageStim(mywindow, image="cext_under8_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[11,0],size=[2.5,2.5])
		if choice==375:
			img1=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[11,0],size=[2.5,2.5])
		if choice==376:
			img1=visual.ImageStim(mywindow, image="cext_under8_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[11,0],size=[2.5,2.5])
		if choice==377:
			img1=visual.ImageStim(mywindow, image="cext_over8_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10.5,0],size=[2.5,2.5])
		if choice==378:
			img1=visual.ImageStim(mywindow, image="cext_under7_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15.5,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[11,0],size=[2.5,2.5])
		if choice==379:
			img1=visual.ImageStim(mywindow, image="cext_over8_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10.5,0],size=[2.5,2.5])
		if choice==380:
			img1=visual.ImageStim(mywindow, image="cext_under7_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15.5,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[11,0],size=[2.5,2.5])
		if choice==381:
			img1=visual.ImageStim(mywindow, image="cext_over8_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10.5,0],size=[2.5,2.5])
		if choice==382:
			img1=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15.5,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[11,0],size=[2.5,2.5])
		if choice==383:
			img1=visual.ImageStim(mywindow, image="cext_over8_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10.5,0],size=[2.5,2.5])
		if choice==384:
			img1=visual.ImageStim(mywindow, image="cext_under7_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15.5,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[11,0],size=[2.5,2.5])
		if choice==385:
			img1=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10.5,0],size=[2,2])
		if choice==386:
			img1=visual.ImageStim(mywindow, image="cext_under7_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15.5,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[11,0],size=[2,2])
		if choice==387:
			img1=visual.ImageStim(mywindow, image="cext_over7_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10.5,0],size=[2,2])
		if choice==388:
			img1=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15.5,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[11,0],size=[2,2])
		if choice==389:
			img1=visual.ImageStim(mywindow, image="cext_over7_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10.5,0],size=[2,2])
		if choice==390:
			img1=visual.ImageStim(mywindow, image="cext_under7_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15.5,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[11,0],size=[2,2])
		if choice==391:
			img1=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10.5,0],size=[2,2])
		if choice==392:
			img1=visual.ImageStim(mywindow, image="cext_under7_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15.5,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[11,0],size=[2,2])
		if choice==393:
			img1=visual.ImageStim(mywindow, image="cext_over8_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[11,0],size=[2,2])
		if choice==394:
			img1=visual.ImageStim(mywindow, image="cext_under8_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[11,0],size=[2,2])
		if choice==395:
			img1=visual.ImageStim(mywindow, image="cext_over8_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[11,0],size=[2,2])
		if choice==396:
			img1=visual.ImageStim(mywindow, image="cext_under8_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[11,0],size=[2,2])
		if choice==397:
			img1=visual.ImageStim(mywindow, image="cext_over8_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[11,0],size=[2,2])
		if choice==398:
			img1=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[11,0],size=[2,2])
		if choice==399:
			img1=visual.ImageStim(mywindow, image="cext_over8_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[11,0],size=[2,2])
		if choice==400:
			img1=visual.ImageStim(mywindow, image="cext_under8_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[11,0],size=[2,2])
		if choice==401:
			img1=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[11,0],size=[2,2])
		if choice==402:
			img1=visual.ImageStim(mywindow, image="cext_under8_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[11,0],size=[2,2])
		if choice==403:
			img1=visual.ImageStim(mywindow, image="cext_over7_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[11,0],size=[2,2])
		if choice==404:
			img1=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[11,0],size=[2,2])
		if choice==405:
			img1=visual.ImageStim(mywindow, image="cext_over7_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[11,0],size=[2,2])
		if choice==406:
			img1=visual.ImageStim(mywindow, image="cext_under8_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[11,0],size=[2,2])
		if choice==407:
			img1=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[11,0],size=[2,2])
		if choice==408:
			img1=visual.ImageStim(mywindow, image="cext_under8_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[11,0],size=[2,2])
		if choice==409:
			img1=visual.ImageStim(mywindow, image="cext_over8_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10.5,0],size=[2,2])
		if choice==410:
			img1=visual.ImageStim(mywindow, image="cext_under7_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15.5,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[11,0],size=[2,2])
		if choice==411:
			img1=visual.ImageStim(mywindow, image="cext_over8_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10.5,0],size=[2,2])
		if choice==412:
			img1=visual.ImageStim(mywindow, image="cext_under7_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15.5,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[11,0],size=[2,2])
		if choice==413:
			img1=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10.5,0],size=[2,2])
		if choice==414:
			img1=visual.ImageStim(mywindow, image="cext_under7_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15.5,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[11,0],size=[2,2])
		if choice==415:
			img1=visual.ImageStim(mywindow, image="cext_over8_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10.5,0],size=[2,2])
		if choice==416:
			img1=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15.5,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[11,0],size=[2,2])
		if choice==417:
			img1=visual.ImageStim(mywindow, image="cext_over7_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,-.3],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10.5,0],size=[1.5,1.5])
		if choice==418:
			img1=visual.ImageStim(mywindow, image="cext_under7_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15.5,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[11,-.3],size=[1.5,1.5])
		if choice==419:
			img1=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,-.3],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10.5,0],size=[1.5,1.5])
		if choice==420:
			img1=visual.ImageStim(mywindow, image="cext_under7_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15.5,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[11,-.3],size=[1.5,1.5])
		if choice==421:
			img1=visual.ImageStim(mywindow, image="cext_over7_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,-.3],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10.5,0],size=[1.5,1.5])
		if choice==422:
			img1=visual.ImageStim(mywindow, image="cext_under7_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15.5,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[11,-.3],size=[1.5,1.5])
		if choice==423:
			img1=visual.ImageStim(mywindow, image="cext_over7_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,-.3],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10.5,0],size=[1.5,1.5])
		if choice==424:
			img1=visual.ImageStim(mywindow, image="cext_under7_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15.5,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[11,-.3],size=[1.5,1.5])
		if choice==425:
			img1=visual.ImageStim(mywindow, image="cext_over8_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[11,0],size=[1.5,1.5])
		if choice==426:
			img1=visual.ImageStim(mywindow, image="cext_under8_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[11,0],size=[1.5,1.5])
		if choice==427:
			img1=visual.ImageStim(mywindow, image="cext_over8_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[11,0],size=[1.5,1.5])
		if choice==428:
			img1=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[11,0],size=[1.5,1.5])
		if choice==429:
			img1=visual.ImageStim(mywindow, image="cext_over8_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[11,0],size=[1.5,1.5])
		if choice==430:
			img1=visual.ImageStim(mywindow, image="cext_under8_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[11,0],size=[1.5,1.5])
		if choice==431:
			img1=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[11,0],size=[1.5,1.5])
		if choice==432:
			img1=visual.ImageStim(mywindow, image="cext_under8_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[11,0],size=[1.5,1.5])
		if choice==433:
			img1=visual.ImageStim(mywindow, image="cext_over7_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[11,0],size=[1.5,1.5])
		if choice==434:
			img1=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[11,0],size=[1.5,1.5])
		if choice==435:
			img1=visual.ImageStim(mywindow, image="cext_over7_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[11,0],size=[1.5,1.5])
		if choice==436:
			img1=visual.ImageStim(mywindow, image="cext_under8_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[11,0],size=[1.5,1.5])
		if choice==437:
			img1=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[11,0],size=[1.5,1.5])
		if choice==438:
			img1=visual.ImageStim(mywindow, image="cext_under8_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[11,0],size=[1.5,1.5])
		if choice==439:
			img1=visual.ImageStim(mywindow, image="cext_over7_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[11,0],size=[1.5,1.5])
		if choice==440:
			img1=visual.ImageStim(mywindow, image="cext_under8_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[11,0],size=[1.5,1.5])
		if choice==441:
			img1=visual.ImageStim(mywindow, image="cext_over8_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10.5,0],size=[1.5,1.5])
		if choice==442:
			img1=visual.ImageStim(mywindow, image="cext_under7_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15.5,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[11,0],size=[1.5,1.5])
		if choice==443:
			img1=visual.ImageStim(mywindow, image="cext_over8_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10.5,0],size=[1.5,1.5])
		if choice==444:
			img1=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15.5,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[11,0],size=[1.5,1.5])
		if choice==445:
			img1=visual.ImageStim(mywindow, image="cext_over8_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10.5,0],size=[1.5,1.5])
		if choice==446:
			img1=visual.ImageStim(mywindow, image="cext_under7_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15.5,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[11,0],size=[1.5,1.5])
		if choice==447:
			img1=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10.5,0],size=[1.5,1.5])
		if choice==448:
			img1=visual.ImageStim(mywindow, image="cext_under7_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15.5,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[11,0],size=[1.5,1.5])
		if choice==449:
			img1=visual.ImageStim(mywindow, image="cext_over7_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10.5,0],size=[1,1])
		if choice==450:
			img1=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15.5,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[11,0],size=[1,1])
		if choice==451:
			img1=visual.ImageStim(mywindow, image="cext_over7_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10.5,0],size=[1,1])
		if choice==452:
			img1=visual.ImageStim(mywindow, image="cext_under7_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15.5,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[11,0],size=[1,1])
		if choice==453:
			img1=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10.5,0],size=[1,1])
		if choice==454:
			img1=visual.ImageStim(mywindow, image="cext_under7_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15.5,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[11,0],size=[1,1])
		if choice==455:
			img1=visual.ImageStim(mywindow, image="cext_over7_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10.5,0],size=[1,1])
		if choice==456:
			img1=visual.ImageStim(mywindow, image="cext_under7_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15.5,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[11,0],size=[1,1])
		if choice==457:
			img1=visual.ImageStim(mywindow, image="cext_over8_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[11,0],size=[1,1])
		if choice==458:
			img1=visual.ImageStim(mywindow, image="cext_under8_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[11,0],size=[1,1])
		if choice==459:
			img1=visual.ImageStim(mywindow, image="cext_over8_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[11,0],size=[1,1])
		if choice==460:
			img1=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[11,0],size=[1,1])
		if choice==461:
			img1=visual.ImageStim(mywindow, image="cext_over8_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[11,0],size=[1,1])
		if choice==462:
			img1=visual.ImageStim(mywindow, image="cext_under8_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[11,0],size=[1,1])
		if choice==463:
			img1=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[11,0],size=[1,1])
		if choice==464:
			img1=visual.ImageStim(mywindow, image="cext_under8_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[11,0],size=[1,1])
		if choice==465:
			img1=visual.ImageStim(mywindow, image="cext_over7_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[11,0],size=[1,1])
		if choice==466:
			img1=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[11,0],size=[1,1])
		if choice==467:
			img1=visual.ImageStim(mywindow, image="cext_over7_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[11,0],size=[1,1])
		if choice==468:
			img1=visual.ImageStim(mywindow, image="cext_under8_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[11,0],size=[1,1])
		if choice==469:
			img1=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[11,0],size=[1,1])
		if choice==470:
			img1=visual.ImageStim(mywindow, image="cext_under8_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[11,0],size=[1,1])
		if choice==471:
			img1=visual.ImageStim(mywindow, image="cext_over7_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[11,0],size=[1,1])
		if choice==472:
			img1=visual.ImageStim(mywindow, image="cext_under8_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[11,0],size=[1,1])
		if choice==473:
			img1=visual.ImageStim(mywindow, image="cext_over8_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10.5,0],size=[1,1])
		if choice==474:
			img1=visual.ImageStim(mywindow, image="cext_under7_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15.5,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[11,0],size=[1,1])
		if choice==475:
			img1=visual.ImageStim(mywindow, image="cext_over8_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10.5,0],size=[1,1])
		if choice==476:
			img1=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15.5,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[11,0],size=[1,1])
		if choice==477:
			img1=visual.ImageStim(mywindow, image="cext_over8_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10.5,0],size=[1,1])
		if choice==478:
			img1=visual.ImageStim(mywindow, image="cext_under7_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15.5,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[11,0],size=[1,1])
		if choice==479:
			img1=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10.5,0],size=[1,1])
		if choice==480:
			img1=visual.ImageStim(mywindow, image="cext_under7_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15.5,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[11,0],size=[1,1])
		if choice==481:
			img1=visual.ImageStim(mywindow, image="cext_over7_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10.5,0],size=[3,3])
		if choice==482:
			img1=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15.5,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[11,0],size=[2.5,2.5])
		if choice==483:
			img1=visual.ImageStim(mywindow, image="cext_over7_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10.5,0],size=[3,3])
		if choice==484:
			img1=visual.ImageStim(mywindow, image="cext_under7_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15.5,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[11,0],size=[2.5,2.5])
		if choice==485:
			img1=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10.5,0],size=[2.5,2.5])
		if choice==486:
			img1=visual.ImageStim(mywindow, image="cext_under7_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15.5,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[11,0],size=[3,3])
		if choice==487:
			img1=visual.ImageStim(mywindow, image="cext_over7_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10.5,0],size=[2.5,2.5])
		if choice==488:
			img1=visual.ImageStim(mywindow, image="cext_under7_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15.5,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[11,0],size=[3,3])
		if choice==489:
			img1=visual.ImageStim(mywindow, image="cext_over8_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[11,0],size=[3,3])
		if choice==490:
			img1=visual.ImageStim(mywindow, image="cext_under8_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[11,0],size=[2.5,2.5])
		if choice==491:
			img1=visual.ImageStim(mywindow, image="cext_over8_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[11,0],size=[3,3])
		if choice==492:
			img1=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[11,0],size=[2.5,2.5])
		if choice==493:
			img1=visual.ImageStim(mywindow, image="cext_over8_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[11,0],size=[2.5,2.5])
		if choice==494:
			img1=visual.ImageStim(mywindow, image="cext_under8_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[11,0],size=[3,3])
		if choice==495:
			img1=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[11,0],size=[2.5,2.5])
		if choice==496:
			img1=visual.ImageStim(mywindow, image="cext_under8_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[11,0],size=[3,3])
		if choice==497:
			img1=visual.ImageStim(mywindow, image="cext_over7_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[11,0],size=[3,3])
		if choice==498:
			img1=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[11,0],size=[2.5,2.5])
		if choice==499:
			img1=visual.ImageStim(mywindow, image="cext_over7_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[11,0],size=[3,3])
		if choice==500:
			img1=visual.ImageStim(mywindow, image="cext_under8_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[11,0],size=[2.5,2.5])
		if choice==501:
			img1=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[11,0],size=[2.5,2.5])
		if choice==502:
			img1=visual.ImageStim(mywindow, image="cext_under8_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[11,0],size=[3,3])
		if choice==503:
			img1=visual.ImageStim(mywindow, image="cext_over7_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[11,0],size=[2.5,2.5])
		if choice==504:
			img1=visual.ImageStim(mywindow, image="cext_under8_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[11,0],size=[3,3])
		if choice==505:
			img1=visual.ImageStim(mywindow, image="cext_over8_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10.5,0],size=[3,3])
		if choice==506:
			img1=visual.ImageStim(mywindow, image="cext_under7_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15.5,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[11,0],size=[2.5,2.5])
		if choice==507:
			img1=visual.ImageStim(mywindow, image="cext_over8_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10.5,0],size=[3,3])
		if choice==508:
			img1=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15.5,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[11,0],size=[2.5,2.5])
		if choice==509:
			img1=visual.ImageStim(mywindow, image="cext_over8_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10.5,0],size=[2.5,2.5])
		if choice==510:
			img1=visual.ImageStim(mywindow, image="cext_under7_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15.5,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[11,0],size=[3,3])
		if choice==511:
			img1=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[3,3])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10.5,0],size=[2.5,2.5])
		if choice==512:
			img1=visual.ImageStim(mywindow, image="cext_under7_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15.5,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[11,0],size=[3,3])
		if choice==513:
			img1=visual.ImageStim(mywindow, image="cext_over7_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10.5,0],size=[2.5,2.5])
		if choice==514:
			img1=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15.5,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[11,0],size=[2,2])
		if choice==515:
			img1=visual.ImageStim(mywindow, image="cext_over7_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10.5,0],size=[2.5,2.5])
		if choice==516:
			img1=visual.ImageStim(mywindow, image="cext_under7_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15.5,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[11,0],size=[2,2])
		if choice==517:
			img1=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10.5,0],size=[2,2])
		if choice==518:
			img1=visual.ImageStim(mywindow, image="cext_under7_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15.5,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[11,0],size=[2.5,2.5])
		if choice==519:
			img1=visual.ImageStim(mywindow, image="cext_over7_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10.5,0],size=[2,2])
		if choice==520:
			img1=visual.ImageStim(mywindow, image="cext_under7_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15.5,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[11,0],size=[2.5,2.5])
		if choice==521:
			img1=visual.ImageStim(mywindow, image="cext_over8_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[11,0],size=[2.5,2.5])
		if choice==522:
			img1=visual.ImageStim(mywindow, image="cext_under8_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[11,0],size=[2,2])
		if choice==523:
			img1=visual.ImageStim(mywindow, image="cext_over8_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[11,0],size=[2.5,2.5])
		if choice==524:
			img1=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[11,0],size=[2,2])
		if choice==525:
			img1=visual.ImageStim(mywindow, image="cext_over8_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[11,0],size=[2,2])
		if choice==526:
			img1=visual.ImageStim(mywindow, image="cext_under8_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[11,0],size=[2.5,2.5])
		if choice==527:
			img1=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[11,0],size=[2,2])
		if choice==528:
			img1=visual.ImageStim(mywindow, image="cext_under8_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[11,0],size=[2.5,2.5])
		if choice==529:
			img1=visual.ImageStim(mywindow, image="cext_over7_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[11,0],size=[2.5,2.5])
		if choice==530:
			img1=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[11,0],size=[2,2])
		if choice==531:
			img1=visual.ImageStim(mywindow, image="cext_over7_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[11,0],size=[2.5,2.5])
		if choice==532:
			img1=visual.ImageStim(mywindow, image="cext_under8_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[11,0],size=[2,2])
		if choice==533:
			img1=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[11,0],size=[2,2])
		if choice==534:
			img1=visual.ImageStim(mywindow, image="cext_under8_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[11,0],size=[2.5,2.5])
		if choice==535:
			img1=visual.ImageStim(mywindow, image="cext_over7_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[11,0],size=[2,2])
		if choice==536:
			img1=visual.ImageStim(mywindow, image="cext_under8_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[11,0],size=[2.5,2.5])
		if choice==537:
			img1=visual.ImageStim(mywindow, image="cext_over8_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10.5,0],size=[2.5,2.5])
		if choice==538:
			img1=visual.ImageStim(mywindow, image="cext_under7_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15.5,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[11,0],size=[2,2])
		if choice==539:
			img1=visual.ImageStim(mywindow, image="cext_over8_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10.5,0],size=[2.5,2.5])
		if choice==540:
			img1=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15.5,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[11,0],size=[2,2])
		if choice==541:
			img1=visual.ImageStim(mywindow, image="cext_over8_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10.5,0],size=[2,2])
		if choice==542:
			img1=visual.ImageStim(mywindow, image="cext_under7_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15.5,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[11,0],size=[2.5,2.5])
		if choice==543:
			img1=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10.5,0],size=[2,2])
		if choice==544:
			img1=visual.ImageStim(mywindow, image="cext_under7_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15.5,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[11,0],size=[2.5,2.5])
		if choice==545:
			img1=visual.ImageStim(mywindow, image="cext_over7_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10.5,0],size=[2,2])
		if choice==546:
			img1=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15.5,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[11,0],size=[1.5,1.5])
		if choice==547:
			img1=visual.ImageStim(mywindow, image="cext_over7_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10.5,0],size=[2,2])
		if choice==548:
			img1=visual.ImageStim(mywindow, image="cext_under7_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15.5,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[11,0],size=[1.5,1.5])
		if choice==549:
			img1=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10.5,0],size=[1.5,1.5])
		if choice==550:
			img1=visual.ImageStim(mywindow, image="cext_under7_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15.5,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[11,0],size=[2,2])
		if choice==551:
			img1=visual.ImageStim(mywindow, image="cext_over7_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10.5,0],size=[1.5,1.5])
		if choice==552:
			img1=visual.ImageStim(mywindow, image="cext_under7_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15.5,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[11,0],size=[2,2])
		if choice==553:
			img1=visual.ImageStim(mywindow, image="cext_over8_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[11,0],size=[2,2])
		if choice==554:
			img1=visual.ImageStim(mywindow, image="cext_under8_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[11,0],size=[1.5,1.5])
		if choice==555:
			img1=visual.ImageStim(mywindow, image="cext_over8_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[11,0],size=[2,2])
		if choice==556:
			img1=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[11,0],size=[1.5,1.5])
		if choice==557:
			img1=visual.ImageStim(mywindow, image="cext_over8_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[11,0],size=[1.5,1.5])
		if choice==558:
			img1=visual.ImageStim(mywindow, image="cext_under8_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[11,0],size=[2,2])
		if choice==559:
			img1=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[11,0],size=[1.5,1.5])
		if choice==560:
			img1=visual.ImageStim(mywindow, image="cext_under8_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[11,0],size=[2,2])
		if choice==561:
			img1=visual.ImageStim(mywindow, image="cext_over7_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[11,0],size=[2,2])
		if choice==562:
			img1=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[11,0],size=[1.5,1.5])
		if choice==563:
			img1=visual.ImageStim(mywindow, image="cext_over7_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[11,0],size=[2,2])
		if choice==564:
			img1=visual.ImageStim(mywindow, image="cext_under8_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[11,0],size=[1.5,1.5])
		if choice==565:
			img1=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[11,0],size=[1.5,1.5])
		if choice==566:
			img1=visual.ImageStim(mywindow, image="cext_under8_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[11,0],size=[2,2])
		if choice==567:
			img1=visual.ImageStim(mywindow, image="cext_over7_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[11,0],size=[1.5,1.5])
		if choice==568:
			img1=visual.ImageStim(mywindow, image="cext_under8_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[11,0],size=[2,2])
		if choice==569:
			img1=visual.ImageStim(mywindow, image="cext_over8_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10.5,0],size=[2,2])
		if choice==570:
			img1=visual.ImageStim(mywindow, image="cext_under7_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15.5,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[11,0],size=[1.5,1.5])
		if choice==571:
			img1=visual.ImageStim(mywindow, image="cext_over8_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10.5,0],size=[2,2])
		if choice==572:
			img1=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15.5,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[11,0],size=[1.5,1.5])
		if choice==573:
			img1=visual.ImageStim(mywindow, image="cext_over8_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10.5,0],size=[1.5,1.5])
		if choice==574:
			img1=visual.ImageStim(mywindow, image="cext_under7_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15.5,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[11,0],size=[2,2])
		if choice==575:
			img1=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10.5,0],size=[1.5,1.5])
		if choice==576:
			img1=visual.ImageStim(mywindow, image="cext_under7_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15.5,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[11,0],size=[2,2])
		if choice==577:
			img1=visual.ImageStim(mywindow, image="cext_over7_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10.5,0],size=[1.5,1.5])
		if choice==578:
			img1=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15.5,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[11,0],size=[1,1])
		if choice==579:
			img1=visual.ImageStim(mywindow, image="cext_over7_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10.5,0],size=[1.5,1.5])
		if choice==580:
			img1=visual.ImageStim(mywindow, image="cext_under7_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15.5,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[11,0],size=[1,1])
		if choice==581:
			img1=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10.5,0],size=[1,1])
		if choice==582:
			img1=visual.ImageStim(mywindow, image="cext_under7_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15.5,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[11,0],size=[1.5,1.5])
		if choice==583:
			img1=visual.ImageStim(mywindow, image="cext_over7_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10.5,0],size=[1,1])
		if choice==584:
			img1=visual.ImageStim(mywindow, image="cext_under7_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15.5,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[11,0],size=[1.5,1.5])
		if choice==585:
			img1=visual.ImageStim(mywindow, image="cext_over8_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[11,0],size=[1.5,1.5])
		if choice==586:
			img1=visual.ImageStim(mywindow, image="cext_under8_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[11,0],size=[1,1])
		if choice==587:
			img1=visual.ImageStim(mywindow, image="cext_over8_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[11,0],size=[1.5,1.5])
		if choice==588:
			img1=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[11,0],size=[1,1])
		if choice==589:
			img1=visual.ImageStim(mywindow, image="cext_over8_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[11,0],size=[1,1])
		if choice==590:
			img1=visual.ImageStim(mywindow, image="cext_under8_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[11,0],size=[1.5,1.5])
		if choice==591:
			img1=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[11,0],size=[1,1])
		if choice==592:
			img1=visual.ImageStim(mywindow, image="cext_under8_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[11,0],size=[1.5,1.5])
		if choice==593:
			img1=visual.ImageStim(mywindow, image="cext_over7_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[11,0],size=[1.5,1.5])
		if choice==594:
			img1=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[11,0],size=[1,1])
		if choice==595:
			img1=visual.ImageStim(mywindow, image="cext_over7_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[11,0],size=[1.5,1.5])
		if choice==596:
			img1=visual.ImageStim(mywindow, image="cext_under8_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[11,0],size=[1,1])
		if choice==597:
			img1=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[11,0],size=[1,1])
		if choice==598:
			img1=visual.ImageStim(mywindow, image="cext_under8_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[11,0],size=[1.5,1.5])
		if choice==599:
			img1=visual.ImageStim(mywindow, image="cext_over7_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[11,0],size=[1,1])
		if choice==600:
			img1=visual.ImageStim(mywindow, image="cext_under8_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[11,0],size=[1.5,1.5])
		if choice==601:
			img1=visual.ImageStim(mywindow, image="cext_over8_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10.5,0],size=[1.5,1.5])
		if choice==602:
			img1=visual.ImageStim(mywindow, image="cext_under7_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15.5,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[11,0],size=[1,1])
		if choice==603:
			img1=visual.ImageStim(mywindow, image="cext_over8_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10.5,0],size=[1.5,1.5])
		if choice==604:
			img1=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15.5,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[11,0],size=[1,1])
		if choice==605:
			img1=visual.ImageStim(mywindow, image="cext_over8_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10.5,0],size=[1,1])
		if choice==606:
			img1=visual.ImageStim(mywindow, image="cext_under7_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15.5,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[11,0],size=[1.5,1.5])
		if choice==607:
			img1=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10.5,0],size=[1,1])
		if choice==608:
			img1=visual.ImageStim(mywindow, image="cext_under7_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15.5,0],size=[1,1])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[11,0],size=[1.5,1.5])
		if choice==609:
			img1=visual.ImageStim(mywindow, image="cext_over7_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[10.5,0],size=[2.5,2.5])
		if choice==610:
			img1=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15.5,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[11,0],size=[1.5,1.5])
		if choice==611:
			img1=visual.ImageStim(mywindow, image="cext_over7_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10.5,0],size=[2.5,2.5])
		if choice==612:
			img1=visual.ImageStim(mywindow, image="cext_under7_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15.5,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[11,0],size=[1.5,1.5])
		if choice==613:
			img1=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10.5,0],size=[1.5,1.5])
		if choice==614:
			img1=visual.ImageStim(mywindow, image="cext_under7_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15.5,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[11,0],size=[2.5,2.5])
		if choice==615:
			img1=visual.ImageStim(mywindow, image="cext_over7_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10.5,0],size=[1.5,1.5])
		if choice==616:
			img1=visual.ImageStim(mywindow, image="cext_under7_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15.5,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[11,0],size=[2.5,2.5])
		if choice==617:
			img1=visual.ImageStim(mywindow, image="cext_over8_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[11,0],size=[2.5,2.5])
		if choice==618:
			img1=visual.ImageStim(mywindow, image="cext_under8_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[11,0],size=[1.5,1.5])
		if choice==619:
			img1=visual.ImageStim(mywindow, image="cext_over8_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[11,0],size=[2.5,2.5])
		if choice==620:
			img1=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[11,0],size=[1.5,1.5])
		if choice==621:
			img1=visual.ImageStim(mywindow, image="cext_over8_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[11,0],size=[1.5,1.5])
		if choice==622:
			img1=visual.ImageStim(mywindow, image="cext_under8_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[11,0],size=[2.5,2.5])
		if choice==623:
			img1=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[11,0],size=[1.5,1.5])
		if choice==624:
			img1=visual.ImageStim(mywindow, image="cext_under8_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[11,0],size=[2.5,2.5])
		if choice==625:
			img1=visual.ImageStim(mywindow, image="cext_over7_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[11,0],size=[2.5,2.5])
		if choice==626:
			img1=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[11,0],size=[1.5,1.5])
		if choice==627:
			img1=visual.ImageStim(mywindow, image="cext_over7_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[11,0],size=[2.5,2.5])
		if choice==628:
			img1=visual.ImageStim(mywindow, image="cext_under8_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[11,0],size=[1.5,1.5])
		if choice==629:
			img1=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[11,0],size=[1.5,1.5])
		if choice==630:
			img1=visual.ImageStim(mywindow, image="cext_under8_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[11,0],size=[2.5,2.5])
		if choice==631:
			img1=visual.ImageStim(mywindow, image="cext_over7_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under8_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[11,0],size=[1.5,1.5])
		if choice==632:
			img1=visual.ImageStim(mywindow, image="cext_under8_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over7_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[11,0],size=[2.5,2.5])
		if choice==633:
			img1=visual.ImageStim(mywindow, image="cext_over8_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[10.5,0],size=[2.5,2.5])
		if choice==634:
			img1=visual.ImageStim(mywindow, image="cext_under7_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15.5,-.3],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[11,0],size=[1.5,1.5])
		if choice==635:
			img1=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10.5,-.3],size=[2.5,2.5])
		if choice==636:
			img1=visual.ImageStim(mywindow, image="cext_under7_az.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_az.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-15.5,-.3],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[11,0],size=[1.5,1.5])
		if choice==637:
			img1=visual.ImageStim(mywindow, image="cext_over8_pur.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_pur.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[10.5,-.3],size=[1.5,1.5])
		if choice==638:
			img1=visual.ImageStim(mywindow, image="cext_under7_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15.5,-.3],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[11,0],size=[2.5,2.5])
		if choice==639:
			img1=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-15,0],size=[2.5,2.5])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[10.5,-.3],size=[1.5,1.5])
		if choice==640:
			img1=visual.ImageStim(mywindow, image="cext_under7_ver.png", pos=[-15,0])
			img2=visual.ImageStim(mywindow, image="cext_over8_ver.png", pos=[11,0])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-15.5,-.3],size=[1.5,1.5])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[11,0],size=[2.5,2.5])
		txtRecordat1=visual.ImageStim(mywindow, image="Recordatorio1.png", pos=[0,15])
		txtRecordat2=visual.TextStim(mywindow,text="S = Si",wrapWidth = 60,color=[0,0,0], pos=[-11,-14], colorSpace="rgb255")
		txtRecordat3=visual.TextStim(mywindow,text="N = No",wrapWidth = 60,color=[0,0,0], pos=[8,-14], colorSpace="rgb255")
		txtRecordat1.draw()
		txtRecordat2.draw()
		txtRecordat3.draw()
		img1.draw()
		img2.draw()
		img3.draw()
		img4.draw()
		mybaseline.close
		mywindow.update()
		presentation_time = time.time()
#Tiempo que duran los ensayos0
		core.wait(1 )
		presentation2_time = time.time()
#		mywindow.setColor(color=[255,255,255], colorSpace="rgb255")
#		mywindow.update()
		mywindow.setColor(color=[255,255,255], colorSpace="rgb255")
		txtRecordat1=visual.ImageStim(mywindow, image="Recordatorio1.png", pos=[0,15])
		txtRecordat2=visual.TextStim(mywindow,text="S = Si",wrapWidth = 60,color=[0,0,0], pos=[-11,-14], colorSpace="rgb255")
		txtRecordat3=visual.TextStim(mywindow,text="N = No",wrapWidth = 60,color=[0,0,0], pos=[8,-14], colorSpace="rgb255")
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
			response_time = time.time() - presentation_time
			response_timeB = time.time() - presentation2_time
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
		isPurple=(choice in Pur)
		if isPurple: 
			Colorx='Purpura'
		isOrange=(choice in Nar)
		if isOrange: 
			Colorx='Naranja'
		isGreen=(choice in Ver)
		if isGreen: 
			Colorx='Verde'
		isBlue=(choice in Az)
		if isBlue: 
			Colorx='Azul'
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
		reglita_time = time.time()
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
			response_time2 = time.time() - reglita_time
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
		mybaseline.write(str(i)+","+str(choice)+","+str(Respuesta)+","+str(isCorrect)+","+str(rightcounterb)+","+str(wrongcounterb)+","+str(isHit)+","+str(hitB)+","+str(isRejection)+","+str(rejectionB)+","+str(isFalseAlarm)+","+str(falsealarmB)+","+str(isMiss)+","+str(missB)+","+str(Confidence)+","+str(response_time)+","+str(response_timeB)+","+str(response_time2)+","+str(Colorx)+"\n")
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
