import requests
import bs4 as bs
from time import sleep
base = 'http://www.ocenchik.ru'

link = 'http://www.ocenchik.ru/docsf/2229-ponyatiya-ocenki-podhody-ocenki-fso1.html'
fso_links = []

content = requests.get(link)
content = content.content

soup = bs.BeautifulSoup(content)
links = soup.find_all('a', href = True)
for i in links:
    if i.text.count('135') or i.text.count('ФСО'):
        fso_links.append(i)




for l in fso_links:
    if l.attrs['href'].startswith('/'):
        r = requests.get(base + l.attrs['href'])
        sleep(1)
        content = r.content
        soup = bs.BeautifulSoup(content, 'lxml')
        fsotext = soup.text
        with open('fso_{}.txt'.format(l.text.replace('"', '')), 'w') as f:
            f.write(fsotext)
    if l.attrs['href'].count('www.') == 1:
        r = requests.get(l.attrs['href'])
        sleep(1)
        content = r.content
        soup = bs.BeautifulSoup(content, 'lxml')
        fsotext = soup.text
        with open('fso_{}.txt'.format(l.text.replace('"', '')), 'w') as f:
            f.write(fsotext)







