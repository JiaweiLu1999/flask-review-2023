import requests
from bs4 import BeautifulSoup

URL = "https://www.amazon.com/dp/B07WVNBY1G"
headers = {
    "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
    "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                   "Chrome/115.0.0.0 Safari/537.36"
}
response_text = requests.get(URL, headers=headers).text
print(response_text)
