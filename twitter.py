from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from fake_useragent import UserAgent
from selenium.webdriver.chrome.options import Options
from auto_application_helpers import init
import time
import pickle
import math

def post_to_twitter(tweet):
    USERNAME = 'MissingPieceJG'
    PW = 'JeffGreen$1'

    driver = webdriver.Firefox();
    driver.get("https://www.twitter.com")

    time.sleep(2)
    ## Login 
    el = driver.find_element_by_xpath("//*[contains(text(), 'Log in')]")
    el.click()

    # fill out the username 
    time.sleep(2)
    el = driver.find_element_by_xpath("//*[contains(text(), 'email')]")
    el.click()
    action = ActionChains(driver)
    action.send_keys(USERNAME)
    action.perform()

    # "type" in your password 
    time.sleep(2)
    el = driver.find_element_by_xpath("//*[contains(text(), 'Password')]")
    el.click()
    action2 = ActionChains(driver)
    action2.send_keys(PW, Keys.ENTER)
    action2.perform()

    time.sleep(5)
    el = driver.find_element_by_class_name("DraftEditor-editorContainer")
    el.click()
    time.sleep(2)
    action3 = ActionChains(driver)
    action3.send_keys(tweet)
    action3.perform()

    el = driver.find_element_by_xpath("//*[contains(text(), 'Tweet')]")
    el.click()
    time.sleep(3)
    action4 = ActionChains(driver)
    time.sleep(3)
    action4.send_keys(tweet)
    action4.perform()
    time.sleep(1)
    el = driver.find_element_by_xpath("//*[contains(text(), 'Tweet')]")
    el.click()

