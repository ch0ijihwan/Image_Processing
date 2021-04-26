import cv2

image = cv2.imread("read_color.jpg", cv2.IMREAD_COLOR) #명암도
if image is None: raise Exception("영상 파일 읽기 에러")

title = "images"
cv2.imshow(title,image)
cv2.waitKey(0)

params_jpg = (cv2.IMWRITE_JPEG_QUALITY, 100)  # JPEG 화질 설정, 최대값인 100으로 설정
params_png = [cv2.IMWRITE_PNG_COMPRESSION, 0]  # PNG 압축 레벨 설정. 최솟값인 9로 설정. 압축률이 낮을 수록 원본과 가깝기 떄문에.

## 행렬을 영상 파일로 저장
cv2.imwrite("test.jpg", image,params_jpg)#최대값인 100으로 설정
cv2.imwrite("test.png", image, params_png)

print("저장 완료")