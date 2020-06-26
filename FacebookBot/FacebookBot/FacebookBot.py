from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import sys
import os
import time
#Takes username and password from the console to prevent hard coding the credentials
username = sys.argv[1]
password = sys.argv[2]


class TwitterBot():
    def __init__(self):
        self.username = username
        self.password  = password
        self.driver = webdriver.Chrome(r'C:\Aryamann\chromedriver.exe')
        self.baseurl = 'https://www.twitter.com/login'
        

    def login(self):
        #Getting the Twitter Url
        self.driver.get(self.baseurl)
        WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located((By.NAME, 'session[username_or_email]'))).send_keys(self.username)
        WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located((By.NAME, 'session[password]'))).send_keys(self.password)
        WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/form/div/div[3]/div/div'))).click()
    #TWEETING SOMETHING ,TAKES THE MESSAGE AS INPUT
    def tweet(self,message):
        self.login()
        time.sleep(5)
        WebDriverWait(self.driver,20).until(expected_conditions.presence_of_element_located((By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div'))).send_keys(message)
        time.sleep(2)
        WebDriverWait(self.driver,20).until(expected_conditions.presence_of_element_located((By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div'))).click()

if __name__ == '__main__':

    Aryamann = TwitterBot()

    Aryamann.tweet('Testing')
