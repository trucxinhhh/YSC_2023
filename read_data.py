from NeuroPy2 import NeuroPy
from time import sleep 
import winsound as ws
import csv
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


neuroPy=NeuroPy("COM1")  
neuroPy.start()
sleep(10)
for a in range(2):
    ws.Beep(2000,500) 
Meditation = []
Attention=[]
BlinkStrength=[]

fig = plt.figure(figsize=(6, 3))
x = [0]
y = [0]
i=0
ln, = plt.plot(x, y, '-')

def update(frame):
    x.append(x[-1] + 1)
    y.append(neuroPy.attention)
 
    ln.set_data(x, y) 
    fig.gca().relim()
    fig.gca().autoscale_view() 
    return ln,
while 1:    
    i=i+1
    print ("Attention ", neuroPy.attention)
    Attention.append(neuroPy.attention)
    animation = FuncAnimation(fig, update, interval=10)
    plt.show()
    sleep(0.01)

