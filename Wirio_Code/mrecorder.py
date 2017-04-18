import sys
import pickle
from pynput import mouse
import time
import os
import numpy as np

class mouse_tracker():
	def __init__(self):
		self.points=0
		self.list1=[]
		self.login_name=''
		self.starttime=''
	def move(self,x,y):
		self.list1.append([0,x,y])
		print "Mouse at: "+str(x)+" "+str(y)
	def click(self,x,y,button,pressed):
		if pressed:
			self.list1.append([1,x,y])
			print "Mouse pressed at: "+str(x)+" "+str(y)
			if x==0 and y==0:
				option=int(raw_input("Enter 1 to continue, 0 to exit: "))
				if option==0:
					with open("./data/"+self.login_name+" ["+self.starttime+"].wirdata",'wb') as files:
						pickle.dump(self.list1,files)
					return False
	def mainfunct(self):
		self.login_name=str(raw_input("Enter \'user\' for user and \'impostor\' for impostor: "))
		print self.login_name
		self.starttime=time.ctime()
		print self.starttime
		print 'mouse'
		self.list1.append([self.login_name,self.starttime,'mouse'])
		with mouse.Listener(on_move=self.move,on_click=self.click) as listener:
			listener.join()
			
if __name__ == '__main__':
	mt=mouse_tracker()
	mt.mainfunct()
