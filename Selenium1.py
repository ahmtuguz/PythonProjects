from selenium import webdriver
import time
driver=webdriver.Chrome()

url="https://github.com"

driver.get(url)

driver.maximize_window()
time.sleep(1)

url="https://github.com/ahmtuguz"
driver.get(url)
#if "ahmtuguz" in driver.title:
#    driver.save_screenshot("png")

time.sleep(1)

driver.back()
time.sleep(1)

print(driver.title)
time.sleep(1)
driver.close()

