import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv
import re
import sys

url = "https://summerofcode.withgoogle.com/projects/"
driver = webdriver.Chrome('./chromedriver') 
driver.get(url)
SCROLL_PAUSE_TIME = 5

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height
    html = driver.page_source

    soup = BeautifulSoup(html,'html.parser')
    script = soup.find_all('div' , class_="project-card__right-header-content" )

    def function(result, file):
        name= result.find('h2')
        divs = result.find_all('div')
        proj = divs[1]
        rows = [name.text, divs[3].text, proj.text]
        csv_line = name.text.strip() + ',' + divs[3].text + ',' + proj.text + '\n'
        file.write(csv_line)

    with open('GSoc.csv','w',newline='',encoding='utf-8') as file:
        for result in script:
                function(result, file)
driver.close()
    