import numpy as np,cv2

pts1 = np.array([(100,100,1),(400,100,1), (400,250,1),(100,250,1)],np.float32)

theta = 30 * np.pi / 180 # 책에서 나온 출력 결과는 30 도로 되어있어서 30로도 바꿨습니다. 45 도는 밑에 주석 해제하면 됩니다.
#theta = 45 * np.pi / 180


m = np.array([[np.cos(theta), -np.sin(theta), 0],  #theta 만큼 회전해주기위한 행렬 생성
              [np.sin(theta),   np.cos(theta),0],
              [ 0, 0, 1]],np.float32)


delta = (pts1[2] - pts1[0])//2 # 중심점 찾기
center = pts1[0] + delta
print(center)
## 평행이동 정렬

t1 = np.eye(3, dtype=np.float32)
t2 = np.eye(3, dtype=np.float32)

t1 = pts1 - np.array([center,center,center,center]) #원점으로 평행이동한 행렬 생성

t2 = cv2.gemm(t1, m,1,None, 1, flags = cv2.GEMM_2_T) # 회전

pts2 = t2 + np.array([center,center,center,center]) # 회전 후 원래 있던 좌표로 이동 + center






for i, (pt1,pt2) in enumerate(zip(pts1,pts2)):
    print("pts1[%d] = %s, pst2[%d] = %s" %(i, pt1, i, pt2))

image = np.full((400,500,3), 255, np.uint8)
cv2.polylines(image, [np.int32(pts1[:,:2])],True,(0,255,0),2)

cv2.polylines(image, [np.int32(pts2[:,:2])],True,(255,0,0),3) # 결과
cv2.imshow("image",image)
cv2.waitKey(0)