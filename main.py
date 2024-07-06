# OpenCV Python program to detect cars in video frame
# import libraries of python OpenCV
import cv2, os
video = cv2.VideoCapture('D:/Open CV/Lesson 10/cars.mp4')
cars = 'D:/Open CV/Lesson 10/cars.xml'
car_cascade = cv2.CascadeClassifier(cars)

while True:
    (ret, im) = video.read()
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    morecars = car_cascade.detectMultiScale(gray, 1.3, 1)

    for(x,y,w,h) in morecars:
        cv2.rectangle(im, (x,y),(x + w, y + h), (255,0,0), 2)

    cv2.imshow('OpenCV', im)
    if cv2.waitKey(33) == 27:
        break
     #nuh uh

