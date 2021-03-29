import requests
import pandas as pd
from selenium import webdriver
path_geck = 'C:/Users/cth/AppData/Local/Programs/Python/Python39/geckodriver.exe'
path_ff = 'C:/Program Files/Mozilla Firefox/firefox.exe'
from bs4 import BeautifulSoup
from cian import CianClient
import cian as cian


pd.set_option('display.max_rows', 50)
pd.set_option('display.min_rows', 20)
pd.set_option('display.max_columns', 20)
pd.set_option('display.width', 150)
pd.set_option('display.precision', 4)
pd.set_option('expand_frame_repr', True)


url = 'https://www.cian.ru/cat.php?deal_type=sale&engine_version=2&offer_type=offices&office_type%5B0%5D=3&office_type%5B1%5D=7&p=2&region=4593&sort=price_square_order'

content = requests.get(url)
soup = BeautifulSoup(content.content)
all_links = soup.find_all('button', {'class' : '_93444fe79c--main--1-d6V _93444fe79c--light--366j7'})

driver = webdriver.Firefox(executable_path= path_geck)
driver.get(url)
driver.find_element_by_xpath('/html/body/div[6]/div/div[6]/div/div/div/button[1]').click()