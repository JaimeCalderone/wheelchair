#####################################################################################################
#                                                                                                   #
#   This is the first fucntion that the system runs, here you can find the loop that waits for a    #
#   key to be pressed (destination) to start the function that search for the destination           #
#                                                                                                   #
#####################################################################################################


import pyzbar.pyzbar as pyzbar
import pigpio
import numpy as np
import cv2 
import time
import math
import keyboard  
import search as s
import memory as m
import sys
sys.setrecursionlimit(10000)
#from projecte import detect
																															  

def wait4key():
    buttonpressed='Null'
    while buttonpressed=='Null':  # While a key is not pressed, run the loop
        try:  # used try so that if user pressed other than the given key error will not be shown
            if keyboard.is_pressed('x') or keyboard.is_pressed('a') or keyboard.is_pressed('s') or keyboard.is_pressed('w'):  # if key 'q' is pressed 
                print('BOTON_1!')
                buttonpressed='1'  #Assign that the first button has been pressed
                break 
            elif keyboard.is_pressed('y') or keyboard.is_pressed('g') or keyboard.is_pressed('h'):  # if key 'q' is pressed 
                print('BOTON_2!')
                buttonpressed='2'   #Assign that the second button has been pressed
                break
            elif keyboard.is_pressed('p') or keyboard.is_pressed('o') or keyboard.is_pressed('l'):  # if key 'q' is pressed 
                print('BOTON_3!')
                buttonpressed='3'   #Assign that the third button has been pressed
                break
            elif keyboard.is_pressed('1') or keyboard.is_pressed('5') or keyboard.is_pressed('4') or keyboard.is_pressed('8'):  # if key 'q' is pressed 
                print('BOTON_4!')
                buttonpressed='4'   #Assign that the third button has been pressed
                break
        except:
            b=0
    return buttonpressed  # The function returns which button or part of the keyboard has been pressed

def main():
    #
    #   Main function of Buttons.py
    #
    #   Get the webcam, set parameters
    cap = cv2.VideoCapture(0)   #Camera source (in the case that you want to choose among different cameras connected)
    cap.set(cv2.CAP_PROP_FPS, 40)   #Frames per second, it will impact on the system performance
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)  #Image width, it will impact on the system performance
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 960) #Image height, it will impact on the system performance
    #cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)
    time.sleep(2)

	#   Set the GPIO pin that controlls the servo motor that turn the camera																	
    pi = pigpio.pi()
    pin=17

    #Function that waits for a key to be pressed
    button = wait4key()
    # print(button)																														  

    ##################################################################################################################################
    #   This function fills a memory with information that can be userful for the system to arrive at points of the room that are
    #   not visible when the user choose it as the destination.
    ##################################################################################################################################

    memory = []#m.scan(cap,pi,pin) DESCOMENTAR PARA USAR MEMORIA Y LLENARLA AL PRINCIPIO

    print("################# MEMORY ################")
    print(memory) #Print the memory information about the destination that are visible

	##################################################################################################################################
    #   Start the search, this function calls the function s in the file search.py to start the searching of the destination according
    #   to the destination selected, the camera variable (cap) to continue using the camera inside search.py, the gpio pin variable
    #   and the memory variable to use it if its necessary
    ##################################################################################################################################																																  
    s.s(button,cap,pi,pin,memory)
    
def main2(cap, pi,pin,memory):
    print("hola1")
    button = wait4key()
    # print(button)
    s.s(button,cap, pi,pin,memory)

if __name__ == "__main__":
    main()
