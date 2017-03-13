import os
import sys
import pickle
import glob
import matplotlib.pyplot as plt

path=os.path.join(os.getcwd(),"RecordedData/")
with open (os.path.join(path,sys.argv[1]+'.txt'),'rb') as files:
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
	plt.ylabel('Y axis')
	plt.xlabel('X axis')
	fig.savefig("./RecordedDataPlot/"+sys.argv[1]+'.jpg')
	plt.show()
