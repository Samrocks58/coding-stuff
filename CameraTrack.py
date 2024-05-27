from traceback import print_stack
import cv2, numpy, sys

video_capture = cv2.VideoCapture(0)

hue_change=10
sat_change=30
value_change=50
starting_color = [0, 0, 0]
white = [255, 255, 255]

def click(event,x,y,flags,param):  
    global hsv, lower_color, upper_color, hue_change, value_change, sat_change, starting_color
    if(event == cv2.EVENT_LBUTTONDOWN):
        starting_color = hsv[y, x]
        upper_color = numpy.array([starting_color[0]+hue_change, starting_color[1]+sat_change, starting_color[2]+value_change])
        lower_color = numpy.array([starting_color[0]-hue_change, starting_color[1]-sat_change, starting_color[2]-value_change])

def update():
    global upper_color, lower_color, starting_color
    upper_color = numpy.array([starting_color[0]+hue_change, starting_color[1]+sat_change, starting_color[2]+value_change])
    lower_color = numpy.array([starting_color[0]-hue_change, starting_color[1]-sat_change, starting_color[2]-value_change])      

cv2.namedWindow('frame')  
cv2.setMouseCallback('frame',click)  

lower_color = numpy.array([0, 0, 0])#v=50
upper_color = numpy.array([0, 0, 0])
prev_char=''
cur_char=''

while True:
    ret, frame = video_capture.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # lower_color = numpy.array([80, 100, 25])#v=50
    # upper_color = numpy.array([100, 255, 255])

    mask = cv2.inRange(hsv, lower_color, upper_color)
    small_mask=cv2.resize(mask, (0, 0), fx=0.25, fy=0.25)

    NumXY = 0
    TotalX = 0
    TotalY = 0
    res = cv2.bitwise_and(frame, frame, mask=mask)
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

    # res = cv2.Canny(frame,100,70)
    # small_res=cv2.resize(res, (0, 0), fx=0.50, fy=0.50)
    # for y in range(len(small_res)):
    #     for x in range(len(small_res[y])):
    #         if res[y*2, x*2] == 255:
    #             frame[y*2, x*2] = [255, 255, 255]

    # frame2 = [numpy.uint8(numpy.clip(i,0,255)) for i in frame]
    # frame = cv2.GaussianBlur(frame, 5, 5)
    # cv2.fastNlMeansDenoisingColoredMulti(res, 2, 5, None, 4, 7, 35)
    
    cv2.imshow("frame", frame)
    cv2.imshow("res", res)
    
    c = cv2.waitKey(1)

    if c == 27:
        break
    if c > -1 and c != prev_char:
        cur_char = c
    prev_char = c
    if cur_char == ord('q'):
        break
    if cur_char == ord('h'):
        hue_change += 1
        update()
    if cur_char == ord('n'):
        hue_change -= 1
        update()
    if cur_char == ord('s'):
        sat_change += 1
        update()
    if cur_char == ord('x'):
        sat_change -= 1
        update()
    if cur_char == ord('v'):
        value_change += 1
        update()
    if cur_char == ord('f'):
        value_change -= 1
        update()
    if cur_char == ord('c'):
        lower_color = numpy.array([0, 0, 0])
        upper_color = numpy.array([0, 0, 0])
    if cur_char == ord('r'):
        # print(res[0])
        for y in range(len(res)):
            for x in range(len(res[0])):
                if res[y, x] == 255:
                    print(res[y].index(255))
                    frame[x, y] = [255, 255, 255]
    cur_char=''

video_capture.release()
cv2.destroyAllWindows()
print(f"hue change: {hue_change}")
print(f"saturation change: {sat_change}")
print(f"value change: {value_change}")
# Useful Functions in cv2:
#   
# small_frame=cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
# rgb_small_frame = small_frame[:, :, ::-1]
# cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
# font = cv2.FONT_HERSHEY_DUPLEX
# cv2.putText(frame, face_name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)