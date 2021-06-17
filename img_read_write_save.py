import cv2

image = cv2.imread("E:\opencv\images\samples\data\lena.jpg",-1) #reading a image
#print(image)

cv2.imshow("imagewindow",image) #showimg that image
k= cv2.waitKey(0)

if k==27:
    cv2.destroyAllWindows() #deleting that window
elif k==ord("s"):
    cv2.imwrite("lena_copy.png",image) #writing an image
    cv2.destroyAllWindows()

#cv2.waitKey(5000) #showing that image for 5 seconds