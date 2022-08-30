import schedule
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

browser = webdriver.Firefox(executable_path="./drivers/geckodriver")

def job():
schedule.every(1).minutes.do(job) 
browser.get('https://www.blewpass.com/')
capa = DesiredCapabilities.FIREFOX
capa["pageLoadStrategy"] = "none"

browser.execute_script("window.stop();")

text_area = browser.find_element_by_css_selector('div.fpbt_column:nth-child(2) > input:nth-child(1)')

text_area.send_keys("https://www.ouo.io/Zo8LTR")

browser.find_element_by_css_selector('div.fpbt_column:nth-child(3) > input:nth-child(1)').click()
time.sleep(2)

browser.execute_script("window.stop();")

browser.find_element_by_css_selector('.desc > a:nth-child(1)').click()
time.sleep(1)

browser.find_element_by_css_selector('#form-captcha input.btn.btn-main').click()
browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(2)
browser.execute_script("window.stop();")

act = webdriver.ActionChains(browser)
a = browser.find_element_by_css_selector('#btn-main')

act.move_to_element(a)
act.click(a)
act.perform()
browser.execute_script("window.stop();")

act.key_down(Keys.CONTROL).key_down(Keys.TAB).key_up(Keys.TAB).key_up(Keys.CONTROL).perform()
time.sleep(1)

time.sleep(2)
browser.quit()
