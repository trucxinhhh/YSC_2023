from time import sleep 
import csv
import winsound as ws
import datetime
import pandas as pd
from NeuroPy2 import NeuroPy
from tensorflow.keras.models import load_model
import serial
from random import randint


Attention=[]
c=0
input = [[]]
input_to_csv=[]
count_number=[]
check_data=[]

# mo_hinh = load_model("U:/THI/YSC_2023/25_10_2023/Model/7_11_2023/train_11")
mo_hinh = load_model("U:/THI/YSC_2023/25_10_2023/Model/19_11_2023/train_10")

neuroPy=NeuroPy("COM4")  
neuroPy.start()
sleep(10)


ser = serial.Serial(
   port='COM5',
   baudrate=115200
)
def send_data(left,right): 
    ID='N79 D'
    data_left=str(left)
    stop=' \n'
    frame = ID + data_left +stop
    
    ID2='N137 D'
    data_right=str(right)
    frame2 = ID2 + data_right +stop

    ser.write(frame.encode())
    ser.write(frame2.encode())

def count(data):
    global count_number
    count_number=[0,0,0,0,0,0,0,0,0,0]
    for v in data:
        if v in [0,1,2,3,4,5,6,7,8,9,10]:
            count_number[0] += 1
        elif v in [11,12,13,14,15,16,17,18,19,20]:
            count_number[1] += 1
        elif v in [21,22,23,24,25,26,27,28,29,30]:
            count_number[2] += 1
        elif v in [31,32,33,34,35,36,37,38,39,40]:
            count_number[3] += 1
        elif v in [41,42,43,44,45,46,47,48,49,50]:
            count_number[4] += 1 
        elif v in [51,52,53,54,55,56,57,58,59,60]:
            count_number[5] += 1
        elif v in [61,62,63,64,65,66,67,68,69,70]:
            count_number[6] += 1 
        elif v in [71,72,73,74,75,76,77,78,79,80]:
            count_number[7] += 1 
        elif v in [81,82,83,84,85,86,87,88,89,90]:
            count_number[8] += 1
        elif v in [91,92,93,94,95,96,97,98,99,100]:
            count_number[9] += 1

def reset():
    count_number.clear()
    input[0].clear()
    
def control_signal(data1):
    global check_data
    data= abs(data1)
    if data <=1.2 and data > 0.98:
        print(data)
        send_data(160,150)
        print("TIEN")
        
    elif  data > 1.99 and data <= 2.2: 
        print("TRAI ")
        print(data)
        send_data(-150,150)
    elif  data > 2.9 and data <= 3.2: 
        print("phai")
        print(data)
        send_data(150,-150)
    else :
        print("STOP")
        print(data)
        send_data(0,0)

def AI_control(data):
    global  input_to_csv  
    df= pd.DataFrame(data)
    
    Y =(mo_hinh.predict(df))
    print(df)
    my_list=df.loc[:,0:9].values.tolist()
    input_to_csv.append(my_list[0].copy())
    df1=pd.DataFrame(input_to_csv)
    
    Num=[]
    
    for v in range(0,len(Y)):
        for x in Y[v]:
            Num.append(x)


    Num_final=Num[0]
    control_signal(Num_final)
    df1['lable']=Num_final

    df1.to_csv("U:/THI/YSC_2023/25_10_2023/data_19_11/data15.csv")

    reset()
    
for i in range (100):
    random = neuroPy.attention
    # random =randint(80,100)
    Attention.append(random)
    print(random)
    sleep(0.01)

while (1):
    
    time_strat = datetime.datetime.now()

    random = neuroPy.attention
    # random =randint(70,100)
    Attention.append(random)
    print(Attention)
    Attention.pop(0)
    sleep(0.01)

    count(Attention)
    for i in count_number:
        input[0].append(i)
    
    AI_control(input)
    
    time_end = datetime.datetime.now()
