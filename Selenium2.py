from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome()
url="https://github.com"
driver.get(url)

searchInput=driver.find_element_by_name("q")
time.sleep(1)
searchInput.send_keys("python")
time.sleep(1)
searchInput.send_keys(Keys.ENTER)
time.sleep(1)
result=driver.find_elements_by_css_selector(".repo-list-item")
for element in result:
    print(element)
driver.close()




