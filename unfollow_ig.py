from selenium import webdriver
from time import sleep
import getpass

class InstaBot:
    def __init__(self,username,pw):
        self.driver = webdriver.Chrome()
        self.username = username
        
        #navigate to instagram
        self.driver.get("https://instagram.com")
        sleep(2)
        
        #click on log in
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[2]/p/a').click()
        sleep(2)

        #enter username in the correct input box
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input')\
            .send_keys(username)
        sleep(2)

        #enter password in the correct input box
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input')\
            .send_keys(pw)
        sleep(2)

        #press log in
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[4]').click()
        sleep(5)

        #You don't want notifications :)
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]').click()
        sleep(2)

    def get_unfollowers(self):
        #click on my profile
        self.driver.find_element_by_xpath("//a[contains(@href,'/{}')]".format(self.username))\
            .click()
        sleep(3)

        #click on following
        self.driver.find_element_by_xpath("//a[contains(@href,'/following')]").click()
        
        #put them in a list
        following = self._get_names()
       
        #click on followers
        self.driver.find_element_by_xpath("//a[contains(@href,'/followers')]").click()
        
        #put them in a list
        followers = self._get_names()
        
        #check and print which who doesn't follow you back
        not_following_back = [user for user in following if user not in followers]
        print(not_following_back)

    def _get_names(self):
        sleep(2)
        scroll_box = self.driver.find_element_by_xpath("/html/body/div[4]/div/div[2]")
        last_ht, ht = 0, 1
        
        #scrolling
        while last_ht != ht:
            last_ht = ht
            sleep(1)
            ht = self.driver.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight); 
                return arguments[0].scrollHeight;
                """, scroll_box)
        links = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text != '']
        
        # close button
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/div[2]/button")\
            .click()
        return names

#enter your details
user = input("Please enter your username:\n")
pw   = getpass.getpass('Please enter your password:\n')

#let it ruuuun 
my_Bot = InstaBot(user,pw)
my_Bot.get_unfollowers()
