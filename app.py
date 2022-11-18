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
from datetime import datetime

today = datetime.today().strftime("%Y%m%d")

#
#   네이버 라이브 쇼핑
#
driver = webdriver.Chrome()
time.sleep(5)
URL = f"https://shoppinglive.naver.com/calendar?d={today}"
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
num = 0
for li in lis:
    # 시간
    live_time = li.select_one(".LiveItem_time_2l54m")
    
    # 시청자 수
    on_Air_badge_count = li.select_one(".LiveItem_viewer_n7Q3p")
    LiveItem_viewer_n7Q3p = ""
    if on_Air_badge_count == None :
        LiveItem_viewer_n7Q3p = "방송대기"
    else :
        LiveItem_viewer_n7Q3p = on_Air_badge_count.text

    # 방송이름
    LiveContent_title = li.select_one(".LiveContent_title_25rkS")

    # 상품이름
    LiveContent_product_name_1EjEV = li.select_one(".LiveContent_product_name_1EjEV ")

    # 가격
    LiveContent_price_2YTb7 = li.select_one(".LiveContent_price_2YTb7 > strong")

    # 판매자 이름
    LiveContent_seller_X20Vo = li.select_one(".LiveContent_seller_X20Vo") 
    print(f"시간 : {live_time.text} , 판매자 이름 : {LiveContent_seller_X20Vo.text} , 시청자 수 : {LiveItem_viewer_n7Q3p} , 방송이름 : {LiveContent_title.text} , 상품이름 : {LiveContent_product_name_1EjEV.text} , 가격 : {LiveContent_price_2YTb7.text}  ")


#
#   카카오 라이브 쇼핑
#

print()
time.sleep(1)
URL = f"https://store.kakao.com/home/live/calendar?date={today}"
driver.get(url=URL)
time.sleep(5)
kakao_html = driver.page_source
soup = BeautifulSoup(kakao_html , "html.parser")
kakao_lis = soup.select(".has_alarm")
num = 0

for li in kakao_lis:
    txt_time = li.select_one(".txt_time")
    tit_live = li.select_one(".tit_live")
    info_play_count = ""
    info_play = li.select_one(".info_play")
    if info_play == None:
        info_play_count = "방송대기"
    else :
        info_play_count = info_play.text
    print(f"시간 : {txt_time.text} , 시청자 수 : {tit_live.text} , 방송이름 : {info_play_count} ")
print()

#
#   티몬 라이브 쇼핑
#

time.sleep(1)
URL = "http://media.tmon.co.kr/schedule"
driver.get(url=URL)
time.sleep(10)
timon_html = driver.page_source
soup = BeautifulSoup(timon_html , "html.parser")
timon_lis = soup.select(".sc-jhAzac.fyAMLI.className")
for li in timon_lis:
     txt_time = li.select_one(".sc-brqgnP.ghrAtA")
     print(txt_time.text)


#
#   그립 라이브 쇼핑
#

print()
time.sleep(1)
URL = f"https://www.grip.show/lives?tab=4"
driver.get(url=URL)
time.sleep(5)