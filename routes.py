from puente_H import motors
import movement as mov
import search
import Buttons
import pyzbar.pyzbar as pyzbar
import numpy as np
import cv2 
import time
import math
def stopmotors():
	v=0
	d="f"
	m="a"
	motors(m,d,v)
	m="b"
	motors(m,d,v)
	
def right(distance):
	v=100
	d="r"
	m="a"
	motors(m,d,v)
	d="f"         
	m="b"
	motors(m,d,v)
	time.sleep(0.7)
	v=65
	d="f"
	m="a"
	motors(m,d,v)
	m="b"
	motors(m,d,v)
	if distance<5:
		time.sleep(2.3)
	else:
		time.sleep(1.3)
	v=100
	d="f"
	m="a"
	motors(m,d,v)
	d="r"         
	m="b"
	motors(m,d,v)
	time.sleep(0.7)
	
def left(distance):
	v=100
	d="f"
	m="a"
	motors(m,d,v)
	d="r"         
	m="b"
	motors(m,d,v)
	time.sleep(0.7)
	v=65
	d="f"
	m="a"
	motors(m,d,v)
	m="b"
	motors(m,d,v)
	if distance<5:
		time.sleep(2.3)
	else:
		time.sleep(1.3)
	v=100
	d="r"
	m="a"
	motors(m,d,v)
	d="f"         
	m="b"
	motors(m,d,v)
	time.sleep(0.7)
	
	
def move(distance,orientation,decodedObject,pos,cap,pi,pin,lost,memory):
	if (distance<35 ):
		print("routes distance: "+str(distance))
		print("routes orientation: "+str(orientation))
		if orientation=="right1" or orientation=="right2":
			left(distance)
			stopmotors()
			print("VOLVEMOS A SEARCH")
			search.s(decodedObject.data.decode("utf-8"),cap, pi,pin,memory)
		elif orientation=="left1" or orientation=="left2":
			right(distance)
			stopmotors()
			search.s(decodedObject.data.decode("utf-8"),cap, pi,pin,memory)
			
		v=80
		d="f"
		m="a"
		motors(m,d,v)
		v=80
		m="b"
		motors(m,d,v)
		first=False
		if distance<10:
			time.sleep(1.5)
		elif distance<20:
			time.sleep(1)
		elif distance<30:
			time.sleep(0.5)
		else:
			time.sleep(0.3)
		stopmotors()
		mov.gotodestination(decodedObject,pos,cap,first,pi,pin,lost,memory)
	else:
		stopmotors()
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
	elif a<b:
		print("a: ")
		print(a)
		print("b: ")
		print(b)
		print("right")
		right(distance)
	else:
		print("distance MOVEMO: ")
		print(distance)
		print(el2[1]*1.10)
		print(el2[1]*0.90)
		if distance>el2[1]*1.10:
			v=80
			d="r"
			m="a"
			motors(m,d,v)
			v=80
			m="b"
			motors(m,d,v)
			first=False
			if distance<10:
				time.sleep(1)
			elif distance<20:
				time.sleep(1)
			elif distance<30:
				time.sleep(0.5)
			else:
				time.sleep(0.3)
			stopmotors()
			mov.gotomemodestination(decodedObject,pos,cap,first,pi,pin,lost,memory,el2,movememo,button)
		elif distance<el2[1]*0.90:
			v=80
			d="f"
			m="a"
			motors(m,d,v)
			v=80
			m="b"
			motors(m,d,v)
			first=False
			if distance<10:
				time.sleep(1)
			elif distance<20:
				time.sleep(1)
			elif distance<30:
				time.sleep(0.5)
			else:
				time.sleep(0.3)
			stopmotors()
			mov.gotomemodestination(decodedObject,pos,cap,first,pi,pin,lost,memory,el2,movememo,button)
		else:
			search.s(button,cap, pi,pin,memory)
			
		
		
		
def stop(decodedObject,pos,cap):
	v=0
	d="f"
	m="a"
	motors(m,d,v)
	m="b"
	motors(m,d,v)
	first=False
	mov.gotodestination(decodedObject,pos,cap,first,pi,pin,lost,memory,el2,movememo)

		
		
		
