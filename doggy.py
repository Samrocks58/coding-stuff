import requests, cv2, shutil, os
response=requests.get("https://dog.ceo/api/breeds/image/random")
response=response.json()
if response["status"] == "success":
    link=response["message"]
    filename=link.split("/")[-1]
    picture=requests.get(link, stream=True)
else:
    quit()  
with open(filename,'wb') as f:
    shutil.copyfileobj(picture.raw, f)
image=cv2.imread(filename)
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
    cur_char=''
cv2.destroyAllWindows()
os.remove(filename)
quit()