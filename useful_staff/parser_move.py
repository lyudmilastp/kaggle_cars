import requests
from bs4 import BeautifulSoup
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import urllib
from bs4 import BeautifulSoup
import io

linkone = 'https://www.cian.ru/kupit-kvartiru-1-komn-ili-2-komn/'
# html_doc = urllib.request.urlopen(linkone).read()
# soup = BeautifulSoup(html_doc, 'lxml')

# get all flat links from the page
html_doc = requests.get(linkone)
html_doc = html_doc.content
soup = BeautifulSoup(html_doc, 'lxml')
links = soup.find_all('a', {'class' : '_93444fe79c--link--39cNw'})
links = [i['href'] for i in links]

# get pages links
pages = soup.find_all('a', {'class' :"_93444fe79c--list-itemLink--3o7_6"})
pages = [i['href'] for i in pages]

# Parse data from the specific flat advert



# example links
# <a href="https://www.cian.ru/sale/flat/247916416/" class="_93444fe79c--link--39cNw"><span class="_93444fe79c--link-area--3CWic"></span></a>
# <a href = "https://www.cian.ru/cat.php?deal_type=sale&amp;engine_version=2&amp;offer_type=flat&amp;p=2&amp;region=1&amp;room1=1&amp;room2=1" class ="_93444fe79c--list-itemLink--3o7_6" > 2 < / a >