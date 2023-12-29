import mysql.connector
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# 데이터베이스 설정 _S @@@@@@@@@@@@@@@@@@@@@@
conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="3145664",
        database="crow"
    )

# 데이터베이스 커서 생성
cursor = conn.cursor()
# 데이터베이스 설정 _E @@@@@@@@@@@@@@@@@@@@@@

# 웹 드라이버 설정 _S @@@@@@@@@@@@@@@@@@@@@@
# 웹 드라이버 초기화 (ChromDriver 사용)
service = Service('C:\chromedriver.exe')
# 웹 드라이버 설정 _E @@@@@@@@@@@@@@@@@@@@@@


query = "INSERT INTO top10_up (n_date, company, price, `change`, change_price, percent) VALUES (NOW(),%s,%s,%s,%s,%s)"

top10_up = []

try:
    # 웹 드라이버 가져옴
    driver = webdriver.Chrome(service=service)
    # 네이버 금융 페이지
    driver.get('https://finance.naver.com/')
    time.sleep(2)
    # a_tag = TOP종목 내에 있는 상승 버튼
    a_tag = driver.find_element(By.CSS_SELECTOR, "ul.tab_area.sise_top1 li.tab2 a")
    a_tag.click()
    time.sleep(1)

    # up_rows는 상승된 종목들을 가져옴
    up_rows = driver.find_elements(By.CSS_SELECTOR, 'tbody#_topItems2 tr.up')
    # 하위에 있는 th, td 태그를 가져옴
    for row in up_rows:
        header = row.find_element(By.TAG_NAME, 'th').text
        datas = row.find_elements(By.TAG_NAME, 'td')
        data_cell = datas[1].text.split("\n")
        # 전달할 데이터
        data = (header, datas[0].text, data_cell[0], data_cell[1], datas[2].text)
        print(data)
        # 데이터베이스에 전달
        cursor.execute(query, data)
    conn.commit()

finally:
    # 드라이버 종료
    driver.quit()
    cursor.close()
    conn.close()