import requests, cv2, os
import numpy as np

def Restart():
    global image
    response=requests.get("https://dog.ceo/api/breeds/image/random")
    response=response.json()
    if response["status"] == "success":
        link=response["message"]
        picture=requests.get(link, stream=True)
    else:
        quit()

    image = np.asarray(bytearray(picture.content), dtype="uint8") 
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)

    height = image.shape[0]
    width = image.shape[1]

    max_size = 600
    if height > max_size or width > max_size:
        bigNum = max(height, width)
        if bigNum == height:
            width = round(width * max_size/height)
            height = max_size
        else:
            height = round(height * max_size/width)
            width = max_size

    # print([height, width])
    # print(image.shape)

    image = cv2.resize(image, (width, height))

Restart()
prev_char=''
cur_char=''

while True:
    cv2.imshow("doggo", image)
    c = cv2.waitKey(1)

    if c == 27:
        break
    if c > -1 and c != prev_char:
        cur_char = c
    prev_char = c
    if cur_char == ord('q'):
        break
    elif cur_char == ord('r'):
        Restart()
    try:
        cv2.getWindowProperty('doggo', 0)
    except Exception:
        break
    cur_char=''
cv2.destroyAllWindows()
quit()