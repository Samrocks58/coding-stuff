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
while True:
    cv2.imshow("doggo", image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
os.remove(filename)
quit()