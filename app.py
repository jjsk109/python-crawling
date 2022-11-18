from bs4 import BeautifulSoup
import requests

# headers = {
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
# }

# url = "https://npay.tistory.com/636"
# r = requests.get(url,headers=headers)

# print(r.raise_for_status)

# html = r.text

# soup = BeautifulSoup(html , "html.parser")

# title = soup.select("tr")
# for item in title:    
#     td = item.select("td")
#     for item2 in td:
#        print()
# ---------------------------------------------------------------------------------
    
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

import time
driver = webdriver.Chrome()
time.sleep(5)
URL = "https://shoppinglive.naver.com/calendar?d=20221115"
driver.get(url=URL)
time.sleep(3)
page_hight = 3000
for index in range(1,15):
    time.sleep(1)
    page_hight = page_hight * index
    page_string = f"window.scrollTo(0, {page_hight})"
    driver.execute_script(page_string)

html = driver.page_source
soup = BeautifulSoup(html , "html.parser")
lis = soup.select(".LiveList_item_3s2bf")
for li in lis:
    # 시간
    live_time = li.select_one(".LiveItem_time_2l54m")
    print()

    # 시청자 수

    on_Air_badge_count = li.select_one(".LiveItem_viewer_n7Q3p")
    LiveItem_viewer_n7Q3p = ""
    if on_Air_badge_count == None :
        print('방송대기')
        LiveItem_viewer_n7Q3p = ""
    else :
        print(on_Air_badge_count.text)
        LiveItem_viewer_n7Q3p = on_Air_badge_count.text

    # 방송이름
    LiveContent_title = li.select_one(".LiveContent_title_25rkS")
    print(LiveContent_title.text)
    # 상품이름
    LiveContent_product_name_1EjEV = li.select_one(".LiveContent_product_name_1EjEV ")
    print(LiveContent_product_name_1EjEV.text)
    # 가격
    LiveContent_price_2YTb7 = li.select_one(".LiveContent_price_2YTb7 > strong")
    print(LiveContent_price_2YTb7.text)
    # 판매자 이름
    LiveContent_seller_X20Vo = li.select_one(".LiveContent_seller_X20Vo") 
    print(LiveContent_seller_X20Vo.text)

    print()

