resume_words = 'test'
FIRST_NAME = 'Ezra'
LAST_NAME = 'Mendelson'
PHONE = '2488021094'
EMAIL = 'ezra.mendelson@gmail.com'

from selenium import webdriver;
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By;
from selenium.webdriver.common.keys import Keys;
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from fake_useragent import UserAgent
from selenium.webdriver.chrome.options import Options
import time
import pickle

def main():
    b = init();
    print(b.get_cookies())
    boolean = check_for_linkedin(b);
    if not boolean:
        asterisk(b);
        submit(b);
    time.sleep(10)


def init():
    print('init start')
    options = Options()
    ua = UserAgent()
    user_agent = ua.random
    print(user_agent)
    options.add_argument(f'user-agent={user_agent}')

    #url = input()
    #browser=webdriver.Chrome(options=options)
    browser=webdriver.Firefox()
    #cookies = pickle.load(open("cookies-greenhouse-io.txt", "rb"))
    #for cookie in cookies:
     #   browser.add_cookie(cookie)
#    browser.set_window_size(1920,1080);
#    browser.get('https://google.com')
    #browser.get('https://boards.greenhouse.io/quora2/jobs/4810866002?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic')
    browser.get('https://boards.greenhouse.io/perch1/jobs/4821724002?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic')
    time.sleep(5)
    print(browser.get_cookies())
    return browser
    

def fill_name():
    #Fill first name
    first_name = browser.find_element_by_id('first_name');
    first_name.send_keys("Ezra");

    #Fill last name
    try:
        last_name = browser.find_element_by_id("last_name");
        first_name.send_keys(Keys.TAB);
        last_name.send_keys("Mendelson");
    except:
        pass
        print('no last name')

def fill_contact():
    #Fill phone
    try:
        phone = browser.find_element_by_id("phone");
        last_name.send_keys(Keys.TAB);
        phone.send_keys('2488021094');
    except:
        pass
        print('no phone')

    #Fill email
    try:
        email = browser.find_element_by_id("email");
        phone.send_keys(Keys.TAB);
        email.send_keys('ezra.mendelson@gmail.com');
    except:
        pass
        print('no email')

def fill_location():
    #Fill location
    try:
        loc = browser.find_element_by_id("job_application_location");
        first_name.send_keys(Keys.TAB);
        loc.send_keys('Ann Arbor');
        autofill = browser.find_element_by_xpath("//*[contains(text(), 'Ann Arbor,')]");
        autofill.click();
    except:
        pass
        print('no location')

def fill_resume():
    #Click Attach Resume '/mnt/c/Users/owner/Documents/Ezra_Mendelson_Resume';
    #browser.find_element_by_xpath("//*[contains(text(), 'Attach')]").send_keys(r"C:\Users\owner\Documents\Ezra_Mendelson_Resume");

    #Click Paste
    paste = browser.find_element_by_xpath("//*[contains(text(), 'Paste')]");
    paste.click();

    resume = browser.find_element_by_id('resume_text');
    resume.send_keys(resume_words);
    resume.send_keys(Keys.TAB, Keys.TAB, Keys.TAB, Keys.TAB, Keys.TAB, Keys.TAB, 'Bachel', Keys.ENTER, Keys.TAB, 'Computer Scienc', Keys.ENTER, Keys.TAB, '09', '2016', Keys.TAB, '05', '2020')

def asterisk(browser):
    print('asterisk start')
    questions = browser.find_elements_by_class_name('asterisk');
    time.sleep(10)
    for q in questions:
        pickle.dump(browser.get_cookies(), open("cookies.pkl", "wb"))
        print(browser.get_cookies());
        action = ActionChains(browser);
        action2 = ActionChains(browser);
        q.click();
        parent = q.find_element_by_xpath('..')
        print(parent)
        print(parent.text)
        if 'First' in parent.text:
            slow_mo(FIRST_NAME, browser)
        elif 'Last' in parent.text:
            slow_mo(LAST_NAME, browser)
        elif 'Phone' in parent.text:
            slow_mo(PHONE, browser)
        elif 'Email' in parent.text:
            slow_mo(EMAIL, browser)
        elif 'Resume' in parent.text:
            action.send_keys(Keys.TAB, Keys.TAB, Keys.TAB, Keys.TAB, Keys.ENTER, Keys.TAB, 'test')
            action.perform();
        elif 'Location' in parent.text:
            action.send_keys('Ann Arbor')
            action.perform();
            time.sleep(5)
            autofill = browser.find_element_by_xpath("//*[contains(text(), 'Ann Arbor,')]");
            autofill.click();
        elif 'School' in parent.text:
            action.send_keys('University of Michigan')
            action.perform();
            time.sleep(3)
            action2.send_keys(Keys.ENTER)
            action2.perform();
        elif 'Degree' in parent.text:
            action.send_keys('Bach')
            action.perform();
            time.sleep(5)
            action2.send_keys(Keys.ENTER)
            action2.perform();
        elif 'Discipline' in parent.text:
            action.send_keys('Computer Scien')
            action.perform();
            time.sleep(5)
            action2.send_keys(Keys.ENTER)
            action2.perform();
        elif 'Start Date' in parent.text:
            action.send_keys(Keys.TAB)
            action.perform();
            action2.send_keys('09', '2016')
            action2.perform();
        elif 'End Date' in parent.text:
            action.send_keys(Keys.TAB)
            action.perform();
            action2.send_keys('05', '2020')
            action2.perform();
        elif 'did you hear' in parent.text:
            action.send_keys('LinkedIn')
            action.perform()
        else:
            action.send_keys('test')
            action.perform();

def submit(browser):
    print('in submit')
    s = browser.find_element_by_id("submit_app");
    s.click();

def slow_mo(word, browser):
    for c in word:
        action = ActionChains(browser);
        action.send_keys(c)
        action.perform()
        action.reset_actions()
        time.sleep(0.1)

def check_for_linkedin(browser):
    action = ActionChains(browser);
    boolean = True
    try:
        autofill = browser.find_element_by_xpath("//span[contains(text(), 'Apply with')]");
        autofill.click();
    except:
        print('Could not find Apply with Linkedin')
        boolean = False
    if boolean:
        try:
            action.send_keys(Keys.ENTER)
            action.perform();
#            submit(browser);
        except:
            boolean = False
            print('Could not submit')
    return boolean


main();
