# ENGR114-Fish-Feeder
## Problem Statement:
Every day of the year, a lab technician must be present in order to feed the fish housed in the Engineering Department at Portland Community College. As of today, feeding the fish on weekends and during schoolbreaks without the presence of a lab technician is not possible. Our group was tasked with creating a program in Python that could feed the fish under any circumstance. Python code was constructed and used in conjunction with a raspberry piin order to spin a motor. This motor can be instructed to turn on and off effortlessly, as long as the user has internet connection.

## Hardware Setup:
### Materials Used:

Material
Cost
Links
Raspberry pi 3+
Borrowed from PCC 
https://amzn.to/2J9xdsz
Motor Driver
Borrowed from PCC
https://bit.ly/2XMGEl0
Bipolar stepper motor
Borrowed from PCC
https://bit.ly/2s9L07Q
12V - 1A power supply
Borrowed from PCC
https://amzn.to/2XQ1GPH
5V - 2.5A power supply
Borrowed from PCC
https://amzn.to/2T1Vtg6
Female power adapter
Borrowed from PCC
https://amzn.to/2TF2ms9
Wire 
Borrowed from PCC
https://amzn.to/2VWXU5A
Mouse 
Owned
/ / / / / / / / / / / / / / / / / / / / / / / /
Keyboard
Owned
/ / / / / / / / / / / / / / / / / / / / / / / /
Monitor
Owned
/ / / / / / / / / / / / / / / / / / / / / / / /
Micro SD card
$8.99
https://amzn.to/2HhCWe3
HDMI cable
Owned
/ / / / / / / / / / / / / / / / / / / / / / / /



Hardware Schematic:

Hookup Guide:

Part
Pin
Connector
Motor Driver
GPIO 1-40
GPIO
Motor Coil 1
M1
Terminal Block
Motor Coil 2
M2
Terminal Block
Wire
Power terminal block on Motor Driver
Terminal Block
Female Power Adapter
Wire coming from power terminal block on Motor Driver
Terminal Block
Raspberry Pi Power
Raspberry pi micro USB port
Micro USB
Motor Driver/ Motor Code
Motor driver power port
DC power 



Hookup Procedure:
To begin, attach the motor driver into the Raspberry Pi by lining up the GPIO pins with the socket on the board, then apply little pressure until the board is seated properly









Identify the pairs of wires from the stepper motor that connect to coil 1 and coil 2. In the pictures below, yellow/blue is coil 1 and red/green is coil 2
Connect coil 1 to M1 and coil 2 to M2. A screwdriver will be needed to attach the wires to the terminal block









To supply power to the Motor Driver, 2 short strips of wire will have to be attached to the positive and negative power terminal blocks
The exposed ends of the now connected wires will be connect to the female power adapter. Be aware of where positive and negative are being attached to. Positive from the board must connect to positive on the adapter, and negative from the board must connect to negative on the adapter






All connections are complete and the Pi is ready to be programmed!
















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
