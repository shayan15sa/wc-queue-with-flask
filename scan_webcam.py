from this import d
import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar

cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_PLAIN
def scan():
    while True:
        _, frame = cap.read()

        decodedObjects = pyzbar.decode(frame)
        for obj in decodedObjects:
             #print("Data", obj.data)
            cv2.destroyAllWindows()
            d = str(obj.data.decode())
            return {"fn":d.split("^")[0],"ln":d.split("^")[1]}
            

        cv2.imshow("Frame", frame)

        key = cv2.waitKey(1)
        if key == 27:
            cv2.destroyAllWindows()
            break
