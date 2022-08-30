# Selenum_Bot
## This is a Program coded in Python using Selenium that is intended to pass automatically the advertisements of the URL shorter ouo.io. 

This company pays a small amount for every user that passes the multiple ads clicking in determined parts of the webpage. They have implemented diverse measures for avoiding you to pass the adversitments automatically and here I will exlain how I passed all the measures exceptuating the Google captcha.

At first we import all the necesary Python modules for performig the job:

```
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
```
And here comes the program:
- 1. We will define how often is going the script to perform the task.
```
schedule.every(1).minutes.do(job) 
```
- 2. Here we will solve an issue: The web detects the ip address of the machine and does not pay more than one visit.
I have made use of a free proxy service for changing the ip adress every attempt. This part of the script pastes the adversitment url and navigates to it automatically.
```
browser.get('https://www.blewpass.com/')
capa = DesiredCapabilities.FIREFOX
capa["pageLoadStrategy"] = "none"

browser.execute_script("window.stop();")

text_area = browser.find_element_by_css_selector('div.fpbt_column:nth-child(2) > input:nth-child(1)')

text_area.send_keys("https://www.ouo.io/Zo8LTR")

browser.find_element_by_css_selector('div.fpbt_column:nth-child(3) > input:nth-child(1)').click()
time.sleep(2)
```
- 3. We make use of ```time.sleep``` for allowing the page to load properly. 

- 4. We stop the load of the page for avoiding unnecesary things to appear.
```
browser.execute_script("window.stop();")
```
- 5. We perform a simple clicks of the first publicity skip of the webpage.
```
browser.find_element_by_css_selector('.desc > a:nth-child(1)').click()
time.sleep(1)

browser.find_element_by_css_selector('#form-captcha input.btn.btn-main').click()
```
- 6. Here, in the last screen there is a protection  system taht avoids us to click the element directly instead, we have to click the part of the screen where the element is displayed.
 We scroll and wait: 
```
browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(2)
```
We stop the load of the page again.
```
browser.execute_script("window.stop();")
```
We move to the element and perform a click over the button making use of the Action Chains module.
```
act = webdriver.ActionChains(browser)

a = browser.find_element_by_css_selector('#btn-main')

act.move_to_element(a)
act.click(a)
act.perform()
browser.execute_script("window.stop();")
```
- And finally we move tab and close the browser.
```

act.key_down(Keys.CONTROL).key_down(Keys.TAB).key_up(Keys.TAB).key_up(Keys.CONTROL).perform()
time.sleep(1)



time.sleep(2)
browser.quit()
```
