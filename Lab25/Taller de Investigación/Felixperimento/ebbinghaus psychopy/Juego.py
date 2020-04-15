from psychopy import visual, core, event, gui
import time

Matrix1={'a':0.84,'b':-1.08,'c':-0.94,'d':0.96}
Matrix2={'a':-0.95,'b':1.21,'c':1.00,'d':-0.91}
Matrix3={'a':1.11,'b':-0.92,'c':-0.92,'d':0.84}
matrixSel=0
matrices=[Matrix1,Matrix2,Matrix3]
userSel=0



options={'opcion':'1','Nombre':'Participante'}                                                                    #Diccionario
myDlg=gui.DlgFromDict(dictionary=options,title='Game')                                                            #Crear un cuadro de dialogo
if myDlg.OK:
	if options['opcion']=='1':
		matrixSel=0
	elif options['opcion']=='2':
		matrixSel=1	
	elif options['opcion']=='3':
		matrixSel=2
	else:
		print "You screwed it up"
		core.quit()
else:
	core.wait(0.1)
print "Matrix Selection:", matrixSel

myWin=visual.Window(monitor="testMonitor", units="cm", fullscr=True)
myWin.setColor([0,0,255], colorSpace="rgb255")
myWin.update()
myWin.setColor([0,0,255], colorSpace="rgb255")
myWin.update()

myFile=open(options['Nombre']+time.strftime('%Y-%m-%d')+time.strftime('%H.%M.%S')+'_Results.csv','w')             #Abrir/Guardar con nombre, dia y hora 
myFile.write('Ensayo, Seleccion Usuario, Pago, Total \n')

options={'opcion':'A'}
counter=0
for i in range(300):
	# myDlg=gui.DlgFromDict(dictionary=options,title='User Selection') 
	# if myDlg.OK:
	#  	if options['opcion']=='A':
	#  		userSel=0
	#  	elif options['opcion']=='B':
	#  		userSel=1
	#  	elif options['opcion']=='C':
	#  		userSel=2
	#  	elif options['opcion']=='D':
	#  		userSel=3
	#  	else:
	#  		core.quit()
	# else:
	# 	core.quit
	validKeyPressed=False
	while not validKeyPressed:
		for key in event.getKeys():
			if key in matrices[matrixSel].keys():
				validKeyPressed=True
				userSel=key
			elif key=='escape':
				core.quit()
	myFile.write(str(i+1)+','+str(userSel)+','+str(matrices[matrixSel][userSel])+','+str(counter)+"\n")
	
				
	counter=counter + matrices[matrixSel][userSel]
	txtCounter=visual.TextStim(myWin,text=str(counter), height=8, color=(255,117,5), colorSpace='rgb255')
	txtCounter.draw()
	myWin.update()
	
myFile.close()

