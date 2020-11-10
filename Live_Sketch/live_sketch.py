#importing the required libraries
import cv2
import matplotlib.pyplot as plt
import numpy as np

#function sketch to plot the sketch of the image
def sketch(image):
    
    #function to convert bgr image to gray scale
    img_gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    
    #function to blur the image in order to increase speed and effeciency
    img_blur=cv2.GaussianBlur(img_blur,(5,5),0)
    
    #Applying canny algorithm to determine the edges in the image
    img_edge=cv2.Canny(image,70,255,cv2.THRESH_BINARY_INV)
    
    #Returning the final image
    return img_edge

#Capturing the video feed of the camera
cap=cv2.VideoCapture(0)

#Continously displaying the image
while True:
    
    #reading the image; if ret==True then image is being returned by the camera
    ret,frame=cap.read(0)
    
    #Displaying the image 
    cv2.imshow('live sketch',sketch(frame)
    
    #Terminating or closing the window when enter key is pressed
    if cv2.waitKey(1)==13:
        break
               
               
#Stopping the video feed
cap.release()

#Destroying any open Windows
cv2.destroyAllWindows()