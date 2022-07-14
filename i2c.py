from smbus import SMBus
import inter_steering_angle as ISA
i2cbus = SMBus(1)
def i2c(distance):
    #car_turn_angle1 = car_turn_angle
    #car_turn_angle1 = ISA.interpolated_angle(car_turn_angle1)
    #car_turn_angle2 = car_turn_angle1
    print("distance_main_i2c_function", distance)
    #if car_turn_angle == None:
     #           if temp > 0:
     #               car_turn_angle = 90
      #          else:
       #             car_turn_angle = -90 
            
        #    temp = car_turn_angle 
    try: 
        i2cbus.write_byte(0x02, distance)
        #i2cbus.write_byte(0x01, car_turn_angle2)
        print("distance_in_if_i2c_error: ", distance)
    except:
        print("d duoc")
        pass 
