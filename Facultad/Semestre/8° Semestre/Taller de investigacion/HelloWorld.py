#cmd correr en Ebbinghaus Psychopy
from psychopy import visual, core, event
import random

print "hello world"

mywindow= visual.Window(monitor="testMonitor", units="cm", fullscr=True)
#"monitor"= Cuál monitor proyecta; unidades= cm, in, px, fullscr=True/False

mymouse= event.Mouse(mywindow)

options=[1,1,1,1,2,3,4,1]
#eventos posibles; si pones muchos 1, hay más posibilidadesd e que aparezcan 1

mywindow.update()
for i in range (3):
#in range () indica el número de ensayos.
	choice=options[random.randint(0,len(options)-1)]
	#randint siempre tiene que ser n-1, porque el 0 cuenta y en len, me marca la lenght de mis opciones
	if choice==1:
		img1=visual.ImageStim(mywindow, image="moon.png", pos=[-10,0])

		img2=visual.ImageStim(mywindow, image="moon.png", pos=[10,0], size=[10,10])

	if choice==2:
		img1=visual.ImageStim(mywindow, image="world.png", pos=[-10,0])

		img2=visual.ImageStim(mywindow, image="moon.png", pos=[10,0], size=[10,10])
	if choice==3:
		img1=visual.ImageStim(mywindow, image="World.png", pos=[10,0])

		img2=visual.ImageStim(mywindow, image="moon.png", pos=[-10,0], size=[10,10])
	if choice==4:
		img1=visual.ImageStim(mywindow, image="World.png", pos=[-10,0])

		img2=visual.ImageStim(mywindow, image="world.png", pos=[10,0], size=[10,10])
	#Se especifica la presentación de cada condición posible
	img1.draw()

	img2.draw()

	mywindow.update()
	#Siempre que se de una nueva vista, hay que updatear la window
	while 'm' not in event.getKeys(): 
		core.wait(0.1)
		#if 'escape' in event.getKeys():
			#core.quit()
		#Se comentó el if porque aparentemente canceló el 'm'		
		#Bajar subline 3
