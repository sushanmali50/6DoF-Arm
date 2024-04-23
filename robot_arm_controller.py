import tkinter as tk
import RPi.GPIO as GPIO
import time
from adafruit_servokit import ServoKit
nbPCAServo=16 
grab_state = 0


#Parameters
MIN_IMP  =[500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500]
MAX_IMP  =[2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500]
MIN_ANG  =[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
MAX_ANG  =[180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180]

#Objects
pca = ServoKit(channels=16)
for i in range(nbPCAServo):
        pca.servo[i].set_pulse_width_range(MIN_IMP[i] , MAX_IMP[i])


def on_scale_change1(value1):
    pca.servo[0].angle = int(value1)
    print(f"Servo0 to {value1}")
    
def on_scale_change2(value2):
    pca.servo[1].angle = int(value2)
    print(f"Servo1 to {value2}")
    
def on_scale_change3(value3):
    pca.servo[2].angle = int(value3)
    print(f"Servo2 to {value3}")
    
def on_scale_change4(value4):
    pca.servo[3].angle = int(value4)
    print(f"Servo3 to {value4}")    

def on_scale_change5(value5):
    pca.servo[4].angle = int(value5)
    print(f"Servo4 to {value5}")
    
def button_action():
    global grab_state
    if(grab_state == 0):
        pca.servo[5].angle = 180
        grab_state = 1
        print("GRABBING")
    
    else:
        pca.servo[5].angle = 100
        grab_state = 0
        print("LET_GO")

def initialize():
    # Set the initial positions of the servos
    for i in range(nbPCAServo):
        pca.servo[i].angle = int(90)
    button_action()
    pca.servo[4].angle = 45
    time.sleep(1)
    button_action()
    pca.servo[4].angle = 135 
    time.sleep(1)      
    pca.servo[4].angle = 90
    



def shutdown_seq():
    print("Shutting down")
    pca.servo[0].angle = 90
    pca.servo[1].angle = 26
    pca.servo[2].angle = 19
    pca.servo[3].angle = 114
    pca.servo[4].angle = 85
    time.sleep(0.5)
    
    
    
initialize()   
       
window = tk.Tk()
window.title("button")

default_value1 = tk.DoubleVar(value=90)
slider1 = tk.Scale(window, variable=default_value1, from_=0, to=180, orient="horizontal", command=on_scale_change1)
slider1.grid(row=0, column=0, padx=10)

default_value2 = tk.DoubleVar(value=90)
slider2 = tk.Scale(window, from_=180,variable=default_value2, to=0, orient="vertical", command=on_scale_change2)
slider2.grid(row=0, column=1, padx=10)

default_value3 = tk.DoubleVar(value=90)
slider3 = tk.Scale(window, from_=180, to=0,variable=default_value3, orient="vertical", command=on_scale_change3)
slider3.grid(row=0, column=2, padx=10)

default_value4 = tk.DoubleVar(value=90)
slider4 = tk.Scale(window, from_=180, to=0,variable=default_value4, orient="vertical", command=on_scale_change4)
slider4.grid(row=0, column=3, padx=10)

default_value5 = tk.DoubleVar(value=90)
slider5 = tk.Scale(window, from_=180, to=0,variable=default_value5, orient="vertical", command=on_scale_change5)
slider5.grid(row=0, column=4, padx=10)

button6 = tk.Button(window, text="GRAB", command=button_action)
button6.grid(row=0, column=5, padx=10, pady=10)


window.mainloop()

shutdown_seq()