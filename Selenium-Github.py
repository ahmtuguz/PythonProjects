from a import kullanıcı_adı,şifre
import time
from selenium import webdriver

class Github:
    def __init__(self, kullanıcı_adı,şifre):
        self.browser=webdriver.Chrome()
        self.kullanıcı_adı=kullanıcı_adı
        self.şifre=şifre
        self.followers=[]
    
    def loadFollowers(self):
        items=self.browser.find_elements_by_css_selector(".d-table.table-fixed")
        for i in items:
            self.followers.append(i.find_element_by_css_selector(".link-gray").text)  

    def signIn(self):
        self.browser.get("https://github.com/login")
        time.sleep(2)

        self.browser.find_element_by_xpath("//*[@id='login_field']").send_keys(self.kullanıcı_adı)
        self.browser.find_element_by_xpath("//*[@id='password']").send_keys(self.şifre)

        time.sleep(1)

        self.browser.find_element_by_xpath("//*[@id='login']/form/div[4]/input[9]").click()
    def getFollowers(self):
        self.browser.get("https://github.com/ahmtuguz?tab=followers")  
        time.sleep(1)

        self.loadFollowers()
  
        while True:
            links=self.browser.find_element_by_class_name("pagination").find_elements_by_tag_name("a")
            if len(links)==1:
                if links[0].text=="Next":
                    links[0].click()
                    time.sleep(1)
                    self.loadFollowers()
                else:
                    break
            else:
                for link in links:
                    if link.text=="Next":
                        link.click()
                        time.sleep(1)
                        self.loadFollowers()
                    else:
                        continue            


github=Github(kullanıcı_adı,şifre)
github.signIn()
github.getFollowers()
print(len(github.followers))
print(github.followers)    

    