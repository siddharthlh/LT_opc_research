from datetime import datetime
import numpy as np
import serial

a  = np.array([])
b = np.array([])



while True:
        now   = datetime.now()
        #print(datetime.timestamp(now))
        ser = serial.Serial('COM5',115200)
        y = ser.read()
        print(y)
        """x = datetime.timestamp(now)
        y = ser.read()
        a = np.append(a,x)
        b = np."""
    
    
    
