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
from twitter import post_to_twitter
import time
import pickle
import math

dic = {'AEA' : '+2000'}

#def init():
#    print('init start')
#    options = Options()
#    ua = UserAgent()
#    user_agent = ua.random
#    options.add_argument(f'user-agent={user_agent}')
#
#    browser = webdriver.Firefox()
#    browser.get('https://www.espn.com/nba/playbyplay?gameId=401266805')
#    time.sleep(2)
#    return browser

def check_for_jeff_score(b):
    time.sleep(2)
    jg = False
    post_to_twitter('Missing piece Jeff Green')
    while True:
        elem = b.find_element_by_class_name('scoring-play')
        if 'Jeff Green enters' in elem.text and not jg:
            post_to_twitter('Missing piece Jeff Green has checked in')
            jg = True
        if 'Jeff Green steals' in elem.text and not jg:
            post_to_twitter('Missing piece Jeff Green steal')
        if 'Jeff Green assists' in elem.text and not jg:
            post_to_twitter('Missing piece Jeff Green assist')
        if 'Jeff Green makes two' in elem.text and not jg:
            post_to_twitter('Missing piece Jeff Green scores')
        if 'for Jeff Green' in elem.text and not jg:
            post_to_twitter('Missing piece Jeff Green has checked out :(')
        if 'Jeff Green makes dunk' in elem.text and not jg:
            post_to_twitter('Missing piece Jeff Green dunked the ball!')
        if 'Jeff Green turnover' in elem.text and not jg:
            post_to_twitter('Missing piece Jeff Green turned the ball over :(')
        if 'Jeff Green' not in elem.text:
            jg = False
        time.sleep(5)

browser = init('https://www.espn.com/nba/playbyplay?gameId=401266805')
check_for_jeff_score(browser)
