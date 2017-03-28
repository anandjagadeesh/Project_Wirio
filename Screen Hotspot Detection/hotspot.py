import os
import sys
import pickle
import glob
import matplotlib.pyplot as plt

class HotspotFinder():
	def __init__(self):
		self.lu=[]
		self.li=[]
		self.hslist=[]
		self.makelist()
		self.findhs()
		self.ploths()
	def makelist(self):
		self.l1=glob.glob('./RecordedData/user*.txt')
		for i in self.l1:
			i="u"+i.split("/u")[-1]
			self.lu.append(i)
		self.l1=glob.glob('./RecordedData/impostor*.txt')
		for i in self.l1:
			i="i"+i.split("/i")[-1]
			self.li.append(i)
	def findhs(self):
		for i in self.lu:
			with open('./RecordedData/'+i,'rb') as file1:
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
	def ploths(self):
		x=[]
		y=[]
		t=[]
		for i in self.hslist:
			x.append(i[0])
			y.append(i[1])
			t.append(i[2])
		fig = plt.figure()
		plt.gca().invert_yaxis()
		#plt.gca().invert_xaxis()
		plt.scatter(x,y,c=t)
		fig.suptitle("Hotspots_User_Plot")
		plt.ylabel('Pixels on Y')
		plt.xlabel('Pixels on X')
		fig.savefig("./RecordedDataPlot/Hotspots_User_Plot.jpg")
		plt.show()
		with open("./RecordedData/"+"Hotspots_User.txt",'wb') as files:
			pickle.dump(self.hslist,files)
		
if __name__ == '__main__':
	hs=HotspotFinder()
