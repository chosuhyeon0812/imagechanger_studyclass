import cv2
import datetime

# 웹캠으로부터 영상 캡처
cap = cv2.VideoCapture(0)

# 캡처할 동영상의 확장자, 코덱, 프레임레이트, 해상도 등 설정
fourcc = cv2.VideoWriter_fourcc(*'XVID')
fps = 30
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# VideoWriter 객체 생성
out = cv2.VideoWriter('output.avi', fourcc, fps, (width, height), isColor=False)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
        
    # 오늘 날짜 출력
    now = datetime.datetime.now()
    today = now.strftime("%Y-%m-%d")
    font = cv2.FONT_HERSHEY_SIMPLEX
    bottomLeftCornerOfText = (10,30)
    fontScale = 1
    fontColor = (255,255,255)
    lineType = 2
    cv2.putText(frame,today, bottomLeftCornerOfText, font, fontScale, fontColor, lineType)
    
    # 흑백 이미지로 변환
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # 화면에 출력
    cv2.imshow('frame', gray)
    
    # 저장
    out.write(gray)
    
    # 'q' 키를 누르면 종료
    if cv2.waitKey(1) == ord('q'):
        break
        
# 리소스 해제
cap.release()
out.release()
cv2.destroyAllWindows()
