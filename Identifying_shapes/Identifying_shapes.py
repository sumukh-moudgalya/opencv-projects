import cv2
import matplotlib.pyplot as plt
import numpy as np

image=cv2.imread('someshapes.jpg')


#showing the image in which shape has to be identified
cv2.imshow("image",image)
cv2.waitKey(0)

#Converting to grayscale
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

#Finding the thresh of the image
ret,thresh=cv2.threshold(gray,127,255,1)

#Finding the contours
contours,heirarchy=cv2.findContours(thresh.copy(),cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)


#Sorting depending on the length of the contours and displaying the respective shape with its name
for cnt in contours:
    approx=cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
    
    if len(approx)==3:
        shape_name="Triangle"
        cv2.drawContours(image,[cnt],0,(0,255,0),-1)
        
        
        #Trying to find the center of the shape or contour
        M=cv2.moments(cnt)
        cx=int(M['m10']/M['m00'])
        cy=int(M['m01']/M['m00'])
        cv2.putText(image,shape_name,(cx-50,cy),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0),1)
        
    elif len(approx)==4:
        x,y,w,h=cv2.boundingRect(cnt)
        M=cv2.moments(cnt)
        cx=int(M['m10']/M['m00'])
        cy=int(M['m01']/M['m00'])
        
        if abs(w-h)<=3:
            shape_name="square"
            cv2.drawContours(image,[cnt],0,(255,0,0),-1)
            cv2.putText(image,shape_name,(cx-50,cy),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0),1)
        else:
            shape_name="rectangle"
            cv2.drawContours(image,[cnt],0,(255,0,0),-1)
            cv2.putText(image,shape_name,(cx-50,cy),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0),1)
    
    
    elif len(approx)==10:
        M=cv2.moments(cnt)
        cx=int(M['m10']/M['m00'])
        cy=int(M['m01']/M['m00'])
        shape_name="star"
        cv2.drawContours(image,[cnt],0,(0,255,0),-1)
        cv2.putText(image,shape_name,(cx-50,cy),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0),1)
        
    elif len(approx)>=14:
        M=cv2.moments(cnt)
        cx=int(M['m10']/M['m00'])
        cy=int(M['m01']/M['m00'])
        shape_name="circle"
        cv2.drawContours(image,[cnt],0,(255,0,0),-1)
        cv2.putText(image,shape_name,(cx-50,cy),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0),1)
cv2.imshow("shapes identified",image)
cv2.waitKey(0)


cv2.destroyAllWindows(0)


