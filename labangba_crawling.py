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

import pymysql

#
#   디비 연동
#
conn = pymysql.connect(host='127.0.0.1', user='root',
                       password='kingark1593', db='labangba', charset='utf8')
cur = conn.cursor()

#
#   크롬 브라우져 띄우기
#

driver = webdriver.Chrome()
time.sleep(5)

#
#   라방바 로그인 접속
#
URL = f"https://datalab.labangba.com/user/sign_in?redirect=%2Fschedule"
driver.get(url=URL)
time.sleep(3)

#
# 로그인 - 아이디 패스워드 입력 후 클릭
#
driver.find_element(
    By.CSS_SELECTOR, '#__next > div > div > div > main > form > div:nth-child(1) > div > input').send_keys('jjsk109@gmail.com')
time.sleep(1)
driver.find_element(
    By.CSS_SELECTOR, '#__next > div > div > div > main > form > div:nth-child(2) > div > input').send_keys('kingark1593!@')
time.sleep(1)
driver.find_element(
    By.CSS_SELECTOR, '#__next > div > div > div > main > form > button').click()
time.sleep(10)


#
# 일정 클릭하기
#
variable = driver.current_url
#
# 일정의 과저 클릭하기
#
driver.find_element(By.CSS_SELECTOR, '#__next > div > div > div > div > div.schedule_setterContainer___6eGu > div.schedule_calendarContainer__fvarT > div.schedule_calendarLeft__YG6Xy > div.schedule_pc__bHcni > div > div.jsx-1374961830.SelectSmall_selectBox__bSJTd.SelectSmall_noselect__zrIky').click()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, '#__next > div > div > div > div > div.schedule_setterContainer___6eGu > div.schedule_calendarContainer__fvarT > div.schedule_calendarLeft__YG6Xy > div.schedule_pc__bHcni > div > div.jsx-1374961830.SelectSmall_optionsContainer__DpSZy.SelectSmall_active__i4n3m > div > div.jsx-2891349745.realarea > ul > li:nth-child(2)').click()
time.sleep(5)

#
# 일정의 달력 클릭하기
#
driver.find_element(By.CSS_SELECTOR, '#__next > div > div > div > div > div.schedule_setterContainer___6eGu > div.schedule_calendarContainer__fvarT > div.schedule_calendarLeft__YG6Xy > div.schedule_selectorContainer__zG3Kz > div.schedule_pc__bHcni > div > div').click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, '#__next > div > div > div > div > div.schedule_setterContainer___6eGu > div.schedule_calendarContainer__fvarT > div.schedule_calendarLeft__YG6Xy > div.schedule_selectorContainer__zG3Kz > div.schedule_pc__bHcni > div > div.Calendar_frame__RoLvH > div.Calendar_board__gz_8_ > div.Calendar_head__naWOV > figure:nth-child(1)').click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, '#__next > div > div > div > div > div.schedule_setterContainer___6eGu > div.schedule_calendarContainer__fvarT > div.schedule_calendarLeft__YG6Xy > div.schedule_selectorContainer__zG3Kz > div.schedule_pc__bHcni > div > div.Calendar_frame__RoLvH > div.Calendar_board__gz_8_ > div.Calendar_date__Kddkw > div:nth-child(1) > div:nth-child(1)').click()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, '#__next > div > div > div > div > div.schedule_setterContainer___6eGu > div.schedule_calendarContainer__fvarT > div.schedule_calendarLeft__YG6Xy > div.schedule_selectorContainer__zG3Kz > button').click()
time.sleep(3)

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")
lis = soup.select(".schedule_container__Bp3qt")

for li in lis:
    trs = li.select('tr')
    for tr in trs:
        tds = tr.select('td')

        if (len(tds)):
            data_string = "('2022-12-01',"

            # 시간 live_time
            data_string += f"'{tds[1].select('span')[1].text}',"
            title = tds[2].select('span')[0].text
            title = title.encode('utf-8', 'ignore').decode('utf-8')

            data_string += f"'🍊불로초감귤 / 오색 방울토마토 1분 광고방송!🍅',"  # 방송 제목 title
            data_string += f"'{tds[2].select('span')[1].text}',"  # 미디어 media
            if (len(tds[3].select('span'))):
                # 분류 division
                data_string += f"'{tds[3].select('span')[0].text}',"

            # 시청자 수 live_view
            data_string += f"{tds[4].select('span')[0].text},"
            # 판매수량 sale_count
            data_string += f"{tds[5].select('span')[0].text},"
            data_string += f"'{tds[6].select('span')[0].text}',"  # 판매금액 sale
            # 판매 갯수 product_count
            data_string += f"{tds[7].select('span')[0].text})"
            sql = f"INSERT INTO live_information(live_date, live_time, title, media, division, live_view, sale_count, sale, product_count)VALUES{data_string}"
            print(sql)
            cur.execute(sql)
            conn.commit()

        print()
# time.sleep(10)


#
# DB 연동
#


conn.close()
