from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from fake_useragent import UserAgent
from selenium.webdriver.chrome.options import Options
import time
import pickle
import math

dic = {'AEA' : '+2000'}

def init():
    print('init start')
    options = Options()
    ua = UserAgent()
    user_agent = ua.random
    print(user_agent)
    options.add_argument(f'user-agent={user_agent}')

    browser = webdriver.Firefox()
    browser.get('https://www.betallweek.com/?logout=yes')
    time.sleep(5)
    print(browser.get_cookies())
    return browser

def login(b):
    user = b.find_element_by_id('account')
    user.send_keys('DI715')
    pw = b.find_element_by_id('password')
    pw.send_keys('mezra01')
    log_button = b.find_element_by_id('login_submit')
    log_button.click();
    time.sleep(3)
    live = b.find_element_by_id('ctl00_ctl00_LiveBetting')
    live.click();
    time.sleep(10);
    names = b.find_element_by_class_name('nameTeam')
    print(names)
    #while True:
    #    for elem in dic:
    #        string = "//*[contains(text(),'" + elem + "')]"
    #        print(string)
    #        bet = b.find_element_by_xpath(string)
    #    time.sleep(10)

browser = init()
login(browser)
