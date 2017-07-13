import psychopy.visual
import psychopy.event
import math
import random
import time

def ringCoord(ringrad, ttl, i):
	return [ringrad * math.cos(2 * math.pi / ttl * i),ringrad * math.sin(2 * math.pi / ttl * i)]

def drawcircs(circ,ringrad, n):
	for i in range(n):
		circ.pos = ringCoord(ringrad,n,i)
		circ.draw()

def crossDraw(line,size):
	##needs to be called at every flip
	'''p.v.line, int -> null'''
	line.start =	[0,size]
	line.end =	[0,-size]	
	line.draw()
	line.start =	[size,0]
	line.end =	[-size,0]
	line.draw()

def setLine(line, size, isVert, pos):
	'''p.v.line,int,bool,int,ls[2]->null'''
	line.start = pos;
	line.end = pos;
	if (isVert):
		line.start +=	[0,size]
		line.end -=	[0,size]
	else:
		line.start +=	[size,0]
		line.end -=	[size,0]	
	line.draw()

def randbool():
	return ((random.randint(0,100) % 2) == 0)

def getAccuracy(target, inputls):
	'''str,ls->bool'''
	return target in inputls

