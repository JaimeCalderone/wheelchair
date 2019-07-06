import pyzbar.pyzbar as pyzbar
import pigpio
import numpy as np
import cv2 
import time
import math
import keyboard  # using module keyboard
import search as s
import memory as m
import sys
sys.setrecursionlimit(10000)
#from projecte import detect



def wait4key():
    print("hola2")
    buttonpressed='Null'
    while buttonpressed=='Null':  # making a loop
        try:  # used try so that if user pressed other than the given key error will not be shown
            if keyboard.is_pressed('x') or keyboard.is_pressed('a') or keyboard.is_pressed('s') or keyboard.is_pressed('w'):  # if key 'q' is pressed 
                print('BOTON_1!')
                buttonpressed='1'
                break 
            elif keyboard.is_pressed('y') or keyboard.is_pressed('g') or keyboard.is_pressed('h'):  # if key 'q' is pressed 
                print('BOTON_2!')
                buttonpressed='2'
                break
            elif keyboard.is_pressed('p') or keyboard.is_pressed('o') or keyboard.is_pressed('l'):  # if key 'q' is pressed 
                print('BOTON_3!')
                buttonpressed='3'
                break
            elif keyboard.is_pressed('1') or keyboard.is_pressed('5') or keyboard.is_pressed('4') or keyboard.is_pressed('8'):  # if key 'q' is pressed 
                print('BOTON_4!')
                buttonpressed='4'
                break
        except:
            b=0
    return buttonpressed

def main():
    # get the webcam:
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FPS, 40)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    #cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)
    time.sleep(2)

    pi = pigpio.pi()
    pin=17


    print("hola1")
    button = wait4key()
    # print(button)
    memory = m.scan(cap,pi,pin)
    print("################# MEMORY ################")
    print(memory)
    s.s(button,cap,pi,pin,memory)
    
def main2(cap, pi,pin,memory):
    print("hola1")
    button = wait4key()
    # print(button)
    s.s(button,cap, pi,pin,memory)

if __name__ == "__main__":
    main()
