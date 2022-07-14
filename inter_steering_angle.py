import numpy as np
angle_threshold= [10, 20, 50, 80, 90]
neg_angle_threshold= [-90, -80, -50, -20, -10]


def interpolated_angle(car_turn_angle):
    if car_turn_angle is not None:
        if (((car_turn_angle >= 0) and (car_turn_angle < 10)) or ((car_turn_angle <= 0) and (car_turn_angle > -10))):
            car_turn_angle = 0

        elif (car_turn_angle > 10) :
            for i in range(0, 4, 1) :

                if ((car_turn_angle > angle_threshold[i]) and ((car_turn_angle < angle_threshold[i+1]))):
                    car_turn_angle = (angle_threshold[i] + angle_threshold[i+1])/2
                    break
                elif (car_turn_angle == angle_threshold[i]):
                    car_turn_angle = angle_threshold[i]
                    break
                elif (car_turn_angle >90 ):
                    car_turn_angle = 90
                    break


        else:
            for i in range(0, 4, 1) :
                if ((car_turn_angle >= neg_angle_threshold[i]) and ((car_turn_angle < neg_angle_threshold[i+1]))):
                    car_turn_angle = (neg_angle_threshold[i] + neg_angle_threshold[i+1])/2
                    break

                elif (car_turn_angle == neg_angle_threshold[i]):
                    car_turn_angle = neg_angle_threshold[i]
                    break

                elif (car_turn_angle <-90):
                    car_turn_angle = -90
                    break

    return car_turn_angle







