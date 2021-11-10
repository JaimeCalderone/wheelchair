import pyzbar.pyzbar as pyzbar
import RPi.GPIO as GPIO    #Importamos la libreria RPi.GPIO
import numpy as np
import cv2 
import time
import math
from puente_H import motors
from movement import gotodestination

# get the webcam:
cap = cv2.VideoCapture(0)
#cap.set(cv2.CAP_PROP_FPS, 40)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
time.sleep(2)

GPIO.setmode(GPIO.BCM)   #Ponemos la Raspberry en modo BOARD
GPIO.setup(17,GPIO.OUT)    #Ponemos el pin 21 como salida
p = GPIO.PWM(17,50)        #Ponemos el pin 21 en modo PWM y enviamos 50 pulsos por segundo
p.start(2.5)               #Enviamos un pulso del 7.5% para centrar el servo

def decode(im) : 
	# Find barcodes and QR codes
	decodedObjects = pyzbar.decode(im)
	# Print results
	# for obj in decodedObjects:
	#     print('Type : ', obj.type)
	#     print('Data : ', obj.data,'\n')  
	#     print('object : ', obj,'\n')   
	return decodedObjects


def s(button):
	print(button)
	font = cv2.FONT_HERSHEY_SIMPLEX
	servopos=[2.5,3.75,5,6.25,7.5,8.75,10,11.25,12.5,2.5,3.75,5,6.25,7.5,8.75,10,11.25,12.5]
	if cap.isOpened():
		for spos in servopos:
			position=spos
			p.ChangeDutyCycle(float(position))
			ret, frame = cap.read()
			time.sleep(1)
		
			ret, frame = cap.read()

			# Our operations on the frame come here
			im = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

			height, width = im.shape
			# print(height,width)
			totalpixels=height*width
	
			decodedObjects = decode(im)
			for decodedObject in decodedObjects:
				print(decodedObject.data.decode("utf-8"))
				print(button)
		    	
				pt = f.getPoints(decodedObject.polygon)
				distance, dist, qrsize = f.getSize(decodedObject, totalpixels)
				orientation = f.getOrientation(points, dist)

				if(decodedObject.data.decode("utf-8") ==button):
					print("ENCONTRADO")
					p.ChangeDutyCycle(7.5)
					p.stop()
					gotodestination(decodedObject,servopos[pos],cap)

				cv2.putText(frame, "p0", pt[0], font, 1, (0,255,255), 2, cv2.LINE_AA)
				cv2.putText(frame, "p1", pt[1], font, 1, (0,255,255), 2, cv2.LINE_AA)
				cv2.putText(frame, "p2", pt[2], font, 1, (0,255,255), 2, cv2.LINE_AA)
				cv2.putText(frame, "p3", pt[3], font, 1, (0,255,255), 2, cv2.LINE_AA)
	

	
	
			ret, frame = cap.read()
			# Display the resulting frame
			cv2.imshow('frame',frame)
			key = cv2.waitKey(1)
			if key & 0xFF == ord('q'):
				break
			elif key & 0xFF == ord('s'): # wait for 's' key to save
				cv2.imwrite('Capture.png', frame)  
			

