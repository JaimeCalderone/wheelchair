import pyzbar.pyzbar as pyzbar
import RPi.GPIO as GPIO    #Importamos la libreria RPi.GPIO
import functions as f
import numpy as np
import cv2 
import time
import math
from puente_H import motors
import movement as mov

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
	return val[1]
	
def movementmemo(button,cap,pi,pin,el2,memory):
    font = cv2.FONT_HERSHEY_SIMPLEX
    servopos=[500,700,900,1100,1300,1500,1700,1900,2100,2300,2500,500,700,900,1100,1300,1500,1700,1900,2100,2300,2500]
    pos=0
    while(True):
    	if cap.isOpened():
		    #print(pos)
		    print("servopos: ")
		    print(servopos[pos])
		    if pos==11:
		        v=100
		        d="f"
		        m="a"
		        motors(m,d,v)
		        d="r"         
		        m="b"
		        motors(m,d,v)
		        time.sleep(1.6)
	#            ret, frame = cap.read()
		        v=0
		        d="f"
		        m="a"
		        motors(m,d,v)
		        m="b"
		        motors(m,d,v)

		    pi.set_servo_pulsewidth(pin, servopos[pos])
		    pos+=1
		    time.sleep(0.18)
		    
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
		    	print(button)
		    	
		    	points = decodedObject.polygon
		    	pt, xmedia, ymedia = f.getPoints(decodedObject.polygon)
		    	distance, dist, qrsize = f.getSize(decodedObject, totalpixels)
		    	orientation = f.getOrientation(points, dist)
		    	
		    	if(int(decodedObject.data.decode("utf-8")) ==el2[0]):
		    		print("ENCONTRADO")
		    		pi.set_servo_pulsewidth(pin, 1500)
		    		time.sleep(0.5)
		    		first=True
		    		lost=0
		    		movememo=True
		    		mov.gotomemodestination(decodedObject,servopos[pos],cap,first,pi,pin,lost,memory,el2,movememo,button)
		    		
		    	cv2.putText(frame, "p0", pt[0], font, 1, (0,255,255), 2, cv2.LINE_AA)
		    	cv2.putText(frame, "p1", pt[1], font, 1, (0,255,255), 2, cv2.LINE_AA)
		    	cv2.putText(frame, "p2", pt[2], font, 1, (0,255,255), 2, cv2.LINE_AA)
		    	cv2.putText(frame, "p3", pt[3], font, 1, (0,255,255), 2, cv2.LINE_AA)
		    	
		    if pos==22:
		    	print("NO SE HA ENCONTRADO EL CODIGO")
		    
	#        ret, frame = cap.read() 
		    # Display the resulting frame
		    cv2.imshow('frame',frame)
		    key = cv2.waitKey(1)
		    if key & 0xFF == ord('q'):
		        break
		    elif key & 0xFF == ord('s'): # wait for 's' key to save 
		        cv2.imwrite('Capture.png', frame)  
    
def gomemory(button, cap, pi,pin,memory,qrdetected):
	print("##### Entra en memoria ######")	
	memory.sort(key=sortqr, reverse = True)
	print("##### memory ######")	
	print(memory)
	for el in memory:
		if int(button)==el[0]:
			for el2 in memory:
				print("eeeeoooo")
				print("")
				print("int(button):")
				print("")
				print(int(button))
				print("")
				print("el2[0]:")
				print("")
				print(el2[0])
				print("")
				print("qrdetected:")
				print("")
				print(qrdetected)
				if int(button)!=el2[0] and el2[0] in qrdetected:
					print("##### ir a movementmemo ######")	
					movementmemo(button,cap,pi,pin,el2,memory)
					print(el2)	
			


def s(button, cap, pi,pin,memory):
    print(button)
    font = cv2.FONT_HERSHEY_SIMPLEX
    servopos=[500,700,900,1100,1300,1500,1700,1900,2100,2300,2500,500,700,900,1100,1300,1500,1700,1900,2100,2300,2500]
    pos=0
    qrdetected=[]
    while(True):
    	if cap.isOpened():
		    #print(pos)
		    print("servopos: ")
		    print(servopos[pos])
		    if pos==11:
		        v=100
		        d="f"
		        m="a"
		        motors(m,d,v)
		        d="r"         
		        m="b"
		        motors(m,d,v)
		        time.sleep(1.7)
	#            ret, frame = cap.read()
		        v=0
		        d="f"
		        m="a"
		        motors(m,d,v)
		        m="b"
		        motors(m,d,v)

		    pi.set_servo_pulsewidth(pin, servopos[pos])
		    pos+=1
		    time.sleep(0.18)
		    
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
		    	if int(decodedObject.data.decode("utf-8")) not in qrdetected:
		    		qrdetected.append(int(decodedObject.data.decode("utf-8")))
		    	print("CODIGO DETECTADO")
		    	print(decodedObject.data.decode("utf-8"))
		    	print(button)
		    	
		    	points = decodedObject.polygon
		    	pt, xmedia, ymedia = f.getPoints(decodedObject.polygon)
		    	distance, dist, qrsize = f.getSize(decodedObject, totalpixels)
		    	orientation = f.getOrientation(points, dist)
		    	
		    	if(decodedObject.data.decode("utf-8") ==button):
		    		print("ENCONTRADO")
		    		pi.set_servo_pulsewidth(pin, 1500)
		    		time.sleep(0.5)
		    		first=True
		    		lost=0
		    		movememo=False
		    		mov.gotodestination(decodedObject,servopos[pos],cap,first,pi,pin,lost,memory)
		    		
		    	cv2.putText(frame, "p0", pt[0], font, 1, (0,255,255), 2, cv2.LINE_AA)
		    	cv2.putText(frame, "p1", pt[1], font, 1, (0,255,255), 2, cv2.LINE_AA)
		    	cv2.putText(frame, "p2", pt[2], font, 1, (0,255,255), 2, cv2.LINE_AA)
		    	cv2.putText(frame, "p3", pt[3], font, 1, (0,255,255), 2, cv2.LINE_AA)
		    
		    if pos==21:
		    	print("NO HA ENCONTRADO DESTINO, MEMORIA #######################################################")	
		    	gomemory(button, cap, pi,pin,memory,qrdetected)
		    	break
		    
	#        ret, frame = cap.read() 
		    # Display the resulting frame
		    cv2.imshow('frame',frame)
		    key = cv2.waitKey(1)
		    if key & 0xFF == ord('q'):
		        break
		    elif key & 0xFF == ord('s'): # wait for 's' key to save 
		        cv2.imwrite('Capture.png', frame)  

        
        
