import keyboard
import cv2
import numpy as np
import math
import os
import time
import pyautogui
import image_cleanup

def fin_crop(crop_img,img):
    grey = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
    
    # applying gaussian blur
    gauss_blur = image_cleanup.gaussian_method(grey)

    # thresholding: Otsu's Binarization method
    thresh_image = image_cleanup.otsu_method(gauss_blur)

    # show thresholded image
    cv2.imshow('Thresholded', thresh_image)

    # check OpenCV version to avoid unpacking error
    (version, _, _) = cv2.__version__.split('.')

    if version == '3':
        image, contours, hierarchy = cv2.findContours(thresh_image.copy(), \
               cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    else:
        contours, hierarchy = cv2.findContours(thresh_image.copy(),cv2.RETR_TREE, \
               cv2.CHAIN_APPROX_NONE)

    # find contour with max area
    max_contour = max(contours, key = lambda x: cv2.contourArea(x))

    # create bounding rectangle around the contour (can skip below two lines)
    x, y, w, h = cv2.boundingRect(max_contour)
    cv2.rectangle(crop_img, (x, y), (x+w, y+h), (0, 0, 255), 0)

    # finding convex hull
    hull = cv2.convexHull(max_contour)

    # draw_contours contours
    draw_contours = np.zeros(crop_img.shape,np.uint8)
    cv2.drawContours(draw_contours, [max_contour], 0, (0, 255, 0), 0)
    cv2.drawContours(draw_contours, [hull], 0,(0, 0, 255), 0)

    # finding convex hull
    hull = cv2.convexHull(max_contour, returnPoints=False)

    # finding convexity defects
    convex_defects = cv2.convexityDefects(max_contour, hull)
    count_convex_defects = 0
    cv2.drawContours(thresh_image, contours, -1, (0, 255, 0), 3)

    # applying Cosine Rule to find angle for all convex_defects (between fingers)
    # with angle > 90 degrees and ignore defects
    for i in range(convex_defects.shape[0]):
        s,e,f,d = convex_defects[i,0]

        start = tuple(max_contour[s][0])
        end = tuple(max_contour[e][0])
        far = tuple(max_contour[f][0])
        if d>10000:
            count_convex_defects+=1

        
        # find length of all sides of triangle


    # define actions required

    count_convex_defects+=1   
    if count_convex_defects == 1:
        keyboard.press_and_release('right')
        

    else:
        cv2.putText(img,"0", (50, 50),\
            cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
    ha=0
    
    #time.sleep(1)
    # show appropriate images in windows
    #cv2.imshow('Gesture', img)
    all_img = np.hstack((draw_contours, crop_img))
    cv2.imshow('Contours', all_img)
