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

for div in soup.find_all('div'):
    if div.get('id') == "camImgTD":
        # print(div)
        for div2 in div.find_all(id="cameraCont"):
            try: 
                uls = div2.find_all("ul")
                print(len(uls))
                lis = div2.find_all("li")
                print(len(lis))
            except Exception: pass
            print(uls)
            for ul in uls:
                if ul.get('class') == "timeLapseCamera":
                    for li in ul.get_all("li"):
                        print(li.find("img").get("data-src"))