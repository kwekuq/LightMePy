#!/usr/bin/python
#Filename: LightMePy.py

__author__ = 'kwekuq'
import time
import RPi.GPIO as GPIO

lights_list = [1,23,24,25]
duration = 1
#Setting up the board so we can light it up!
def setup(light_list) :
    GPIO.setmode(GPIO.BOARD)
    for x in range(light_list.max) :
        GPIO.setup(lights_list[x],GPIO.output)
    print('GPIO Board setup for lighting!')


def blink(port) :
    GPIO.output(int(port),True)
    time.sleep(duration)
    GPIO.output(int(port),False)
    time.sleep(duration)
    GPIO.cleanup()

def warning(portOne,portTwo) :
    GPIO.output(int(portOne),True)
    time.sleep(duration)
    GPIO.output(int(portOne),False)
    GPIO.output(int(portTwo),True)
    time.sleep(duration)
    GPIO.output(int(portTwo),False)
    time.sleep(duration)
    GPIO.cleanup()

def on(port) :
    GPIO.output(int(port),True)

def off(port) :
    GPIO.output(int(port),False)
    GPIO.cleanup()

def period(repetitions,port, function) :
    for X in range(repetitions):
        if function == "on" :
            on(port)
        elif function =="blink" :
            blink(port)
    off(port)



#The current version of LightMePy
version = "0.3"