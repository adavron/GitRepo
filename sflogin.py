#!/usr/local/bin/python2.7

'''Renews firewall session in  every 45 min'''

import time
from selenium import webdriver

import cred  #this imports credentials from file.

while True:
    w=webdriver.Firefox()
    w.implicitly_wait(3)
    # If current session is active logs out,
    # If session is inactive this part will be skipped.
    try:
        w.get('Put session url here')
        w.find_element_by_name('logout').click()
    except Exception:
        pass
    
    # After active sesion terminated, below line logs in to firewall.
    w.get('https:// URL To Login session')
    w.find_element_by_name('login').click()
    w.find_element_by_name('username').send_keys('UserNameHere')
    w.find_element_by_name('password').send_keys('UserPasswordHere')
    w.find_element_by_name('Login').click()
    w.close()
    
    time.sleep(2700) #waits 45 min and starts again...
