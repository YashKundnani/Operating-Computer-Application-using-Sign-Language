
import keyboard
import cv2
import numpy as np
import math
import os
import time
import pyautogui
from point_sign import p_crop 
from hand_sign import hand_crop 
from fin_sign import fin_crop 
from thumbdown_sign import t_crop 


handCascade=cv2.CascadeClassifier('hand.xml')
pointCascade = cv2.CascadeClassifier('point1.xml')
finCascade=cv2.CascadeClassifier('fin_2.xml')

thumbdownCascade = cv2.CascadeClassifier('thumbdown.xml')
capture = cv2.VideoCapture(0)

while(capture.isOpened()):    
        _,img=capture.read()
        
        cv2.rectangle(img, (300,300), (100,100), (0,255,0),0)
        crop_img = img[100:300, 100:300]

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        point_sign=pointCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3,flags=0, minSize=(100,80))
        fin_sign=finCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3,flags=0, minSize=(100,80))
        hand_sign=handCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5,flags=0, minSize=(100,80))
        thumbdown_sign=thumbdownCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3,flags=0, minSize=(100,80))
       
                
        for (x,y,w,h) in point_sign:
                cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
                roi_gray=gray[y:y+h,x:x+w]
                roi_color=img[y:y+h,x:x+w]
                ha=2
                p_crop(crop_img,img)
                print("Slide Zoomed In!")

        for (x,y,w,h) in fin_sign:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
                roi_gray=gray[y:y+h,x:x+w]
                roi_color=img[y:y+h,x:x+w]
                fin_crop(crop_img,img)
                #time.sleep(0.5)
                pyautogui.press('pagedown')
                print("Slide Moved Forward!")

        for (x,y,w,h) in thumbdown_sign:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
                roi_gray=gray[y:y+h,x:x+w]
                roi_color=img[y:y+h,x:x+w]
                ha=5
                t_crop(crop_img,img)
                #time.sleep(0.5)
                pyautogui.press('pageup')
                print("Slide Moved Backward!")

        for (x,y,w,h) in hand_sign:
                cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)
                roi_gray=gray[y:y+h,x:x+w]
                roi_color=img[y:y+h,x:x+w]
                hand_crop(crop_img,img)
                #time.sleep(0.5)
                print("Slide Zoomed Out!")

                
        cv2.imshow('Feed',img)
        
        k=cv2.waitKey(10)
        if k==27:
                break
cv2.destroyAllWindows()

    
