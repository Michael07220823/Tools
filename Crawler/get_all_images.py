import re
import requests
from bs4 import BeautifulSoup as BS

# 自製標頭檔，以避開網站的封殺
my_headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}

html_content = requests.get("https://ohsoft.net", timeout=10, verify=True, headers=my_headers)

# 判斷當網站接成功時，是否回傳網頁狀態碼200
if html_content.status_code == 200:
    soup = BS(html_content.text, 'html.parser')
    # print(soup.prettify())

    img_list = soup.find_all(src=re.compile(".png$"))

    for link in img_list:
        print(link)