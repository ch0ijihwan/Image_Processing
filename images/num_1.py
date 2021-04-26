import cv2
import numpy as np
capture = cv2.VideoCapture(0)  # 0번 카메라 연결


ix = -1
iy = -1
jx = -1
jy = -1

def onMouse(event, x, y, flags, param):  #콜백 함수 - 이벤트 내용 출력
    global ix, iy, jx, jy

    if event == cv2.EVENT_LBUTTONDOWN:
        ix = x
        iy = y
        print("마우스 왼쪽 버튼 누르기")

    elif event == cv2.EVENT_MOUSEMOVE:
        print("asdf")

    elif event == cv2.EVENT_LBUTTONUP:
        print("마우스 오른쪽 버튼 떼기")
        tx = abs(ix - x)
        ty = abs(iy - y)
        if tx > 0 and ty > 0:
            jx = tx
            jy = ty

if capture.isOpened() == False:
    raise Exception("카메라 연결 안됨")

while True:  # 무한 반복
    ret, frame = capture.read()  # 카메라 영상 받기
    if not ret: break
    if cv2.waitKey(30) >= 0: break

    if ix > 0 and iy > 0 and jx > 0 and jy > 0:
        cv2.rectangle(frame,(ix,iy,jx,jy),(0,0,255),2)

    title = "title"
    cv2.setMouseCallback(title, onMouse)
    cv2.imshow(title, frame)  # 윈도우에 영상 띄우기



capture.release()