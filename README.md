# ENGR114-Fish-Feeder
## Problem Statement:
A lab technician needs to feed his fish every day of the year, including weekends and on vacation. As of today, that is not possible. Our group was tasked with creating a system that could feed the fish under any circumstances.  Python can be used to interact with a Raspberry Pi to start a motor, as long as the user  has an internet connection

## Future Work:
The motor does not include a mechanism to physically feed the fish, only the motion to do so. A mechanism needs to be created to physically feed the fish. There are some issues with connecting the Raspberry Pi to the school’s wifi since it’s so secure. One work around could be created by connecting the Pi a mobile hotspot via smartphone. A more permanent solution would involve connecting the Pi to the school’s wifi.

## Code:
The Write_to_API.py file is used by a laptop to write to Thingspeak.com. The file uploads a 0 when you type 'Starve' and a 1 when you type 'Feed'. After it sends a 1, waits for 30 seconds before sending a 0 so that the motor doesn't spin forever.
https://github.com/zeinsadek/ENGR114-Fish-Feeder-/blob/master/Write_to_API.py

The Raspberry_Pi_Read_API.py file has the function read_api which reads the data coming thingspeak.com. It will produce either a 0 or a 1.
https://github.com/zeinsadek/ENGR114-Fish-Feeder-/blob/master/Raspberry_Pi_Read_API.py

The Raspberry_Pi_Motor_Code uses the Adafruit Motor HAT Python Library to run the motor. It contains a for loop that reads thingspeak.com for 2 minutes. It uses the read_api function to read thingspeak.com. When a 1 is sent it runs the code to make the motor spin. It then sleeps for 30 seconds, allowing the Write_to_API file to send a 0. Once 2 minutes has passed the loop ends. The turnOffMotor function turns the motor off after it has spun so it does note over-heat.
https://github.com/zeinsadek/ENGR114-Fish-Feeder-/blob/master/Raspberry_Pi_Motor_Code.py


## Resources to Help with Future Work: 
(Setting WiFi up for Raspberry Pi) 

https://bit.ly/1Qy1xZm

(Adafruit DC and Stepper Motor HAT for Raspberry Pi)  

https://bit.ly/2u741rK 
