import cv2
import numpy as np
capture = cv2.VideoCapture(0)  # 0번 카메라 연결

if capture.isOpened() == False:
    raise Exception("카메라 연결 안됨")

while True:  # 무한 반복
    ret, frame = capture.read()  # 카메라 영상 받기
    if not ret: break
    if cv2.waitKey(30) >= 0: break

    blue, green, red = cv2.split(frame)
    # cv2.add(frame[100:300,200:300],np.array)
    cv2.add(green[100:300,200:300],50,green[100:300,200:300])

    frame = cv2.merge([blue,green,red])
    pt1 = (200,100)
    pt2 = (300,300)
    cv2.rectangle(frame,pt1,pt2,(0,0,255),3,cv2.LINE_4)

    cv2.rectangle(frame, pt2, pt1, (0, 255,0), 5, cv2.LINE_4)
    title = "View Frame from Camera"
    cv2.imshow(title, frame)  # 윈도우에 영상 띄우기
capture.release()
