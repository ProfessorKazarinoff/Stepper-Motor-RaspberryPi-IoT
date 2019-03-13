#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Run to install the Adafruit-Motor-HAT-Python-Library
git clone https://github.com/adafruit/Adafruit-Motor-HAT-Python-Library

# Code that reads Thingspeak.com and makes the motor run
from Adafruit_MotorHAT import Adafruit_MotorHAT
# Import a function from the read_api file that will continuously read thingspeak
from api import read_api 
from time import sleep
import atexit

mh = Adafruit_MotorHAT()  

# This function is to release the motors after the code is done running so that they don’t overheat

def turnOffMotors():      
    mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

atexit.register(turnOffMotor)

myStepper = mh.getStepper(200,1)
myStepper.setSpeed(30)

# Create a for loop that continuously reads thingspeak for 2 minutes
for i in range(240):
    values=int(read_api())
# When the loop receives a 1, it makes the motor run, then sleep for 30 seconds
    if values == 1:  
        print('Nemo is being Fed')
        my.Stepper.step(300, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.SINGLE)
        turnOffMotors()
        sleep(30)
        continue
# If the loop receives a 0, it simply continues the loop until the 2 minutes is up
    elif values == 0:
        continue


# In[ ]:




