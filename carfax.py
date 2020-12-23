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


def main():
    b = init()
    get_info(b)


def init():
    print('init start')
    options = Options()
    ua = UserAgent()
    user_agent = ua.random
    print(user_agent)
    options.add_argument(f'user-agent={user_agent}')

    browser = webdriver.Firefox()
#    browser.set_window_size(1920,1080);
    browser.get('https://www.carfax.com/Used-Toyota-Corolla_w631')
    time.sleep(1)
    action = ActionChains(browser)
    zipcode = browser.find_element_by_xpath(
        "//input[@placeholder='Enter zip code']")
    zipcode.click()
    action.send_keys('48322', Keys.ENTER)
    action.perform()
    time.sleep(5)
    print(browser.get_cookies())
    return browser


def get_info(b):
    PER_PAGE = 24
    results = b.find_element_by_id('totalResultCount').text
    clicks = math.ceil(int(results) / PER_PAGE)
    print(clicks)

    for i in range(0, clicks):
        for x in range(0, 25):
            s = 'listing_' + str(x)
            try:
                listing = b.find_element_by_id(s)
                link = listing.find_element_by_tag_name(
                    'a').get_attribute('href')
                car = listing.find_element_by_class_name(
                    'srp-list-item-basic-info-model').text
                price = listing.find_element_by_class_name(
                    'srp-list-item-price').text
                features = listing.find_element_by_class_name(
                    'srp-list-item-special-features')
                children = features.find_elements_by_xpath(".//*")
                mileage = children[0].text
                body_type = children[2].text
                color = children[4].text
                engine = children[6].text
            except:
                print('no more listings')
        next_btn = b.find_element_by_xpath("//*[contains(text(), 'Next')]")
        next_btn.click()
        time.sleep(1)


main()
