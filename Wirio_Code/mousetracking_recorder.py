import sys
import pickle
from pynput import mouse
import time
import os

coordlist=[]

def move(x,y):
	coord=[]
	coord.append(x)
	coord.append(y)
	coordlist.append(coord)
	print coord
	
def record():
	print "Mouse Clicked"
	name1=raw_input("Enter file name: ")
	print "Data saved!"
	recorded=[name1,coordlist]
	with open("./data/"+name1+".wirdata",'wb') as files:
		pickle.dump(recorded,files)
	os.system("python plotdata.py "+name1)

def click(x, y, button, pressed):
	if pressed:
		record()
		#return False
		
if __name__ == '__main__':
	with mouse.Listener(on_move=move,on_click=click) as listener:
		listener.join()
