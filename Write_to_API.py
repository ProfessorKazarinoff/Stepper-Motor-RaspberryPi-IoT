#!/usr/bin/env python
# coding: utf-8

# In[1]:


# The write_to_API code will ask a user for input that will be used to update a Thingspeak channel used to turn on a motor which will disperse fish food into the tank in the engineering lab.
# The URL to update our fish feeder channel is https://api.thingspeak.com/update?api_key=XXXXXXXXXXXXXXXX&field1=X
# This function will return the uploaded a value 1 or 0, after feeding the fish
    
def default():
    feed_or_starve = '0'                         # sets the channel upload value to 0
    write_url = f'{base_url}{api_key}{field}{feed_or_starve}'  # f string used to concatenate the url
    r = requests.get(write_url)                                #update channel to 0
# Import the API write key, stored in a .py file for security

from write_API_KEY import API_key
# Import the requests module that is needed to upload the channel

import requests
# import sleep to tell the program to wait a set amount of seconds before continuing

from time import sleep
# Construct the url used to write data to thingspeak:
# Have user decide what value to enter that will be written to thingspeak
# The variable feed_or_starve will be either a 1 or 0 that will be sent to our thingspeak channel
# The user will have the choice to feed the fish or kill the fish by starvation
    
feed_or_starve = input('To feed the fish enter "Feed", to starve the fish enter "Starve": ')
if feed_or_starve in ['Feed','feed']:
    feed_or_starve = '1'     # 1 will turn the motor on to feed the fish when input is 'feed'
elif feed_or_starve in ['Starve','starve']:
    feed_or_starve = '0'          # 0 will turn the motor off when input is 'starve'
else:
    feed_or_starve = '0'          # Incorrect inputs will keep the motor off
    
# The following parts are the components of the url
# This is the main part of the url:

base_url = 'https://api.thingspeak.com/update?api_key='    
# This defines the API write key as a variable that is used in the constructing the final write-to url:
# (it is imported from a separate .py file above)
    
api_key = API_key
# This portion is telling the code to update field 1 in the thingspeak channel:

field = '&field1='                          
# Concatenate the write url together in one string. Use the write url to update the thingspeak channel:

write_url = f'{base_url}{api_key}{field}{feed_or_starve}'
# To update the thingspeak channel with the user input to feed or starve the fish:
    
r = requests.get(write_url)
# Tell the program to wait 30 seconds before running the while loop to return the value to 0:

sleep(30)
# Run a while loop that recognizes when the channel value is a 1 and runs the default() function to return it to 0:

while feed_or_starve == '1':    # Recognizes when the channel is set to 1
    default()                   # Returns the channel to 0
    break


# In[ ]:




