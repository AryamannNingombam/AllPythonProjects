from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
import sys
import os
import time
from pynput.keyboard import Key, Controller
#Takes username and password from the console to prevent hard coding the credentials
username = sys.argv[1]
password = sys.argv[2]

 #WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located((By.NAME, 'session[username_or_email]'))).send_keys(self.username)
class FacebookBot():
    def __init__(self):
         self.keyboard = Controller()
         self.email = username
         self.password  = password
         self.driver  = webdriver.Chrome("../../../../chromedriver.exe")
         self.baseurl = "https://www.facebook.com"
    def login(self):
         self.driver.get(self.baseurl)
         time.sleep(2)
         WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located((By.ID, 'email'))).send_keys(self.email)
         WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located((By.ID, 'pass'))).send_keys(self.password)
         WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located((By.ID, 'u_0_b'))).click()
         #Logged In!

    def search_user(self,user):
        self.login();
        time.sleep(5)
        WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_all_elements_located((By.CLASS_NAME, 'rmlgq0sb')))[0].send_keys(user)
        time.sleep(1)
        self.keyboard.press(Key.enter)
        #
        
        
    def get_user(self,user):
        self.search_user(user)
        time.sleep(5)
        WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_all_elements_located((By.CLASS_NAME, 'dkezsu63')))[0].click()


        # 75 1
    def message_user(self,user,message =''):
        self.login()
        time.sleep(5)
        WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_all_elements_located((By.CLASS_NAME, 'ozuftl9m')))[38].click()
        
me  = FacebookBot()

me.message_user('Hemachandra Ningombam',message= 'TEsting')