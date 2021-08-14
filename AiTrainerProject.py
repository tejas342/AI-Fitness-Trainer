import cv2
import numpy as np
import time
import PoseModule as pm

cap = cv2.VideoCapture(0)

pTime = 0
detector = pm.poseDetector()
count = 0
dir = 0

while True:
    success, img = cap.read()
    #img = cv2.flip(img, 1)     #uncomment this to make it for left hand
    img = cv2.resize(img, (1280, 720))
    img = detector.findPose(img, False)
    lmList = detector.findPosition(img, False)
    #print(lmList)
    
    if len(lmList) != 0:
        angle = detector.findAngle(img, 12, 14, 16)     #right hand
        per = np.interp(angle, (210, 310), (0, 100))
        bar = np.interp(angle, (220, 310), (600, 200))

        #check for the dumbell curl
        color = (255, 0, 255)
        if per == 100:
            color = (0, 255, 0)
            if dir == 0:
                count += 0.5
                dir = 1
        if per == 0:
            color = (0, 255, 0)
            if dir == 1:
                count += 0.5
                dir = 0
        print(count)

        # drawing bar
        cv2.rectangle(img, (1100, 200), (1155, 600), color, 2)
        cv2.rectangle(img, (1100, int(bar)), (1155, 600), color, cv2.FILLED)
        cv2.putText(img, f'{int(per)} %', (1100, 175), cv2.FONT_HERSHEY_PLAIN, 2.5, color, 3)

        # drawing curl bar
        cv2.rectangle(img, (0, 550), (250, 720), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, f'{int(count)}', (35, 680), cv2.FONT_HERSHEY_PLAIN, 8, (255, 0, 0), 8)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, f'FPS : {int(fps)}', (50, 100), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
