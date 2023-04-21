import cv2

# 이미지 파일을 읽어옵니다.
img = cv2.imread("D:\chosuhyeon\school_class\python\py0421\Colorchange\img_chun.webp")

# 이미지를 좌우 반전시킵니다.
flipped_img = cv2.flip(img, 1)

# 결과 이미지를 출력합니다.
cv2.imshow("Flipped Image", flipped_img)
cv2.waitKey(0)
