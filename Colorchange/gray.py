import cv2
# 이미지 파일을 읽어옵니다.
img = cv2.imread("D:\chosuhyeon\school_class\python\py0421\Colorchange\img_chun.webp")

# 이미지를 회색으로 변환합니다.
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 결과 이미지를 출력합니다.
cv2.imshow("Gray Image", gray_img)
cv2.waitKey(0)