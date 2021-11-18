import cv2
import requests

v=cv2.VideoCapture(0)
while True:
    av,fr=v.read()
    new=fr.copy()
    
    o=cv2.cvtColor(new,cv2.COLOR_BGR2GRAY)
    face=cv2.CascadeClassifier("l.xml")
    fa=face.detectMultiScale(o,scaleFactor=1.05,minNeighbors=5)
    for x,y,w,h in fa:
        img = cv2.rectangle(o,(x,y),(x+w,y+h),(0,255,0),3)
    cv2.imshow("cc",img)
    kill=cv2.waitKey(1)
    if kill==ord("k"):
        break
cv2.destroyAllWindows()
