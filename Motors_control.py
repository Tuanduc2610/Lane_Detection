#!/usr/bin/enable_motorv python3
# This Code controls Dc motor and servo motor through pwm
# We defined all gpio pins in BCM mode and create a switch statment to test all
#DC motor pwm -> 0-100 (direct duty cycle)
# servo motor angle -> 0-90 ( 35 is straight , 65 is full right , 0 is full left)

#import sys
from numpy import interp

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
    


    return angle , distance
#turnOfCar() // to disconnect all channels of pwm

    