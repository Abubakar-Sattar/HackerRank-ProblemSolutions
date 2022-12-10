#This script simply send whatsapp message to specified number ...

"""
Requirement;
pywhatkit package(Install using command :- pip install pywhatkit)
you should keep login on whatsapp web before running this script 

"""

import pywhatkit
pywhatkit.sendwhatmsg("+919xxxxxxxxx","HI there, sending whatsapp message using python",18, 30)

"""
sendwhatmsg contains 4 aruguments:
1 - mobile number of receiver along with country code;
2 - message you wish to send to receiver
3 - hours in 24 hours format
4 - minutes 
"""
