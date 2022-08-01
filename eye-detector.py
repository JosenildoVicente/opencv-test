import cv2 as cv
import time 

xml_haar_cascade = 'classifier/haarcascade_eye.xml'

webcam = cv.VideoCapture(0) 
webcam.set(cv.CAP_PROP_FRAME_WIDTH, 320)
webcam.set(cv.CAP_PROP_FRAME_HEIGHT, 240)

frames = [0,0,0,0,0,0,0,0,0,0]
count_frames = 0
start = time.time()
num_frames = 0

faceClassifier = cv.CascadeClassifier(xml_haar_cascade)

while(1): 
    #Get webcam frame
    status, imageFrame = webcam.read() 

    gray_image = cv.cvtColor(imageFrame,cv.COLOR_BGR2GRAY)

    eye = faceClassifier.detectMultiScale(gray_image)
    # print(eye)
    for x, y, w, h in eye:
        cv.rectangle(imageFrame, (x,y), (x+w, y+h), (0,0,0),2)
        cv.circle(imageFrame, (x+int(w/2),y+int(h/2)), 1, (0,0,255), -1)

    #Put frames number on image
    cv.putText(imageFrame, "Frames: " + str(int(num_frames)), (0, 30), cv.FONT_HERSHEY_TRIPLEX, 0.7, (0, 0, 0))

    #count frames time
    frames[count_frames] = (time.time() - start)
    start = time.time() 
    count_frames+=1
    if count_frames >= 10: 
        num_frames = 1/(sum(frames)/10)
        count_frames=0

    #Show frame
    cv.imshow("Color image", imageFrame)

    if not status or cv.waitKey(10) & 0xFF == ord('q'): 
        webcam.release() 
        cv.destroyAllWindows() 
        break