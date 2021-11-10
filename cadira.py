import serial
import time
import struct


print("Start")
port="/dev/rfcomm0" 
bluetooth=serial.Serial(port, 9600)
print("Connected")
bluetooth.flushInput() 
	
	
def move(dirt):
	if dirt=="F":
		data = struct.pack('>2B', 70, 19)
		bluetooth.write(data)
	elif dirt=="B":
		data = struct.pack('>2B', 70, 19)
		bluetooth.write(data)
	elif dirt=="L":
		data = struct.pack('>2B', 76, 19)
		bluetooth.write(data)
	elif dirt=="R":
		data = struct.pack('>2B', 82, 19)
		bluetooth.write(data)
	else:
		data = struct.pack('>2B', 83, 19)
		bluetooth.write(data)
		
move("F")
time.sleep(1)
move("L")
time.sleep(1)
move("F")
time.sleep(1)
move("S")
time.sleep(1)
		

	

#print("Start")
#port="/dev/rfcomm0" This will be different for various devices and on windows it will probably be a COM port.
#bluetooth=serial.Serial(port, 9600)Start communications with the bluetooth unit
#print("Connected")
#bluetooth.flushInput() This gives the bluetooth a little kick
#data = struct.pack('>2B', 70, 19)
#bluetooth.write(data)These need to be bytes not unicode, plus a number
#time.sleep(0.5)
#data = struct.pack('>2B', 66, 19)
#bluetooth.write(data)These need to be bytes not unicode, plus a number
#time.sleep(0.5)
#data = struct.pack('>2B', 76, 19)
#bluetooth.write(data)These need to be bytes not unicode, plus a number
#time.sleep(0.5)
#data = struct.pack('>2B', 82, 19)
#bluetooth.write(data)These need to be bytes not unicode, plus a number
#time.sleep(0.5)
#data = struct.pack('>2B', 83, 19)
#bluetooth.write(data)These need to be bytes not unicode, plus a number
#time.sleep(3)
#bluetooth.close() Otherwise the connection will remain open until a timeout which ties up the /dev/thingamabob
#print("Done")
