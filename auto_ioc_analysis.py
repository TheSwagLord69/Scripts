# Usage:
# python auto_ioc_analysis.py [insert IOC here]
#
# Saves the time and effort of opening up these websites and typing manually
#
# Dependencies:
# Python 3.9 (https://www.python.org/downloads/release/python-390/)
# Selenium, pip install selenium (https://pypi.org/project/selenium/)
# geckodriver.exe, and add to PATH  (https://github.com/mozilla/geckodriver/releases) I personally added mine to my python39 folder
# pynput, pip install pynput (https://pypi.org/project/pynput/)

import sys
import time
import selenium
from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pynput
from pynput.keyboard import Key, Controller
from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController

try:
    ioc_to_be_searched = str(sys.argv[1])
except:
    print("Usage:\npython auto_ioc_analysis.py [insert IOC here]\ne.g. python auto_ioc_analysis.py 192.168.0.1\ne.g. python auto_ioc_analysis.py phishingsite.com")
    quit()

print("[*] Do not click anything. Let the script run, else the keystrokes may not be sent to the right positions.")
print("Searching: ")
print(ioc_to_be_searched)
print("\n")

#browser = webdriver.Firefox()
browser = Firefox()
browser.maximize_window()
browser.implicitly_wait(20)

keyboard = KeyboardController()
mouse = MouseController()

## Virustotal
browser.get('https://www.virustotal.com/gui/home/search')
time.sleep(4)
keyboard.type(ioc_to_be_searched)
time.sleep(1)
keyboard.press(Key.enter)
keyboard.release(Key.enter)

## Metadefender opswat
#Open new tab
browser.execute_script('''window.open("https://metadefender.opswat.com/","_blank");''')
time.sleep(4)
browser.switch_to.window(browser.window_handles[-1])
time.sleep(2)
keyboard.type(ioc_to_be_searched)
time.sleep(1)
keyboard.press(Key.enter)
keyboard.release(Key.enter)

## ipinfo.io
#Open new tab
browser.execute_script('''window.open("https://ipinfo.io/","_blank");''')
time.sleep(5)
browser.switch_to.window(browser.window_handles[-1])
browser.find_element_by_id('homepage-search-input').click()
time.sleep(2)
keyboard.type(ioc_to_be_searched)
time.sleep(1)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
browser.find_element_by_class_name('js-gtm').click()

## Cisco Talos Intel
#Open new tab
browser.execute_script('''window.open("https://talosintelligence.com/","_blank");''')
time.sleep(4)
browser.switch_to.window(browser.window_handles[-1])
browser.find_element_by_id('rep-lookup').click()
time.sleep(2)
keyboard.type(ioc_to_be_searched)
time.sleep(1)
keyboard.press(Key.enter)
keyboard.release(Key.enter)

## whois.domaintools
#Open new tab
browser.execute_script('''window.open("https://whois.domaintools.com/","_blank");''')
time.sleep(4)
browser.switch_to.window(browser.window_handles[-1])
time.sleep(1)
keyboard.type(ioc_to_be_searched)
time.sleep(1)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
browser.find_element_by_id('whois-search').click()

## dns.google
#Open new tab
browser.execute_script('''window.open("https://dns.google/","_blank");''')
time.sleep(4)
browser.switch_to.window(browser.window_handles[-1])
time.sleep(1)
keyboard.type(ioc_to_be_searched)
time.sleep(1)
keyboard.press(Key.enter)
keyboard.release(Key.enter)

## Wheregoes
#Open new tab
browser.execute_script('''window.open("https://wheregoes.com/","_blank");''')
time.sleep(4)
browser.switch_to.window(browser.window_handles[-1])
time.sleep(1)
keyboard.type(ioc_to_be_searched)
time.sleep(1)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
browser.find_element_by_id('form_button').click()

## secuboxlabs.fr.webstatdata.com
#Open new tab
browser.execute_script('''window.open("https://secuboxlabs.fr.webstatdata.com/","_blank");''')
time.sleep(4)
browser.switch_to.window(browser.window_handles[-1])
time.sleep(1)
keyboard.type(ioc_to_be_searched)
time.sleep(1)
keyboard.press(Key.enter)
keyboard.release(Key.enter)

## Symantec sitereview
#Open new tab
browser.execute_script('''window.open("https://sitereview.bluecoat.com/#/","_blank");''')
time.sleep(4)
browser.switch_to.window(browser.window_handles[-1])
browser.find_element_by_id('txtUrl').click()
time.sleep(1)
keyboard.type(ioc_to_be_searched)
time.sleep(1)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
browser.find_element_by_id('btnLookup').click()

