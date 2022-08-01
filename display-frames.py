import cv2 as cv
import time 

webcam = cv.VideoCapture(0) 

frames = [0,0,0,0,0,0,0,0,0,0]
count_frames = 0
start = time.time()
num_frames = 0

while(1): 
    #Get webcam frame
    status, imageFrame = webcam.read() 
    
    cv.putText(imageFrame, "Frames: " + str(int(num_frames)), (0, 30), cv.FONT_HERSHEY_TRIPLEX, 0.7, (0, 0, 0))

    #count frames time
    frames[count_frames] = (time.time() - start)
    start = time.time() 
    count_frames+=1
    if count_frames >= 10: 
        num_frames = 1/(sum(frames)/10)
        count_frames=0

    #Show frame
    cv.imshow("Fist test", imageFrame)

    if not status or cv.waitKey(10) & 0xFF == ord('q'): 
        webcam.release() 
        cv.destroyAllWindows() 
        break