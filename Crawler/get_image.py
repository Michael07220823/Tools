import requests

# 自製標頭檔，以避開網站的封殺
my_headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}

html_content = requests.get("https://www.apple.com/ac/structured-data/images/open_graph_logo.png?201810272230", timeout=10, verify=True, headers=my_headers)

# 判斷當網站接成功時，是否回傳網頁狀態碼200
if html_content.status_code == 200:
    with open("apple.png", "wb") as img:
        img.write(html_content.content)
        print("[INFO] Get image successful!")