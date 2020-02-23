#!/usr/bin/env python
# coding: utf-8

# In[106]:


import numpy as np
import cv2
import copy


def contour_generate_(frame):
    im = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    blur_img = cv2.GaussianBlur(im, (5,5), 0)
    edge = cv2.Canny(blur_img,127,200)
    edge1 = copy.copy(edge)
    contours,hierarchy = cv2.findContours(edge1, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    
    hierarchy = hierarchy[0] #innermost contours
    
    contours_ = list()
    corner_list = list()
    ext_index =list() 
    contour_list = list()
            
    for h in hierarchy:
        if h[3] != -1:
            ext_index.append(h[3]) #index of all the parent 
    
    #Looping over the exterior contours
    for i in ext_index:
        perimeter = cv2.arcLength(contours[i],True)
        approx = cv2.approxPolyDP(contours[i],0.01*perimeter,True)
        
        if len(approx) > 4: #If more than 4 corners detected, take the previous values into consideration
            peri = cv2.arcLength(contours[i-1],True)
            corners = cv2.approxPolyDP(contours[i-1], 0.02*peri, True)
            corner_list.append(corners)
    
    #Append valid corners into contour list
    for corner in corner_list:
        if len(corner) == 4:
            contour_list.append(corner)

    for contour in contour_list:
        area = cv2.contourArea(contour)
        #print("Area = ",area)
        
        #The following needs tuning
        if area > 300 and area < 7000: #Need to tune these
            #print("length contours: ",len(contours))
            contours_.append(contour)
    
    cont_img = cv2.drawContours(frame, contours_, -1, (0,255,0),2)    
    cv2.imshow('AR Tag - Detected',cont_img)
   


# In[108]:


cap = cv2.VideoCapture('/home/akhopkar/Downloads/Tag2.mp4')
if cap.isOpened() == False:
    print("Error loading")

while cap.isOpened():
    ret,frame = cap.read()
    if ret == False:
         break
    img = cv2.resize(frame, (0,0),fx = 0.5, fy = 0.5)
    contour_generate_(img)
    if cv2.waitKey(5) & 0xFF == 27:
         break
            
cap.release()
cv2.destroyAllWindows()


# In[ ]:





# In[ ]:




