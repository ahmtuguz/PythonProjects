from instagram import username,password
from selenium import webdriver
import time

class Instagram:
    def __init__(self,username,password):
        self.driver=webdriver.Chrome()
        self.username=username
        self.password=password
        self.followers=[]
    def getUser(self):
        self.driver.get("https://www.instagram.com")
        time.sleep(2)

        self.driver.find_element_by_xpath("//*[@id='react-root']/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input").send_keys(self.username)
        self.driver.find_element_by_xpath("//*[@id='react-root']/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input").send_keys(self.password)
        
        time.sleep(1)

        self.driver.find_element_by_xpath("//*[@id='react-root']/section/main/article/div[2]/div[1]/div/form/div[4]").click()

        time.sleep(2)

    def getFollowers(self):
        self.driver.get(f"https://www.instagram.com/{self.username}")
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[3]/a")
        time.sleep(1)

        liste=self.driver.find_elements_by_css_selector(".wo9IH")
        for i in liste:
            link=i.find_element_by_css_selector().find_element_by_css_selector("href")
            print(link)

        
        
        
          
instagram=Instagram(username,password)
instagram.getUser()
instagram.getFollowers()

            
