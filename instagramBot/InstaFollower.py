from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import ElementClickInterceptedException
import time


class InstaFollower:

    def __init__(self):
        # Declare variables
        self.login_element = None
        self.password_element = None
        self.to_follow = None
        # Initialize webdriver
        s = Service("Selenium chrome driver path")
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(service=s, options=chrome_options)
        self.driver.get("https://www.instagram.com/")
        self.driver.maximize_window()

    def login(self, login, password):
        driver = self.driver
        # Accept cookies
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, '.x1ja2u2z .xs83m0k .x7r02ix div ._a9--').click()
        driver.implicitly_wait(5)
        # Login to an account
        self.login_element = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        self.login_element.send_keys(login)
        self.password_element = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        self.password_element.send_keys(password)
        driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button/div').click()
        time.sleep(6)

    def search_insta_account(self, account):
        # Move to instagram account
        self.driver.get(f"https://www.instagram.com/{account}/")
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.CSS_SELECTOR, '.x1qjc9v5 .x78zum5 .xl565be a').click()
        time.sleep(2)

    def get_followers_list(self):
        driver = self.driver
        # Scroll
        scrollable_popup = driver.find_element(By.CSS_SELECTOR, '._aano')
        while True:
            last_height = driver.execute_script("return document.getElementsByClassName('_aano')[0].scrollHeight")
            driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scrollable_popup)
            time.sleep(1)
            new_height = driver.execute_script("return document.getElementsByClassName('_aano')[0].scrollHeight")
            if last_height == new_height:
                return driver.find_elements(By.CSS_SELECTOR, '._aano div div .x1i10hfl ._acan')

    def follow_profiles(self, list_of_accounts):
        for account in list_of_accounts:
            try:
                account.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                self.driver.find_element(By.CSS_SELECTOR, '._a9-z ._a9_1').click()
                account.click()
                time.sleep(1)
