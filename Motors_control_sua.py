#!/usr/bin/enable_motorv python3
# This Code controls Dc motor and servo motor through pwm
# We defined all gpio pins in BCM mode and create a switch statment to test all
#DC motor pwm -> 0-100 (direct duty cycle)
# servo motor angle -> 0-90 ( 35 is straight , 65 is full right , 0 is full left)

#import sys
from numpy import interp
from collections import deque

distance_queue = deque(maxlen=3)
#from time import sleep
'''import RPi.GPIO as GPIO
import wiringpi

wiringpi.wiringPiSetup()
wiringpi.pinMode(22,1)
wiringpi.pinMode(23,1)
wiringpi.pinMode(24,1)
wiringpi.pinMode(25,1)

#dc_pwm,servo_pwm,servo_motor=0,0,18
#Motors Pins
motor_a = 21 
motor_b = 20
enable_motor = 16
servo_motor=18
run_car=True
prev_Mode = "Detection"
GPIO.setmode(GPIO.BCM)
    #Motors Setup
GPIO.setup(motor_a,GPIO.OUT)
GPIO.setup(motor_b,GPIO.OUT)
GPIO.setup(enable_motor,GPIO.OUT)
GPIO.setup(servo_motor, GPIO.OUT)
    #Pwm setup
dc_pwm=GPIO.PWM(enable_motor,1000)
dc_pwm.start(0)
servo_pwm=GPIO.PWM(servo_motor, 50)
servo_pwm.start(0)
if run_car:
    car_speed=90
else:
    car_speed=0
dc_pwm.ChangeDutyCycle(car_speed)
## function names are self representing 
def setServoAngle(angle):
    duty = angle / 18 + 2
    GPIO.output(servo_motor, True)
    servo_pwm.ChangeDutyCycle(duty)
    #sleep(1)
    GPIO.output(servo_motor, False)
    servo_pwm.ChangeDutyCycle(duty)
def forward():
    GPIO.output(motor_a,GPIO.HIGH)
    GPIO.output(motor_b,GPIO.LOW)
    print("forward main hun")
def backward():
    GPIO.output(motor_a,GPIO.LOW)
    GPIO.output(motor_b,GPIO.HIGH)
def stop():
    GPIO.output(motor_a,GPIO.LOW)
    GPIO.output(motor_b,GPIO.LOW)
def changePwm(x):
    dc_pwm.ChangeDutyCycle(x)
def turnOfCar():
    GPIO.cleanup()
    dc_pwm.stop()
    servo_pwm.stop()
    
def On_Cam():
    wiringpi.digitalWrite(22,1)
    wiringpi.digitalWrite(23,0)
    wiringpi.digitalWrite(24,1)
    wiringpi.digitalWrite(25,1)
def Off_Cam():
    wiringpi.digitalWrite(22,0)
    wiringpi.digitalWrite(23,1)
    wiringpi.digitalWrite(24,0)
    wiringpi.digitalWrite(25,0)'''


    

def beInLane(Max_Sane_dist,distance,curvature , Mode , Tracked_class):

    IncreaseTireSpeedInTurns = False
    global car_speed , prev_Mode
    
    
    Max_turn_angle = 80
    Max_turn_angle_neg = -80

    CarTurn_angle = 0

    if( (distance > Max_Sane_dist) or (distance < (-1 * Max_Sane_dist) ) ):
        # Max sane distance reached ---> Max penalize (Max turn Tires)
        if(distance > Max_Sane_dist):
            #Car offseted left --> Turn full wheels right
            CarTurn_angle = Max_turn_angle #+ curvature
        else:
            #Car Offseted right--> Turn full wheels left
            CarTurn_angle = Max_turn_angle_neg #+ curvature
    else:
        # Within allowed distance limits for car and lane
        # Interpolate distance to Angle Range
        Turn_angle_interpolated = interp(distance,[-Max_Sane_dist,Max_Sane_dist],[-90,90])
        print("Turn_angle_interpolated = ", Turn_angle_interpolated)
        #CarTurn_angle = Turn_angle_interpolated + curvature
        CarTurn_angle = curvature

    # Handle Max Limit [if (greater then either limits) --> set to max limit]
    if( (CarTurn_angle > Max_turn_angle) or (CarTurn_angle < (-1 *Max_turn_angle) ) ):
        if(CarTurn_angle > Max_turn_angle):
            CarTurn_angle = Max_turn_angle
        else:
            CarTurn_angle = -Max_turn_angle

    angle = CarTurn_angle
    
    global distance_queue
    distance_queue.append(distance)
    distance = (sum(distance_queue)/len(distance_queue))


    return angle , distance
#turnOfCar() // to disconnect all channels of pwm

    