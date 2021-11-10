import pyzbar.pyzbar as pyzbar
import RPi.GPIO as GPIO    #Importamos la libreria RPi.GPIO
import functions as f
import numpy as np
import cv2 
import time
import math
from cadira import move

def decode(im) : 
	# Find barcodes and QR codes
	decodedObjects = pyzbar.decode(im)
	# Print results
	# for obj in decodedObjects:
	#     print('Type : ', obj.type)
	#     print('Data : ', obj.data,'\n')  
	#     print('object : ', obj,'\n')   
	return decodedObjects
	
def sortqr(val):
	return val[0]


def scan(cap, pi,pin):
	memory = []
	memaux = []
	font = cv2.FONT_HERSHEY_SIMPLEX
	servopos=[500,700,900,1100,1300,1500,1700,1900,2100,2300,2500,500,700,900,1100,1300,1500,1700,1900,2100,2300,2500]
	pos=0
	while(True) and pos<=21:
		if cap.isOpened():
			#print(pos)
			print("servopos: ")
			print(servopos[pos])
			if pos==11:
				t_end = time.time() + 3.1#60 * 15
				while time.time() < t_end:
					move("R")
				move("S")
				time.sleep(0.5)
				move("S")

			pi.set_servo_pulsewidth(pin, servopos[pos])
			pos+=1
			time.sleep(0.3)
		    
			for i in range(4):
				cap.grab()
			ret, frame = cap.read()

			for i in range(4):
				cap.grab()
		    
			#        cv2.imshow('frame',frame)
			# Our operations on the frame come here
			im = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

			height, width = im.shape
			# print(height,width)
			totalpixels=height*width

			decodedObjects = decode(im)
			for decodedObject in decodedObjects:
				print("CODIGO DETECTADO")
				print(decodedObject.data.decode("utf-8"))

				points = decodedObject.polygon
				pt, xmedia, ymedia = f.getPoints(decodedObject.polygon)
				distance, dist, qrsize = f.getSize(decodedObject, totalpixels)
				orientation = f.getOrientation(points, dist)

				memaux.append([int(decodedObject.data.decode("utf-8")),qrsize,orientation])

	
				cv2.putText(frame, "p0", pt[0], font, 1, (0,255,255), 2, cv2.LINE_AA)
				cv2.putText(frame, "p1", pt[1], font, 1, (0,255,255), 2, cv2.LINE_AA)
				cv2.putText(frame, "p2", pt[2], font, 1, (0,255,255), 2, cv2.LINE_AA)
				cv2.putText(frame, "p3", pt[3], font, 1, (0,255,255), 2, cv2.LINE_AA)
		    
	#        ret, frame = cap.read() 
		    # Display the resulting frame
			cv2.imshow('frame',frame)
			key = cv2.waitKey(1)
			if key & 0xFF == ord('q'):
				break
			elif key & 0xFF == ord('s'): # wait for 's' key to save 
				cv2.imwrite('Capture.png', frame) 
				
	memaux.sort(key=sortqr)
	print("······· MEMAUX ··········")
	print(memaux)
	for el in memaux:
		if not memory:
			memory.append(el)
		else:
			if el[0] == memory[len(memory)-1][0]:
				if el[2]>memory[len(memory)-1][2]:
					memory.pop()
					memory.append(el)
			else:
				memory.append(el)
	return memory

