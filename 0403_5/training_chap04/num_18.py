import numpy as np
import cv2

red, blue, cyan = (0,0,255), (255,0,0), (255,255,0)
white, black = (255,255,255), (0,0,0)
image = np.full((300, 700, 3), white, np.uint8)   # 가로 700 세로 300 캔버스 생

center = (image.shape[1]//2,image.shape[0]//2)
center1 = (image.shape[1] - 60 //2,image.shape[0]//2)
center2 = ((image.shape[1]//2) + 60,image.shape[0]//2)
size1 = (120, 120)
size2 = (60,60)# 타원 크기 - 반지름 값임 (장축,단축)
                 # 타원의 중심점(2화소 원) 표시


cv2.ellipse(image, center, size1,  0, 180, 360, red, -1)      # 타원 그리기   (이미지, 좌표, 사이즈(장단축), 타원의 각도, 호의 시작각, 엔딩각,색,굵기)

cv2.ellipse(image, center2, size2,  0, 0, 360, blue, -1)      # 타원 그리기   (이미지, 좌표, 사이즈(장단축), 타원의 각도, 호의 시작각, 엔딩각,색,굵기)
cv2.ellipse(image, center, size1,  0, 0, 180, blue, -1)
cv2.ellipse(image, (image.shape[1]//2 - 60,image.shape[0]//2), size2,  0, -180, -360, red, -1)


cv2.imshow("Draw Eclipse & Arc", image)
cv2.waitKey()                                           # 키입력 대기
