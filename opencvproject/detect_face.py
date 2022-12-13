import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img = cv2.imread('with2.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.3, 3)

for(x, y, w, h) in faces:
    print(x,y,w,h)
    cv2.rectangle(img,(x,y),(x+w, y+h),(255,0,0),2)

print('사람 : ',str(len(faces)))

cv2.imshow('img', img)
cv2.waitKey()
#python detect_face.py
