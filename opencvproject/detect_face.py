import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cat_cascade = cv2.CascadeClassifier('haarcascade_frontalcatface.xml')

img = cv2.imread('with2.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.3, 3)
cats = cat_cascade.detectMultiScale(gray,1.09,1)

for(x, y, w, h) in faces:
    print(x,y,w,h)
    cv2.rectangle(img,(x,y),(x+w, y+h),(255,0,0),2)

for(x, y, w, h) in cats:
    print(x,y,w,h)
    cv2.rectangle(img,(x,y),(x+w, y+h),(255,0,0),2)

print('사람 : ',str(len(faces)))
print('고양이 : ',str(len(cats)))

cv2.imshow('img', img)
cv2.waitKey()
#python detect_face.py
