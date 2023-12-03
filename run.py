import time
import serial
from random import randint
import keyboard

left=0
right=0
ser = serial.Serial(
   port='COM5',
   baudrate=115200
)
def send_data(left,right): 
    ID='N79 D'
    ID2='N137 D'
    stop=' \n'
    data_left=str(left)
    frame = ID + data_left +stop
    
    data_right=str(right)
    frame2 = ID2 + data_right +stop

    ser.write(frame.encode())
    ser.write(frame2.encode())
while True:
    print("start control")
    if keyboard.is_pressed("a"):
        print("re trai")
        left= -150
        right=150
    elif keyboard.is_pressed("w"):
        print("thang")
        left=170
        right=150
        
        
    elif keyboard.is_pressed("s"):
        print("lui")
        left=-150
        right=-150
    elif keyboard.is_pressed("d"):
        print("re phai")
        left=150
        right=-150
    elif keyboard.is_pressed("q"): 
       print("stop")
       left=0
       right=0 
    print(left,right)                                                                   
    send_data(left,right)
    time.sleep(1)
