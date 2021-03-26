import numpy as np
import cv2

orange, blue, cyan = (0,165,255), (255,0,0), (255,255,0)
white, black = (255,255,255), (0,0,0)

image = np.full((300,500,3), white, np.uint8) #컬러 영상 생성 및 초기화

center = (image.shape[1]//2,image.shape[0]//2)              #영상 중심 좌표 - 역순 구성
pt1, pt2 = (300,50), (100,220)
shade = (pt2[0] + 2, pt2[1] +2 )                            #그림자 좌표



cv2.circle(image, center, 100, blue)                #원그리기
cv2.circle(image, pt1, 50, orange, 2)
cv2.circle(pt2[0] + 2, pt2[1] + 2)                  #원 내부 채움

