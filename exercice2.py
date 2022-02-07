import html
import time

import bs4
import requests
from bs4 import BeautifulSoup
from pprint import pprint
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
wait_variable.until(E.element_to_be_clickable((By.LINK_TEXT, "INTERNATIONAL"))).click()
submit = driver.find_element(By.XPATH, '//*[@id="content-section-3"]/div[1]/div/div[5]/h4[2]/a')
driver.execute_script("arguments[0].click();",submit)


r = requests.get('https://espol-lille.eu/en/catalogue-de-cours-licence-relations-internationales/')
soup = BeautifulSoup(r.text, 'html.parser')
elems = soup.strong.text
print(elems)
elem = driver.find_element(By.XPATH, '//*[@id="b1"]/h3/span/strong')
print(elem.text)
elem1 = driver.find_element(By.XPATH, '//*[@id="e5"]/h3/span/strong')
print(elem1.text)

elem2 = driver.find_element(By.XPATH, '//*[@id="t1"]/h3/span/strong')
print(elem2.text)


with open('exo.csv', 'w', newline='') as csvfile:
    fieldnames = ['A', 'B', 'E', 'T']
    writer = csv.DictWriter(csvfile, delimiter=' ', fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'A': elems, 'B': elem.text, 'E': elem1.text, 'E': elem2.text}),



time.sleep(7)