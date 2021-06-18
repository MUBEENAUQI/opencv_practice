import cv2

cap = cv2.VideoCapture(0) # accesting video capture
fourcc = cv2.VideoWriter_fourcc("X","V","I","D") #four bit to represent the video
out = cv2.VideoWriter("output.avi",fourcc,20.0,(640,480)) #no of frames per sec,size


while (cap.isOpened()): #chack if video is accessed
    ret,frame = cap.read() #getting the frame, ret (true if frame aviliable)

    if ret == True:
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

        out.write(frame)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #gray scale
        cv2.imshow("video",gray)  #showing gray frame
        cv2.imshow("video2",frame) #showing colored frame

        if cv2.waitKey(1) & 0xFF == ord("q"): #if q is pressed....exit
            break
    else:
        break

cap.release() #releasing it
out.release()
cv2.destroyAllWindows() #destroying it