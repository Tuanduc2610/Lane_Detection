from Code_dieu_khien.Motors_control import beInLane #,stop
import config
import cv2
#import i2c
import time
#import inter_steering_angle as ISA
import inter_angle_to_bit as ISA


#angle_of_car = 1
#car_turn_angle = 1
def Steer(Distance,Curvature,frame , Mode , Tracked_class):
    if config.Testing:
        if(Distance != -1000 | Curvature != -1000):
            if (config.debugging):
                angle_of_car , distance = beInLane(int(frame.shape[1]/2), Distance, Curvature ,Mode ,Tracked_class )
                angle_speed_str = "[ Goc ,Van_Toc ] = [ " + str(int(angle_of_car)) + " , " + str(int(current_speed)) + " ] "
                #cv2.putText(frame_disp,str(angle_of_car),(frame.shape[1]-400,50),cv2.FONT_HERSHEY_DUPLEX,1,(0,255,255),2)
                cv2.putText(frame,str(angle_speed_str),(20,20),cv2.FONT_HERSHEY_DUPLEX,0.4,(0,0,255),1)
                return distance


    else:
        if(Distance != -1000 | Curvature != -1000):
            if (config.debugging):
                
                angle_of_car, distance = beInLane(int(frame.shape[1]/3), Distance,Curvature  , Mode , Tracked_class)
                return distance

    
def Drive_Car(Current_State):
    [distance, Curvature, frame_disp, Mode, Tracked_class] = Current_State
    distance = Steer(distance, Curvature,frame_disp, Mode, Tracked_class)
    distance = 0
    print("distance_in_drive_car_function", distance)
    if distance is not None:
        distance = ISA.interpolated_angle(distance)
        #temp_angle = car_turn_angle
    else:
        distance = None
        
    #else:
     #   if temp_angle > 0:
      #      car_turn_angle = 90
       # if temp < 0:
       #     car_turn_angle = -90 

    #else:
    #    car_turn_angle = 0 
    #print("car_turn_angle: ", int(car_turn_angle))

    #i2c.i2c(car_turn_angle)
    return distance

    
    



    
