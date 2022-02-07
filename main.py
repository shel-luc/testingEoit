import time
import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as W
from selenium.webdriver.support import expected_conditions as E
from webdriver_manager.chrome import ChromeDriverManager

wait_time_out = 15
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.get("https://espol-lille.eu/en/")
wait_variable = W(driver, wait_time_out)
wait_variable.until(E.element_to_be_clickable((By.LINK_TEXT, "EDUCATION"))).click()

for test in driver.find_elements(By.XPATH, '//*[@id="content-section-1"]/div[1]/div/div[3]/div/div/h2/span/strong'):
    print(test.text)
use = test.text

links = driver.find_elements(By.XPATH, '//*[@id="content-section-1"]/div[1]/div/div[3]/div/div/p[2]/a')
for link in links:
    lnk = link.get_attribute("href")
    print(lnk)

links1 = driver.find_elements(By.XPATH, '//*[@id="content-section-1"]/div[1]/div/div[3]/div/div/p[2]/a')
for link in links1:
    lnk1 = link.get_attribute("href")
    print(lnk1)

links2 = driver.find_elements(By.XPATH, '//*[@id="content-section-1"]/div[1]/div/div[5]/div/div/p[2]/a')
for link in links2:
    lnk2 = link.get_attribute("href")
    print(lnk2)

links3 = driver.find_elements(By.XPATH, '//*[@id="content-section-1"]/div[1]/div/div[7]/div/div/p[2]/a')
for link in links3:
    lnk3 = link.get_attribute("href")
    print(lnk3)

links4 = driver.find_elements(By.XPATH, '//*[@id="content-section-1"]/div[1]/div/div[9]/div/div/p[2]/a')
for link in links4:
    lnk4 = link.get_attribute("href")
    print(lnk4)

links5 = driver.find_elements(By.XPATH, '//*[@id="content-section-1"]/div[1]/div/div[11]/div/div/p[2]/a')
for link in links5:
    lnk5 = link.get_attribute("href")
    print(lnk5)


for test1 in driver.find_elements(By.XPATH, '//*[@id="content-section-1"]/div[1]/div/div[5]/div/div/h2/span/strong'):
    print(test1.text)
use1 = test1.text
for test2 in driver.find_elements(By.XPATH, '//*[@id="content-section-1"]/div[1]/div/div[7]/div/div/h2/span/strong'):
    print(test2.text)
use2 = test2.text

for test3 in driver.find_elements(By.XPATH, '//*[@id="content-section-1"]/div[1]/div/div[9]/div/div/h2/span/strong'):
    print(test3.text)
use3 = test3.text

for test4 in driver.find_elements(By.XPATH, '//*[@id="content-section-1"]/div[1]/div/div[11]/div/div/h2/span/strong'):
    print(test4.text)
use4 = test4.text

for test5 in driver.find_elements(By.XPATH, '//*[@id="content-section-1"]/div[1]/div/div[13]/div/div/h2/span/strong'):
    print(test5.text)
use5 = test5.text

r = requests.get('https://espol-lille.eu/en/education/')
soup = BeautifulSoup(r.text, 'lxml')
with open('testy.csv', 'w', newline='') as csvfile:
    fieldnames = ['career', 'faculty', 'link_to_career']
    writer = csv.DictWriter(csvfile, delimiter=' ', fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'career': use ,'faculty':'ESPOL', 'link_to_career': lnk}),
    writer.writerow({'career': use1, 'faculty': 'ESPOL', 'link_to_career': lnk1}),
    writer.writerow({'career': use2, 'faculty': 'ESPOL', 'link_to_career': lnk2}),
    writer.writerow({'career': use3, 'faculty': 'ESPOL', 'link_to_career': lnk3}),
    writer.writerow({'career': use4, 'faculty': 'ESPOL', 'link_to_career': lnk4}),
    writer.writerow({'career': use5, 'faculty': 'ESPOL', 'link_to_career': lnk5})







time.sleep(70)





