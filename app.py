from bs4 import BeautifulSoup
import requests

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
}

url = "https://npay.tistory.com/636"
r = requests.get(url,headers=headers)

print(r.raise_for_status)

html = r.text

soup = BeautifulSoup(html , "html.parser")

title = soup.select("tr")
for item in title:    
    td = item.select("td")
    for item2 in td:
        print(item2)
        print()
    print()
        
    
