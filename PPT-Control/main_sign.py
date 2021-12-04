import warnings
warnings.filterwarnings("ignore")
import cv2
import numpy as np
import pyautogui 
                        
# importingallcascades
handCascade=cv2.CascadeClassifier('hand.xml')
fsCascade = cv2.CascadeClassifier('fist.xml')
okCascade=cv2.CascadeClassifier('ok.xml')
faceCascade = cv2.CascadeClassifier('frontalface.xml')
capture = cv2.VideoCapture(0)

# signlanguagehandlers
#WORKING
def hand_handler(gray,handCascade):
         hand_sign=handCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5,flags=0, minSize=(100,80))
         if len(hand_sign)>0: 
                for (x,y,w,h) in hand_sign:
                        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
                pyautogui.press('pageup')
                print("HAND- Previous Slide",hand_sign)           
                return True  
         else:
                return False   
#WORKING
def fs_handler(gray,fsCascade):
        fs_sign = fsCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3,flags=0, minSize=(100,80))
        if len(fs_sign)>0:
                for (x,y,w,h) in fs_sign:
                        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),2)
                pyautogui.press('pagedown')
                print("FIST- Next Slide",fs_sign)
                return True 
        else:
                return False
        
        
#WORKING
def ok_handler(gray,okCascade):
        ok_sign = okCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3,flags=0, minSize=(100,80))        
        if len(ok_sign)>0:
                for (x,y,w,h) in ok_sign:
                        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
                pyautogui.press('f5')
                print("OK F5- Full Screen ",ok_sign)
                return True 
        else:
                return False
                        
#WORKING
def face_handler(gray,faceCascade):
        face_sign = faceCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3,flags=0, minSize=(100,80))        
        if len(face_sign)>0:
                for (x,y,w,h) in face_sign:
                        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
                pyautogui.press('esc')
                print("FaceDetecting-escaping",face_sign)
                return True 
        else:
                return False 
d=50      
while(capture.isOpened()):    
        _,img=capture.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        cv2.imshow('Feed',img)
        
        if hand_handler(gray,handCascade):
                print("StartingSkippingdFrames")
                skip_frames=d
                while(skip_frames>0):
                        _,timg=capture.read()

                        tgray = cv2.cvtColor(timg, cv2.COLOR_BGR2GRAY)
                        cv2.imshow('Feed',timg)
                        skip_frames=skip_frames-1
                print("EndingSkippingdFrames")
                 
        elif fs_handler(gray,fsCascade):
                print("StartingSkippingdFrames")
                skip_frames=d
                while(skip_frames>0):
                        _,timg=capture.read()

                        tgray = cv2.cvtColor(timg, cv2.COLOR_BGR2GRAY)
                        cv2.imshow('Feed',timg)
                        skip_frames=skip_frames-1
                print("EndingSkippingdFrames")
                
        elif ok_handler(gray,okCascade):
                print("StartingSkippingdFrames")
                skip_frames=d
                while(skip_frames>0):
                        _,timg=capture.read()

                        tgray = cv2.cvtColor(timg, cv2.COLOR_BGR2GRAY)
                        cv2.imshow('Feed',timg)
                        skip_frames=skip_frames-1
                print("EndingSkippingdFrames")
                
        elif face_handler(gray,faceCascade):
                print("StartingSkippingdFrames")
                skip_frames=d
                while(skip_frames>0):
                        _,timg=capture.read()

                        tgray = cv2.cvtColor(timg, cv2.COLOR_BGR2GRAY)
                        cv2.imshow('Feed',timg)
                        skip_frames=skip_frames-1
                print("EndingSkippingdFrames")
        else:
                pass     

        k=cv2.waitKey(1)
        if k==27:
                break        
        
        
cv2.destroyAllWindows()