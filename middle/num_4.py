import numpy as np, cv2

image1 = cv2.imread("images/add1.jpg")  # 영상 읽기
image2 = cv2.imread("images/add2.jpg")
image3 = cv2.imread("images/add3.jpg")


def onMouse(value):  # 줌 조절 함수
    pass


if image1 is None or image2 is None or image3 is None:
    raise Exception("영상 파일 읽기 오류")

cv2.namedWindow('image1')
cv2.createTrackbar('Mixing1', 'image1', 0, 100, onMouse)
mix1 = cv2.getTrackbarPos('Mixing1', 'image1')



cv2.createTrackbar('Mixing2', 'image1', 0, 100, onMouse)
mix2 = cv2.getTrackbarPos('Mixing2', 'image2')



cv2.createTrackbar('Mixing3', 'image1', 0, 100, onMouse)
mix3 = cv2.getTrackbarPos('Mixing3', 'image3')

while True:
    over_image = cv2.addWeighted(image1, float(mix1) / 100, image2, float(mix2) / 100, 0)

    image = cv2.addWeighted(over_image, 1, image3, float(mix3) / 100, 0)


    cv2.imshow("image1", image)


    if cv2.waitKey(30) >= 0: break  # 종료 조건 : 스페이스 바 입력

    mix1 = cv2.getTrackbarPos('Mixing1', 'image1')
    mix2 = cv2.getTrackbarPos('Mixing2', 'image1')
    mix3 = cv2.getTrackbarPos('Mixing3', 'image1')
