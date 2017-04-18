import os
import sys
import pickle
import glob
import matplotlib.pyplot as plt

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
