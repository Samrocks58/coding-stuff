import cv2, numpy, sys

video_capture = cv2.VideoCapture(0)

while True:
    ret, frame = video_capture.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_green = numpy.array([80, 100, 25])#v=50
    upper_green = numpy.array([100, 255, 255])

    mask = cv2.inRange(hsv, lower_green, upper_green)
    small_mask=cv2.resize(mask, (0, 0), fx=0.25, fy=0.25)

    NumXY = 0
    TotalX = 0
    TotalY = 0
    for i in range(0, small_mask.shape[0]):
        for j in range(0, small_mask.shape[1]):
            if small_mask[i, j] == 255:
                NumXY += 1
                TotalX += i
                TotalY += j
    if NumXY != 0:
        CordX = int(4*(TotalX/NumXY)) 
        CordY = int(4*(TotalY/NumXY)) 
        cv2.rectangle(frame, (0, CordX-10), (640, CordX+10), (0, 0, 255), cv2.FILLED)
        cv2.rectangle(frame, (CordY-10, 0), (CordY+10, 480), (0, 0, 255), cv2.FILLED)

    res = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow("frame", frame)
    cv2.imshow("res", res)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
# Useful Functions in cv2:
#   
# small_frame=cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
# rgb_small_frame = small_frame[:, :, ::-1]
# cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
# font = cv2.FONT_HERSHEY_DUPLEX
# cv2.putText(frame, face_name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)