from __future__ import print_function
import functions as f
import routes as r
from puente_H import motors
import search
import pyzbar.pyzbar as pyzbar
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
    
def moveleft():
    move("L")
    time.sleep(0.15)
    move("S")
    time.sleep(0.1)

def moveright():
    move("R")
    time.sleep(0.15)
    move("S")
    time.sleep(0.1)

def moveleft2():
    move("L")
    print("MOVELEFT2")
    time.sleep(0.10)
    move("S")
#    time.sleep(0.1)

def moveright2():
    move("R")
    print("MOVERIGHT2")
    time.sleep(0.10)
    move("S")
#    time.sleep(0.1)
    

##################################################################################################################################
#   This function performs the movements to arrive at the final destination
##################################################################################################################################   
def gotodestination(dest,pos,cap,first,pi,pin,lost,memory):
    
    print("dentro de godestination")

    font = cv2.FONT_HERSHEY_SIMPLEX

    while(True):
        # Capture frame-by-frame
        
        
            
        for i in range(4):
        	cap.grab()
        ret, frame = cap.read()
        for i in range(4):
        	cap.grab()

        
        # Our operations on the frame come here
        im = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        height, width = im.shape
        # print(height,width)
        totalpixels=height*width
        
        decodedObjects = decode(im)
        print("decodedobjects:")
        if not decodedObjects:
            print("NO HAY NADAAAAAAA")
            print("lost: "+str(lost))
            if lost>12:
            	search.s(dest.data.decode("utf-8"),cap, pi,pin,memory) #Search again for the destination
            lost+=1
            

                    
        for decodedObject in decodedObjects:
            points = decodedObject.polygon

            # If the points do not form a quad, find convex hull
            if len(points) > 4 : 
                hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
                hull = list(map(tuple, np.squeeze(hull)))
            else : 
                hull = points;
            
            # Number of points in the qconvex hull
            n = len(hull)     
            # Draw the convext hull
            for j in range(0,n):
                cv2.line(frame, hull[j], hull[ (j+1) % n], (255,0,0), 3)            

            pt, xmedia, ymedia = f.getPoints(decodedObject.polygon)
            distance, dist, qrsize = f.getSize(decodedObject, totalpixels)
            orientation = f.getOrientation(points, dist)


            if(decodedObject.data.decode("utf-8")==dest.data.decode("utf-8")):
                first=False
                lost=0
                print("Ancho imagen : "+str(width))
                print("X media : "+str(xmedia))
                if xmedia<180:
                    moveleft2()
                elif xmedia>780:
                    moveright2()
                else:
                	r.rmove(qrsize,orientation,dest,pos,cap,pi,pin,lost,memory)
                first=False
            else:
            	move("S")
             
        print(pos)
        if first:
        	print("giro buscar POS: ")
        	print(pos)
        	if pos<=1500:
        		print("giro iq")
        		moveright()
        		time.sleep(1)
        	else:
        		print("giro dr")
        		moveleft()
        		time.sleep(1)
        		
        

                    
            # print('distance= ', distance) 
            # print('state= ', state) 
            # print(points)
            # print(x, y)
            # print('Type : ', decodedObject.type)
            # print('Data : ', decodedObject.data,'\n')
            # cv2.putText(frame, barCode, (x, y), font, 1, (0,255,255), 2, cv2.LINE_AA)
            #cv2.putText(frame, "p0", pt[0], font, 1, (0,255,255), 2, cv2.LINE_AA)
            #cv2.putText(frame, "p1", pt[1], font, 1, (0,255,255), 2, cv2.LINE_AA)
            #cv2.putText(frame, "p2", pt[2], font, 1, (0,255,255), 2, cv2.LINE_AA)
            #cv2.putText(frame, "p3", pt[3], font, 1, (0,255,255), 2, cv2.LINE_AA)

                
        # Display the resulting frame
        cv2.imshow('frame',frame)
        key = cv2.waitKey(1)
        if key & 0xFF == ord('q'):
            break
        elif key & 0xFF == ord('s'): # wait for 's' key to save 
            cv2.imwrite('Capture.png', frame)  

   

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
    
    
#The same as destination but using memory 
def gotomemodestination(dest,pos,cap,first,pi,pin,lost,memory,el2,movememo,button):
    
    print("dentro de godestination MEMO")

    font = cv2.FONT_HERSHEY_SIMPLEX

    while(True):
        # Capture frame-by-frame
        
        
            
        for i in range(4):
        	cap.grab()
        ret, frame = cap.read()
        for i in range(4):
        	cap.grab()

        
        # Our operations on the frame come here
        im = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        height, width = im.shape
        # print(height,width)
        totalpixels=height*width
        
        decodedObjects = decode(im)
        print("decodedobjects MEMO:")
        if not decodedObjects:
            print("NO HAY NADAAAAAAA MEMO")
            print("lost: "+str(lost))
            if lost>12:
            	search.s(button ,cap, pi,pin,memory)
            lost+=1
            

                    
        for decodedObject in decodedObjects:
            points = decodedObject.polygon

            # If the points do not form a quad, find convex hull
            if len(points) > 4 : 
                hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
                hull = list(map(tuple, np.squeeze(hull)))
            else : 
                hull = points;
            
            # Number of points in the qconvex hull
            n = len(hull)     
            # Draw the convext hull
            for j in range(0,n):
                cv2.line(frame, hull[j], hull[ (j+1) % n], (255,0,0), 3)            

            pt, xmedia, ymedia = f.getPoints(decodedObject.polygon)
            distance, dist, qrsize = f.getSize(decodedObject, totalpixels)
            orientation = f.getOrientation(points, dist)


            if(el2[0]==int(dest.data.decode("utf-8"))):
                first=False
                lost=0
                print("Ancho imagen MEMO: "+str(width))
                print("X media: "+str(xmedia))
                if xmedia<260:
                    moveleft2()
                elif xmedia>390:
                    moveright2()
                else:
                	r.movememo(decodedObject,qrsize,orientation,dest,pos,cap,pi,pin,lost,memory,el2,movememo,button)
                first=False
            else:
            	move("S")
             
        print(pos)
        if first:
        	print("giro buscar MEMO")
        	if pos<=1500:
        		print("giro iq")
        		moveleft()
        	else:
        		print("giro dr")
        		moveright()
        		
        

                    
            # print('distance= ', distance) 
            # print('state= ', state) 
            # print(points)
            # print(x, y)
            # print('Type : ', decodedObject.type)
            # print('Data : ', decodedObject.data,'\n')
            # cv2.putText(frame, barCode, (x, y), font, 1, (0,255,255), 2, cv2.LINE_AA)
            #cv2.putText(frame, "p0", pt[0], font, 1, (0,255,255), 2, cv2.LINE_AA)
            #cv2.putText(frame, "p1", pt[1], font, 1, (0,255,255), 2, cv2.LINE_AA)
            #cv2.putText(frame, "p2", pt[2], font, 1, (0,255,255), 2, cv2.LINE_AA)
            #cv2.putText(frame, "p3", pt[3], font, 1, (0,255,255), 2, cv2.LINE_AA)

                
        # Display the resulting frame
        cv2.imshow('frame',frame)
        key = cv2.waitKey(1)
        if key & 0xFF == ord('q'):
            break
        elif key & 0xFF == ord('s'): # wait for 's' key to save 
            cv2.imwrite('Capture.png', frame)  

   

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
