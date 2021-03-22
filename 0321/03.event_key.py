import numpy as np
import cv2

## switch case 문을 사전 (dictionary)으로 구현

switch_case = {
    ord('a') : "a키 입력",
    ord('b') : "b키 입력",
    0x41: "A키 입력",
    int('0x42',16) : "B키 입력", # 0x42(16진수) -> 10진수 변환
    2424832: "왼쪽 화살표키 입력 ", # 0x250000  # 이거 윈도우 기준 같음 맥은 안먹음
    2490368: "윗쪽 화살표키 입력" , # 0x260000
    2555904: "오른쪽 화살표키 입력",# 0x270000
    2621440: "아래쪽 화살표키 입력", #0x280000


}

image = np.ones((200,300), np.float) #원소값 1인 행렬 생성
cv2.namedWindow('Keyboard Event') #윈도우 이름
cv2.imshow("Keyboard Event", image)


while True:
    key = cv2.waitKeyEx(100)
    if key == 27: break #ESC키 누르면 종료

    try:
        result = switch_case[key]
        print(result)
    except KeyError:
        result = -1
