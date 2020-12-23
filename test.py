from selenium import webdriver;
from selenium.webdriver.common.by import By;
from selenium.webdriver.common.keys import Keys;

browser=webdriver.Firefox()
browser.get('https://www.mongodb.com/careers/jobs/2332306?t=ircv7l')

a = []
a = browser.find_elements_by_xpath('//span[@class="asterisk"]');

print(a)

