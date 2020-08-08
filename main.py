import cv2 #import opencv 

video=cv2.VideoCapture("pedestrians.mp4") #fetch the video

#inititalize the classifiers
car_classifier="car_detection.xml"
ped_classifier="peds.xml"

#load the classifiers
tracker_loader=cv2.CascadeClassifier(car_classifier)
pedestrian_loader=cv2.CascadeClassifier(ped_classifier)

#main loop
while True:
    #store each frame of the video in frame variable, success->boolean
    (success,frame)=video.read()
    #if success is true meaning the frame is readable
    if success:
        #convert it into black and white
        black_and_white_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        #else break out of the loop
    else:
        break
    
    #Detect all size of cars and pedestrians
    #returns a list of lists! each list is the x,y,w,h of single car.
    cars=tracker_loader.detectMultiScale(black_and_white_frame)
    peds=pedestrian_loader.detectMultiScale(black_and_white_frame)

    #construct a rectangle  around the car and pedestrian of thickness 2 which takes dimensions from cars and peds variables
    for (x,y,w,h) in cars:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)

    for (x,y,w,h) in peds:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

    #show the window with title Car and pedestrian tracking looping over each frame
    cv2.imshow('Car and Pedestrian Tracking',frame)

    #waitkey(1) will not immidiately close the window as we run!
    
    key=cv2.waitKey(1)
    #if key pressed is q or Q then break the loop and close the window
    if key==81 or key==113:
        break
    