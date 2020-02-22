import movement as mov
import search
import Buttons
import pyzbar.pyzbar as pyzbar
import numpy as np
import cv2 
import time
import math
from cadira import move
	
def right(distance):
	move("R")
	time.sleep(0.7)
	move("F")
	if distance<5:
		time.sleep(2.3)
	else:
		time.sleep(1.3)
	move("L")
	time.sleep(0.7)
	
def left(distance):
	move("L")
	time.sleep(0.7)
	move("F")
	if distance<5:
		time.sleep(2.3)
	else:
		time.sleep(1.3)
	move("R")
	time.sleep(0.7)
	
def rmove(distance,orientation,decodedObject,pos,cap,pi,pin,lost,memory):
	if (distance<4 ):
		print("routes distance: "+str(distance))
		print("routes orientation: "+str(orientation))
		if orientation=="right1" or orientation=="right2":
			left(distance)
			move("S")
			time.sleep(1)
			print("VOLVEMOS A SEARCH")
			search.s(decodedObject.data.decode("utf-8"),cap, pi,pin,memory)
		elif orientation=="left1" or orientation=="left2":
			right(distance)
			move("S")
			time.sleep(1)
			search.s(decodedObject.data.decode("utf-8"),cap, pi,pin,memory)
			
		move("F")
		first=False
		if distance<10:
			time.sleep(1.5)
		elif distance<20:
			time.sleep(1)
		elif distance<30:
			time.sleep(0.5)
		else:
			time.sleep(0.3)
		move("S")
		time.sleep(1)
		mov.gotodestination(decodedObject,pos,cap,first,pi,pin,lost,memory)
	else:
		move("S")
		time.sleep(1)
		first=False
		print("SELECCIONA OTRO DESTINO")
		Buttons.main2(cap, pi,pin,memory)
		
def movememo(decodedObject,distance,orientation,dest,pos,cap,pi,pin,lost,memory,el2,movememo,button):
	print("################# DENTRO DE MOVEMEMO #######################")
	if el2[2]=="right2": 
		a=0 
	elif el2[2]=="right1": 
		a=1 
	elif el2[2]=="center": 
		a=2 
	elif el2[2]=="left1": 
		a=3 
	elif el2[2]=="left2": 
		a=4
	if orientation=="right2": 
		b=0 
	elif orientation=="right1": 
		b=1 
	elif orientation=="center": 
		b=2 
	elif orientation=="left1": 
		b=3 
	elif orientation=="left2": 
		b=4
	if a>b:
		print("a: ")
		print(a)
		print("b: ")
		print(b)
		print("left")
		left(distance)
		move("S")
		time.sleep(1)
	elif a<b:
		print("a: ")
		print(a)
		print("b: ")
		print(b)
		print("right")
		right(distance)
		move("S")
		time.sleep(1)
	else:
		print("distance MOVEMO: ")
		print(distance)
		print(el2[1]*1.10)
		print(el2[1]*0.90)
		if distance>el2[1]*1.10:
			move("B")
			first=False
			if distance<10:
				time.sleep(1)
			elif distance<20:
				time.sleep(1)
			elif distance<30:
				time.sleep(0.5)
			else:
				time.sleep(0.3)
			move("S")
			time.sleep(1)
			mov.gotomemodestination(decodedObject,pos,cap,first,pi,pin,lost,memory,el2,movememo,button)
		elif distance<el2[1]*0.90:
			move("F")
			first=False
			if distance<10:
				time.sleep(1)
			elif distance<20:
				time.sleep(1)
			elif distance<30:
				time.sleep(0.5)
			else:
				time.sleep(0.3)
			move("S")
			time.sleep(1)
			mov.gotomemodestination(decodedObject,pos,cap,first,pi,pin,lost,memory,el2,movememo,button)
		else:
			search.s(button,cap, pi,pin,memory)

		
		
		