## securitytails bgpview
#Open new tab
browser.execute_script('''window.open("https://bgpview.io/","_blank");''')
time.sleep(4)
browser.switch_to.window(browser.window_handles[-1])
browser.find_element_by_name('query_term').click()
time.sleep(2)
keyboard.type(ioc_to_be_searched)
time.sleep(1)
keyboard.press(Key.enter)
keyboard.release(Key.enter)

## Urlvoid
#Open new tab
browser.execute_script('''window.open("https://www.urlvoid.com/","_blank");''')
time.sleep(4)
browser.switch_to.window(browser.window_handles[-1])
browser.find_element_by_id('hf-domain').click()
time.sleep(1)
keyboard.type(ioc_to_be_searched)
time.sleep(1)
keyboard.press(Key.enter)
keyboard.release(Key.enter)

## threatfox.abuse.ch
#Open new tab
browser.execute_script('''window.open("https://threatfox.abuse.ch/browse/","_blank");''')
time.sleep(4)
browser.switch_to.window(browser.window_handles[-1])
browser.find_element_by_id('search').click()
time.sleep(1)
keyboard.type(ioc_to_be_searched)
time.sleep(1)
keyboard.press(Key.enter)
keyboard.release(Key.enter)

## urlhaus.abuse.ch
#Open new tab
browser.execute_script('''window.open("https://urlhaus.abuse.ch/browse/","_blank");''')
time.sleep(4)
browser.switch_to.window(browser.window_handles[-1])
browser.find_element_by_id('search').click()
time.sleep(1)
keyboard.type(ioc_to_be_searched)
time.sleep(1)
keyboard.press(Key.enter)
keyboard.release(Key.enter)

## riskdiscovery.com honeydb
#Open new tab
browser.execute_script('''window.open("https://riskdiscovery.com/honeydb/#threats","_blank");''')
time.sleep(4)
browser.switch_to.window(browser.window_handles[-1])
browser.find_element_by_id('ip-address').click()
time.sleep(1)
keyboard.type(ioc_to_be_searched)
time.sleep(1)
browser.find_element_by_id('ip-address-search').click()

## greynoise.io
#Open new tab
browser.execute_script('''window.open("https://www.greynoise.io/","_blank");''')
time.sleep(4)
browser.switch_to.window(browser.window_handles[-1])
browser.find_element_by_id('textInput').click()
time.sleep(2)
keyboard.type(ioc_to_be_searched)
time.sleep(1)
keyboard.press(Key.enter)
keyboard.release(Key.enter)

## threatminer.org
#Open new tab
browser.execute_script('''window.open("https://www.threatminer.org/","_blank");''')
time.sleep(4)
browser.switch_to.window(browser.window_handles[-1])
browser.find_element_by_id('searchTerm_main').click()
time.sleep(1)
keyboard.type(ioc_to_be_searched)
time.sleep(1)
keyboard.press(Key.enter)
keyboard.release(Key.enter)

## fraudguard.io
#Open new tab
browser.execute_script('''window.open("https://fraudguard.io/","_blank");''')
time.sleep(4)
browser.switch_to.window(browser.window_handles[-1])
browser.find_element_by_id('ip').click()
time.sleep(1)
keyboard.type(ioc_to_be_searched)
time.sleep(1)
keyboard.press(Key.enter)
keyboard.release(Key.enter)

## spamcop.net/bl.shtml
#Open new tab
browser.execute_script('''window.open("https://www.spamcop.net/bl.shtml","_blank");''')
time.sleep(4)
browser.switch_to.window(browser.window_handles[-1])
browser.find_element_by_name('ip').click()
time.sleep(1)
keyboard.type(ioc_to_be_searched)
time.sleep(1)
keyboard.press(Key.enter)
keyboard.release(Key.enter)

## https://urlscan.io/
#Open new tab
browser.execute_script('''window.open("https://urlscan.io/","_blank");''')
time.sleep(4)
browser.switch_to.window(browser.window_handles[-1])
browser.find_element_by_id('url').click()
time.sleep(1)
keyboard.type(ioc_to_be_searched)
time.sleep(1)
keyboard.press(Key.enter)
keyboard.release(Key.enter)

##https://sitecheck.sucuri.net/
#Open new tab
browser.execute_script('''window.open("https://sitecheck.sucuri.net/","_blank");''')
time.sleep(4)
browser.switch_to.window(browser.window_handles[-1])
time.sleep(1)
keyboard.type(ioc_to_be_searched)
time.sleep(1)
keyboard.press(Key.enter)
keyboard.release(Key.enter)

'''
References:
https://realpython.com/modern-web-automation-with-python-and-selenium/
https://stackoverflow.com/questions/50414007/unable-to-invoke-firefox-headless
https://stackoverflow.com/questions/28715942/how-do-i-switch-to-the-active-tab-in-selenium
https://www.selenium.dev/documentation/webdriver/browser_manipulation/
'''