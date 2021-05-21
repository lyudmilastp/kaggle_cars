import os
import zipfile
import webbrowser,time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

#заходим на Росреестр
#browser = webdriver.Firefox(firefox_profile=profile)
browser = webdriver.Chrome()
time.sleep (5)
browser.get ('https://rosreestr.ru/wps/portal/cc_vizualisation')        
time.sleep (5)
os.chdir('C:\\2\\')

#zip_ref = zipfile.ZipFile(path_to_zip_file, 'r')
#zip_ref.extractall(directory_to_extract_to)
#zip_ref.close()

zipFiles = []
sigFiles = []

for filename in os.listdir('.'):
    if filename.endswith('.zip'):        
        zipfile.ZipFile(filename, 'r').extractall()
        os.remove(filename)

#собираем файлы в список
for filename in os.listdir('.'):
    if filename.endswith('.zip'):
        zipFiles.append(filename)
#zipFiles.sort()
#print(zipFiles)


for filename in zipFiles:    
    act = browser.find_element_by_id('sig_file')
    act.send_keys('C:\\2\\'+str(filename)+'.sig')
    act = browser.find_element_by_id('xml_file')
    #распаковываем zip файл
    zip_ref = zipfile.ZipFile(filename, 'r').extractall()
    #берем xml из распакованного
    for f in os.listdir('.'):
        if f.endswith('.xml'):
            print(f)
    #вводим xml файл на сайте
            act.send_keys('C:\\2\\'+str(f))    
    act = browser.find_element_by_css_selector('input.brdg1111')
    act.click()
    i = tuple (str(input("Введите каптчу: ")))
    for b in i:
        act.send_keys(b)
        time.sleep (0.1)
    #act.submit()
    act = browser.find_element_by_css_selector('.terminal-button-bright')
    act.click()
    time.sleep (5)
    
    try:
        act = browser.find_element_by_link_text('Показать в человекочитаемом формате')
        act.click()
    #если ошибка с капчей        
    except NoSuchElementException:
        act = browser.find_element_by_id('sig_file')
        act.send_keys('C:\\2\\'+str(filename)+'.sig')
        act = browser.find_element_by_id('xml_file')
        for f in os.listdir('.'):
            if f.endswith('.xml'):
                print(f)    
                act.send_keys('C:\\2\\'+str(f))
        act = browser.find_element_by_css_selector('input.brdg1111')
        act.click()
        i = tuple (str(input("Введите каптчу: ")))
        for b in i:
            act.send_keys(b)
            time.sleep (0.1)        
        act = browser.find_element_by_css_selector('.terminal-button-bright')
        act.click()
        time.sleep (15)
        
    os.remove(filename)
    os.remove(filename+'.sig')
    for f in os.listdir('.'):
            if f.endswith('.xml'):                
                os.remove(f)

time.sleep(15)
browser.quit()

