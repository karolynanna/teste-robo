from selenium import webdriver
from selenium.webdriver.common.by import By

navegador = webdriver.Chrome(executable_path=r'C:/Users/annak/Desktop/webdriver./chromedriver.exe')
navegador.get('https://pt.aliexpress.com/')
navegador.find_element(By.ID, 'search-key').send_keys('Redmi')
navegador.find_element(By.CLASS_NAME,'search-button').submit()
navegador.find_element(By.TAG_NAME,'a')
