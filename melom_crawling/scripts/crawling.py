from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random

user = "Mozilla/5.0 (IPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15(KHTML, like Gecko) CriOS/80.0.3987.95 Mobile/15E148 Safari/604.1"

options_ = Options()
options_.add_argument(f"user-agent={user}")
options_.add_experimental_option("detach", True)
options_.add_experimental_option("excludeSwitches", ["enable-logging"])


#크롬 드라이버 매니저를 자동으로 설치되도록 실행시키는 코드
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options_)

url = "https://m2.melon.com/index.htm"
driver.get(url)
time.sleep(0.5)

Random = random.randint(1,2)

#아래 순서대로 스크래핑한 자료를 출력해주세요
#순위 :
#노래 제목 :
#가수 이름 :
driver.find_element(By.CSS_SELECTOR, ".link-logo").click()
time.sleep(Random)

driver.find_elements(By.CSS_SELECTOR, ".nav_item")[2].click()
time.sleep(Random)

driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
time.sleep(Random)

time.sleep(Random)

driver.find_element(By.XPATH, '//button[@onclick="hasMore2();"]').click()
time.sleep(Random)

driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
time.sleep(Random)

html = driver.page_source
soup = BeautifulSoup(driver.page_source, "html.parser")
items = soup.select(".list_item")


for i in items:
    rank_element = i.select_one(".ranking_num")
    if rank_element:
        rank_text = rank_element.text.rstrip("위").split("\n")
        rank = int(*rank_text)
        if rank >= 50:
            title = i.select_one(".title.ellipsis").text.strip()
            name = i.select_one(".name.ellipsis").text

            print(f"{rank}위 \n 제목 : {title} \n 이름 : {name}")

driver.quit()