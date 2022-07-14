
from Detection.Lanes.Lane_Detection import Detect_Lane
#import ROI

#import i2c
import config
if (config.debugging):
   from Code_dieu_khien.Drive import Drive_Car,Steer
   #from Code_dieu_khien.Motors_control import forward,turnOfCar,On_Cam,Off_Cam
#import i2c_comunicate as i2c

    
import cv2
import time

temp= 0
if (config.debugging):

	#cv2.namedWindow('Vid',cv2.WINDOW_NORMAL)
	cap = cv2.VideoCapture(0)
	fps = cap.get(cv2.CAP_PROP_FPS)
	frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
	
	if(frame_count==0):
		frame_count=1127
	#duration = int(frame_count / fps)
	duration = 1 
	print(fps)
	print(frame_count)
	print(duration)
	Video_pos = 35#sec
else:
    from imutils.video.pivideostream import PiVideoStream


def OnVidPosChange(val):
	global Video_pos
	Video_pos = val
	print(Video_pos)
	cap.set(cv2.CAP_PROP_POS_MSEC,Video_pos*1000)



def main():
    #print("cv2.__version__ = ",cv2.__version__)

    if (config.debugging):
        #cv2.createTrackbar('Video_pos','Vid',Video_pos,duration,OnVidPosChange)
        print("Debugging on Local Video")
    else:
        On_Cam()
        forward()
        vs = PiVideoStream().start()
        time.sleep(2.0)
    
    frame_no = 0
    Mode = "Detection"
    prev_Mode = "Detection"
    Tracked_class = 0
    tm = 0
    temp = 0
    while 1:
        
        start_detection = time.time()
        start_ = time.time()
        if(config.debugging):
            ret, frame = cap.read()# 6 ms
            
            if ret:
                frame = cv2.resize(frame,(config.Resized_width,config.Resized_height))
                #print("shape  of frame", frame.shape[0])
                #ROI= cv2.resize(frame,(config.Resized_width,config.Resized_height))
                #frame = ROI.apply_roi(ROI, ROI)
            else:
                break
        else:
            frame = vs.read().copy()
            #frame = cv2.resize(frame,(config.Resized_width,config.Resized_height))

        
        frame_orig = frame.copy()# Keep it for

        end_ = time.time()
        print("[Profiling] Read and Resize Loop took ",end_ - start_," sec <-->  ",(1/(end_ - start_+0.00001)),"  FPS ")
 
        start_getlanes = time.time()
        if config.Detect_lane_N_Draw:
            distance, Curvature = Detect_Lane(frame)
        
        end_getlanes = time.time()
        print("[Profiling] Detect_Lane Loop took ",end_getlanes - start_getlanes," sec <-->  ",(1/(end_getlanes - start_getlanes+0.00001)),"  FPS ")
        #if ((frame_no %4 )==0):
            #detect_Signs(frame_orig,frame)

        #if ( ((frame_no %2 )==0) or (prev_Mode == "Tracking") ):
        #    Mode , Tracked_class = detect_Signs(frame_orig,frame)
        #    prev_Mode = Mode
        ###start_signs = time.time()
        #Mode , Tracked_class = detect_Signs(frame_orig,frame)
        ###offset = 50
        ###frame_cropped = frame_orig[config.CropHeight_resized_crop - offset:,:]
        ###frame_to_draw_cropped = frame[config.CropHeight_resized_crop - offset:,:]
        
        ###Mode , Tracked_class = detect_Signs(frame_cropped,frame_to_draw_cropped)
        ###end_signs = time.time()
        ###print("[Profiling] detect_Signs Loop took ",end_signs - start_signs," sec <-->  ",(1/(end_signs - start_signs+0.00001)),"  FPS ")
        
        if ((config.debugging) and config.Detect_lane_N_Draw):
            Current_State = [distance, Curvature , frame , Mode , Tracked_class]
            
            distance = Drive_Car(Current_State)
            if distance == None:
                if temp > 0:
                    distance = 3
                if temp < 0:
                    distance = -3
                if temp == 0:
                    distance = 0
                
            else:
                temp = distance
            print('distance_in_Bao_Ve', distance)
            
            
            '''if (time.time() - tm >= 0.1):
                i2c.i2c(distance)
                tm = time.time()'''
            

        
        start_last = time.time()
        FPS_str = str(int(1/(time.time() - start_detection))) + " FPS "
        cv2.putText(frame,FPS_str,(frame.shape[1]-70,20),cv2.FONT_HERSHEY_DUPLEX,0.5,(0,255,255),1)

        cv2.imshow("Man_Hinh_Quan_Sat",frame)
        k = cv2.waitKey(config.waitTime)
        if k==27:
            break
        
        end_last = time.time()
        print("[Profiling] End Loop took ",end_last - start_last," sec <-->  ",(1/(end_last - start_last+0.00001)),"  FPS ")

        frame_no = frame_no + 1
        end_detection = time.time()
        print("[Profiling] Complete Loop took ",end_detection - start_detection," sec <-->  ",(1/(end_detection - start_detection)),"  FPS ")
        print(">>=======================================================================================================<< ")
        
        if config.Profiling:
            config.loopCount = config.loopCount+1
            if(config.loopCount==150):
                break
            
    if(config.debugging):
        # When everything done, release the video capture and video write objects
        cap.release()
    else:
        turnOfCar()
        Off_Cam()

    
    if (config.debugging==False):
        vs.stop() 
        
    # Closes all the frames
    cv2.destroyAllWindows()


if __name__ == '__main__':
	main()
