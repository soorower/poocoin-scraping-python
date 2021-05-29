from os import spawnl
from selenium import webdriver
import time
from time import sleep
from bs4 import BeautifulSoup as bs
import pandas as pd
from selenium.webdriver.chrome.options import Options
import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
coin = input('provide coin address,like(0xb74ed4112c23b7c8ef1439fa55d304d537c5599b): ')
update = int(input('How many updates you want, like(30), it will show 30 updates: '))
delay = int(input('Delay bettween each update: '))
print('Wait for some time to load the page...Its running..')
x = datetime.datetime.now()
hour = x.hour
minute = x.minute
date_1 = x.day
month = x.month
year = x.year
date_time1 = f'{date_1}-{month}-{year}_{hour}-{minute}'
mobile_emulation = {

    "deviceMetrics": {"width": 360, "height": 640, "pixelRatio": 3.0},

    "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19"}

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

driver = webdriver.Chrome(chrome_options=chrome_options)

# coin = '0xb74ed4112c23b7c8ef1439fa55d304d537c5599b'
for i in range(update):
    driver.get(f'https://poocoin.app/tokens/{coin}')
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='mb-1 d-flex flex-column lh-1']/span"))
        )
        soup = bs(driver.page_source, 'html.parser')
        market_cap = soup.find('div',attrs={'class':'px-3'}).find('span',attrs= {'class': 'text-success'}).text
        bnb_lp_bnb_holdings = soup.find('div',attrs={'class':'px-3'}).get_text()
        index1 = bnb_lp_bnb_holdings.find('Holdings:') + 8
        
        sleep(delay)
        price2 = soup.find('div',attrs={'class':'px-3'}).findAll('span',attrs= {'class': 'text-success'})[1].text
        index2 = bnb_lp_bnb_holdings.find(f'{price2}')


        price1 = bnb_lp_bnb_holdings[index1:index2]
        bnb_holdings = price1 + ' ' + price2

        print(f'Price: {element.text}')
        print(f'Market Cap: {market_cap}')
        print(f'BNB Holdings: {bnb_holdings}')
        print('\n')
    except:
        pass