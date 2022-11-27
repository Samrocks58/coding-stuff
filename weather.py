import requests
from bs4 import BeautifulSoup

html = requests.get(r"https://owc.enterprise.earthnetworks.com/OnlineWeatherCenter.aspx?aid=5744").content
soup = BeautifulSoup(html, 'html.parser')

# print(len(soup.get("a")))
# for div in soup.find_all(id="camImgTD"):
#     print(div)
    # print(type(div.get_all("div")))
    # try:
    #     print(div.get_all("div"))
    # except Exception:
    #     pass
    # id="cameraCont"

    # https://direct.earthnetworks.com/DataSevice/GetData.ashx?dt=cl&la=41.8233&lo=-71.4208&f=loadClosestCam

for div in soup.find_all('div'):
    if div.get('id') == "tabs-camera":
        for div2 in div.find_all('div'):
            if div2.get('id') == "camImgTD":
                # print(div)
                for div3 in div2.find_all(id="cameraCont"):
                    try: 
                        uls = div3.find_all("ul")
                        print(len(uls))
                        lis = div3.find_all("li")
                        print(len(lis))
                    except Exception: pass
                    print(uls)
                    for ul in uls:
                        if ul.get('class') == "timeLapseCamera":
                            for li in ul.get_all("li"):
                                print(li.find("img").get("data-src"))