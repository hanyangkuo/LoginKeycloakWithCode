require 'selenium-webdriver'

driver = Selenium::WebDriver.for :chrome
driver.navigate.to "http://localhost:8080/realms/test/account/"

sleep(1)
username = driver.find_element(id: 'username')     
password = driver.find_element(id:  'password')
signInButton = driver.find_element(id: 'kc-login')

sleep(1)
username.send_keys "test"
password.send_keys "test"
signInButton.click

sleep(1000)
driver.manage.all_cookies.each do |cookie|
  puts cookie
end

driver.close
driver.quit