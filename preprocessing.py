import random
from time import sleep
import pandas as pd
c=0
input = []
input_to_csv=[]
count_number=[]
from NeuroPy2 import NeuroPy

neuroPy=NeuroPy("COM4")  
neuroPy.start()
sleep(10)
for a in range(2):
    print("start")

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
    input.clear()
bien_dem=0
Attention=[]
for i in range (100):
    random = neuroPy.attention
    Attention.append(random)
    print(random)
    sleep(0.01)
while bien_dem < 5000:

    random = neuroPy.attention
    print(neuroPy.attention)
    Attention.append(random)
    print(Attention)
    Attention.pop(0)
    sleep(0.01)
    print(Attention)
    count(Attention)
    for i in count_number:
        input.append(i)
    input_to_csv.append(input.copy())
        
    reset()
    df=pd.DataFrame(input_to_csv)
    df.to_csv("U:/THI/YSC_2023/25_10_2023/data_6_11/data6.csv")
    bien_dem +=1
neuroPy.stop()
print("finish")