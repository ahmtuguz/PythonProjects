from tw import username,password
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

class Twitter:
    def __init__(self,username,password):
        self.browserProfile=webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option("prefs",{"intl.accept_languages":"en,en_US"})
        self.driver=webdriver.Chrome("chromedriver.exe",chrome_options=self.browserProfile)
        self.username=username
        self.password=password
    def Login(self):
        self.driver.get("https://twitter.com/login")
        time.sleep(1)
        username=self.driver.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/form/div/div[1]/label/div/div[2]/div/input")
        password=self.driver.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/form/div/div[2]/label/div/div[2]/div/input")
        
        username.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.ENTER)
        time.sleep(2)

    def search(self,hashtag):
        searchInput=self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[1]/div[1]/div/div/div/div/div[1]/div[2]/div/div/div/form/div[1]/div/div/div[2]/input')
        time.sleep(1)
        searchInput.send_keys(hashtag)
        time.sleep(2)
        searchInput.send_keys(Keys.ENTER)
        time.sleep(2)
        list=self.driver.find_elements_by_xpath("//div[@data-testid='tweet']/div[2]/div[2]/div[2]")
        for i in list:
            print("**************")
            print(i.text)           


twitter=Twitter(username,password)
twitter.Login()
twitter.search("python")

