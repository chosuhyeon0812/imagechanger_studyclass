import cv2
import tkinter as tk
from tkinter import filedialog

# Tkinter를 사용하여 파일 선택 창을 띄웁니다.
root = tk.Tk()
root.withdraw()

# 파일 선택 창을 띄워 이미지 파일을 선택합니다.
file_path = filedialog.askopenfilename()

# 이미지 파일을 읽어옵니다.
img = cv2.imread(file_path)

# 이미지를 카키색으로 변환합니다.
kaki_img = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
kaki_img[:, :, 0] = 135
kaki_img = cv2.cvtColor(kaki_img, cv2.COLOR_YCrCb2BGR)

# 결과 이미지를 출력합니다.
cv2.imshow("Kaki Image", kaki_img)
cv2.waitKey(0)
