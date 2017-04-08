#! python3
# commandLineEmail.py - Uses the selenium package to control Firefox browser to log in and send an email. Email address and message from the command line.

import time
import sys
import webbrowser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

userEmail = 'dhampton084@gmail.com'
subject = 'Automated message'
url = 'https://www.google.com/mail/'

# get email address and message from command line arguments.
if len(sys.argv) > 1:
    recipient = sys.argv[1]
    message = ' '.join(sys.argv[2:])

    # prompt for password
    password = input('\n\nPlease enter your password: ')
    # password =

    # Launch browser, locate username element, send username keys, submit
    driver = webdriver.Firefox()
    driver.get(url)
    driver.implicitly_wait(10)  # seconds

    userElem = driver.find_element_by_id('Email')
    userElem.clear()
    userElem.send_keys(userEmail)
    userElem.submit()

    # Locate password element, send pw keys, submit
    passElem = driver.find_element_by_id('Passwd')
    passElem.clear()
    passElem.send_keys(password)

    # Find and deselect option to "Stay signed in"
    try:
        checkElem = driver.find_element_by_id('PersistentCookie')
        checkElem.click()
    except Exception as err:
        print('An exception happened in checkElem: ' + str(err))

    passElem.submit()

    # Locate compose element, click button, locate subject line, enter subject
    try:
        composeElem = driver.find_element_by_css_selector('.T-I-KE')
        composeElem.click()
    except Exception as err:
        print('An exception happened in composeElem: ' + str(err))

    time.sleep(1)  # to allow "to" field to manipulated

    try:
        recipientElem = driver.find_element_by_css_selector('textarea[name=to]') # #\:8i
        # recipientElem.clear()
        recipientElem.send_keys(recipient)
    except Exception as err:
        print('An exception happened in recipientElem: ' + str(err))

    try:
        subjectElem = driver.find_element_by_css_selector('input[name=subjectbox]')
        # subjectElem.clear()
        subjectElem.send_keys(subject)
    except Exception as err:
        print('An exception happened in subjectElem: ' + str(err))


    # Locate message body element, send keys, locate send button, send message
    try:
        bodyElem = driver.find_element_by_css_selector('div[aria-label="Message Body"')
        # bodyElem.clear()
        bodyElem.send_keys(message)
        bodyElem.send_keys(Keys.CONTROL, Keys.ENTER)
    except Exception as err:
        print('An exception happened in bodyElem: ' + str(err))

    # try:
    #     sendElem = driver.find_element_by_class_name('T-I J-J5-Ji aoO T-I-atl L3')
    #     sendElem.click()
    # except Exception as err:
    #     print('An exception happened in sendElem: ' + str(err))

    # Locate signout element, logout of gmail.
    try:
        menuElem = driver.find_element_by_css_selector('a[href="https://accounts.google.com/SignOutOptions?hl=' +
                                                       'en&continue=https://mail.google.com/mail&service=mail"')
        menuElem.click()
    except Exception as err:
        print('An exception happened in menuElem: ' + str(err))

    time.sleep(1)  # wait for menu to appear

    try:
        logoutElem = driver.find_element_by_css_selector('#gb_71')
        logoutElem.click()
    except Exception as err:
        print('An exception happened in logoutElem: ' + str(err))

    time.sleep(1)  # wait for logout to complete

    driver.quit()

else:
    print('Opening email homepage...')
    webbrowser.open(url)
