from __future__ import division
import math
import numpy as np
import os
import sys

# passed with str() function applied

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
