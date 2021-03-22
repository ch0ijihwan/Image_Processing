import numpy as np
import cv2

image = np.zeros((200,300),np.uint8) #ndarray 행렬 생성
image.fill(255)# 흰 색

title1,title2 = 'AUTOSIZE', 'NORMAL'
cv2.namedWindow(title1,cv2.WINDOW_AUTOSIZE)
cv2.namedWindow(title2,cv2.WINDOW_NORMAL)

cv2.imshow(title1, image) # 영상으로 표시
cv2.imshow(title2, image)
cv2.resizeWindow(title1,700,700) # 오토사이즈라 변경 불가  # 윈도우에선 색은 그대로고 그 창만 커지는거 같음. 200,300안은 흰색이고 그 외에 커진 부분은 회색
cv2.resizeWindow(title2,700,700)

cv2.waitKey(0)
cv2.destroyAllWindows()