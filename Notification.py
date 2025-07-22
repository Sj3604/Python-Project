# this module is for the invoking the notification 
from plyer import notification
# this module is for calling up the time module 
import time 

if __name__ =="__main__":
    while True:
    #  this is the function in which there will be 4 paramters 
     notification.notify(title = "*** Have Some Rest! ***",
                        message = "Taking short breaks refreshes you a lot! ",
                        app_icon = r"C:\Users\Vishal Infotech\Downloads\hey.ico",timeout = 5)
     time.sleep(50) 
     
