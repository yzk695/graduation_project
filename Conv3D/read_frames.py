import cv2 as cv

path = "G:/Graduation_Project/video-classification-master/UCF8/v_Basketball_g25_c07.avi"

capture = cv.VideoCapture(path)

print(capture.get(7))