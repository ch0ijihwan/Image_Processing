import numpy as np

import cv2

image = np.zeros((200,400),np.uint8) #행렬 생성 200*400 = 80000개
image[:] = 200      # 회색(200)으로 생성


title1, title2 = 'Position1','Position2'
cv2.namedWindow(title1, cv2.WINDOW_AUTOSIZE)
cv2.namedWindow(title2)

cv2.moveWindow(title1,150,150)  # 윈도우 이동 - 위치 지정
cv2.moveWindow(title2,400,50)


cv2.imshow(title1,image)  #행렬 원소를 영상으로 표시
cv2.imshow(title2,image)

cv2.waitKey(0)          #키 이벤트 대기(0)
cv2.destroyAllWindows() #열린 모든 윈도우 파
