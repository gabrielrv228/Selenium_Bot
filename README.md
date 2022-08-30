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
