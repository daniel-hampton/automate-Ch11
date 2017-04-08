#! python3
# 2048.py - issues up, right, down , left keystrokes to the game at https:///gabrielecirulli.github.io/2048

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# open webdriver navigate to url

url = 'https://gabrielecirulli.github.io/2048'

driver = webdriver.Firefox()

driver.get(url)
bodyElem = driver.find_element_by_css_selector('body')

numCycles = 100

time.sleep(3)

while numCycles:
    bodyElem.send_keys(Keys.UP)
    bodyElem.send_keys(Keys.RIGHT)
    bodyElem.send_keys(Keys.DOWN)
    bodyElem.send_keys(Keys.LEFT)
    numCycles -= 1

scoreElem = driver.find_element_by_css_selector('.score-container')
print('\n\nYour score was {}'.format(scoreElem.text))
