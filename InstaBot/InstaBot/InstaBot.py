from selenium import webdriver
import sys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

#TAKES USERNAME AND PASSWORD AS INPUT FROM THE CONSOLE
username = sys.argv[1]
password = sys.argv[2]
class InstaBot():
    def __init__(self,username,password):
        self.username  = username
        self.password = password
        self.driver = webdriver.Chrome(r'C:\Aryamann\chromedriver.exe')
        
        self.base_url = 'https://www.instagram.com'
        
    def login(self):
        #LOGGING IN
        self.driver.get(self.base_url)
        time.sleep(1)
        WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input'))).send_keys(self.username)
        WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input'))).send_keys(self.password)
        WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]/button'))).click()
    def get_user_page(self,user):
        self.login()
        time.sleep(6)
        self.driver.get(f'{self.base_url}/{user}')

    def follow_user(self,user):

        self.get_user_page(user)
        time.sleep(3)
        WebDriverWait(self.driver,20).until(expected_conditions.presence_of_all_elements_located((By.CLASS_NAME,'_5f5mN')))[0].click()

    def unfollow_user(self,user):
        
        self.get_user_page(user)
        time.sleep(3)
        WebDriverWait(self.driver,20).until(expected_conditions.presence_of_all_elements_located((By.CLASS_NAME,'_5f5mN')))[0].click()
        time.sleep(1)
        WebDriverWait(self.driver,20).until(expected_conditions.presence_of_all_elements_located((By.CLASS_NAME,'aOOlW')))[0].click()
    def block_user(self,user):
        
        self.get_user_page(user)
        time.sleep(3)
        WebDriverWait(self.driver,20).until(expected_conditions.presence_of_all_elements_located((By.CLASS_NAME,'_8-yf5')))[0].click()
        time.sleep(1)
        WebDriverWait(self.driver,20).until(expected_conditions.presence_of_all_elements_located((By.CLASS_NAME,'aOOlW')))[0].click()
        time.sleep(1)
        WebDriverWait(self.driver,20).until(expected_conditions.presence_of_all_elements_located((By.CLASS_NAME,'aOOlW')))[0].click()
       
    def restrict_user(self,user):
        self.get_user_page(user)
        time.sleep(3)
        WebDriverWait(self.driver,20).until(expected_conditions.presence_of_all_elements_located((By.CLASS_NAME,'_8-yf5')))[0].click()
        time.sleep(1)
        WebDriverWait(self.driver,20).until(expected_conditions.presence_of_all_elements_located((By.CLASS_NAME,'aOOlW')))[1].click()
        time.sleep(1)
        WebDriverWait(self.driver,20).until(expected_conditions.presence_of_all_elements_located((By.CLASS_NAME,'sqdOP')))[0].click()
        
    def report_user(self,user):
        self.get_user_page(user)
        time.sleep(3)
        WebDriverWait(self.driver,20).until(expected_conditions.presence_of_all_elements_located((By.CLASS_NAME,'_8-yf5')))[0].click()
        time.sleep(1)
        
        WebDriverWait(self.driver,20).until(expected_conditions.presence_of_all_elements_located((By.CLASS_NAME,'aOOlW')))[1].click()



InstaBot1 = InstaBot(username,password)
InstaBot1.unfollow_user('garyvee')



