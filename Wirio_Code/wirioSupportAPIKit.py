######################################################################
# Program Name: Wirio Support API Kit                                #
#--------------------------------------------------------------------#
# AUTHOR: Anand J. <https://github.com/anandjagadeesh>               #
# Requirements: All Modules given Below | On Python 2.7.9            #
# Proposed Updates: Migration to Python 3 or above and add backward  #
#                   compatibility for Python 2 in later stages       #
######################################################################

######################################################################
# PYTHON MODULES TO BE INCLUDED                                      #
######################################################################
from __future__ import division
import math
import numpy as np
import os
import sys
import pickle
import glob
import matplotlib.pyplot as plt
from pynput import mouse
import time
import Xlib
import Xlib.display

######################################################################
# ANGLE METRICS                                                      #
######################################################################
def angleMetricAPI(x1,y1,x2,y2,x3,y3):
		
	a=0.0
	b=0.0
	c=0.0
	
	a=math.sqrt(((x3-x2)**2)+((y3-y2)**2))
	b=math.sqrt(((x1-x3)**2)+((y1-y3)**2))
	c=math.sqrt(((x2-x1)**2)+((y2-y1)**2))
	
	area=math.sqrt(((a+b+c)/2)*(((a+b+c)/2)-a)*(((a+b+c)/2)-b)*(((a+b+c)/2)-c))
	
	d=((2*area)/c)
	
	angB=acos((b**2-((a**2)+(c**2)))/(-2*a*c))
	
	opp=math.sqrt(((x2-x2)**2)+((y2-y1)**2))
	adj=math.sqrt(((x2-x1)**2)+((y1-y1)**2))
	
	angA=atan(opp/adj)
	
	return str(angA)+'|'+str(angB)+'|'+str(d)

######################################################################
# SCREEN SIZE                                                        #
######################################################################
def findresolution():
	resolution = Xlib.display.Display().screen().root.get_geometry()
	return str(resolution.width)+"x"+str(resolution.height)

######################################################################
# HOTSPOT PLOTTER                                                    #
######################################################################
class HotspotFinder():
	def __init__(self):
		self.hslist=[]
	#------- FIND HOTSPOTS FOR CURRENT USER WHO IS LOGGED IN IF DATA PRESENT -------#
	def findHotspots(self,path,uname):
		if uname in os.getusername():
			self.l1=glob.glob(path+os.getusername()+"*.wirdata")
			for i in self.l1:
				with open(path+i,'rb') as file1:
					fileval=pickle.load(file1)
				coordlist=fileval[1:]
				for j in coordlist:
					flag=0
					for k in self.hslist:
						if k[0]==j[1] and k[1]==j[2]:
							k[2]=k[2]+1
							flag=1
					if flag==0:
						self.hslist.append([j[1],j[2],1])
	#------- PLOT HOTSPOTS FOR CURRENT USER WHO IS LOGGED IN IF DATA PRESENT -------#
	def ploths(self,plotpath,datapath):
		x=[]
		y=[]
		t=[]
		templist=[]
		for i in self.hslist:
			templist.append(i[::-1])
		templist.sort(reverse=True)
		self.hslist=[]
		for i in templist:
			self.hslist.append(i[::-1])
		for i in self.hslist:
			print i
			x.append(i[0])
			y.append(i[1])
			t.append(i[2])
		fig = plt.figure()
		plt.gca().invert_yaxis()
		plt.scatter(x,y,c=t)
		fig.suptitle("Hotspots_User_Plot")
		plt.ylabel('Pels on Y')
		plt.xlabel('Pels on X')
		fig.savefig(plotpath+"Hotspots_User_Plot.jpg")
		plt.show()
		x=[]
		y=[]
		t=[]
		for i in self.hslist[:15]:
			print i
			x.append(i[0])
			y.append(i[1])
			t.append(i[2])
		fig = plt.figure()
		plt.gca().invert_yaxis()
		plt.scatter(x,y,c=t)
		fig.suptitle("Hotspots_User_Plot_Maximum_Spots")
		plt.ylabel('Pels on Y')
		plt.xlabel('Pels on X')
		fig.savefig(plotpath+"Hotspots_User_Plot_Maximum_Spots.jpg")
		plt.show()
		with open(datapath+"Hotspots_User_MaxSpots.wirdata",'wb') as files:
			pickle.dump(self.hslist[:15],files)
		with open(datapath+"Hotspots_User.wirdata",'wb') as files:
			pickle.dump(self.hslist,files)

######################################################################
# SIMPLE PATH PLOTTER FOR PELS MOVED ON SCREEN                       #
######################################################################
def plotPathsOnScreen(datapath,plotpath):
	with open (path,'rb') as files:
		fileval=pickle.load(files)
		coordlist=fileval[1][1:]
		xcoord=[]
		ycoord=[]
		for i in coordlist:
			xcoord.append(i[0])
			ycoord.append(i[1])
		fig = plt.figure()
		fig.suptitle(fileval[0])
		plt.gca().invert_yaxis()
		plt.plot(xcoord,ycoord)
		plt.ylabel('Pels on Y axis')
		plt.xlabel('Pels on X axis')
		fig.savefig(plotpath)
		plt.show()


