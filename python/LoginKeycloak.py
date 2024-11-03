from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('http://localhost:8080/realms/test/account/')

time.sleep(1)
username = driver.find_element(By.ID, 'username')     
password = driver.find_element(By.ID, 'password')
signInButton = driver.find_element(By.ID, 'kc-login')

time.sleep(1)
username.send_keys('test')
password.send_keys('test')
signInButton.click()

time.sleep(1)
cookies_list = driver.get_cookies()
for cookie in cookies_list:
    print(cookie)

driver.close()
driver.quit()