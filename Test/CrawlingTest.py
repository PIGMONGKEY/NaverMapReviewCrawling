import requests
from bs4 import BeautifulSoup

url = "https://pcmap.place.naver.com/restaurant/1231684190/review/visitor?entry=bmp&from=map&fromPanelNum=" \
      "1&ts=1691500494146"
# headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome"
#                          "/115.0.0.0 Safari/537.36"}

response = requests.get(url)
print(response.status_code)
soup = BeautifulSoup(response.content.decode('utf-8', 'ignore'), features="html.parser")

value = soup.find("span", {"class": "zPfVt"})
print(value)

value = soup.find_all("span", {"class": "zPfVt"})
print(value)
