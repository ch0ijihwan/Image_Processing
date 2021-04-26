import cv2
import numpy as np

image = np.zeros((600,1000, 3), np.uint8)

pt_1 = ()
pt_2 = ()
capture = False

def Mouse(event, x, y, flags, param) :
    global  img_, pt1, pt2, capture

    if event == cv2.EVENT_LBUTTONDOWN :
        if capture is False:
            capture = True
            pt1 = (x, y)
        else:
            capture = False
    elif event == cv2.EVENT_LBUTTONUP:
        if capture is True:
            pt2 = (x, y)
            cv2.rectangle(image, pt1, pt2, (0, 0, 255), 5)
            cv2.imshow(img_, image)

            while True:
                ret, frame = cap.read()  # 카메라 영상 받기
                if not ret: break
                if cv2.waitKey(30) >= 0: break  # 키입력 '스페이스바' 시 종료

                frame = cv2.resize(frame, pt2, cv2.INTER_AREA)

                for i in range(pt1[1], pt2[1]):

                    for j in range(pt1[0], pt2[0]):

                        image[i][j] = frame[i - pt1[1]][j - pt1[0]]



                cv2.imshow(img_, image)


cap = cv2.VideoCapture(0)  # 0번 카메라 연결
if cap.isOpened() == False:
    raise Exception("카메라 연결 불가")

img_ = "view"
cv2.imshow(img_, image)

cv2.setMouseCallback(img_, Mouse)
cv2.waitKey(0)
capture.release()