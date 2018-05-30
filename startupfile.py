import os
import sys
from appium import webdriver
import subprocess

def startup():
    dir = os.path.dirname(__file__)
    apkpath = os.path.join(dir,'APK/app-debug.apk')
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '8.0'
    desired_caps['deviceName'] = 'Nexus_5X_API_27:5554'
    desired_caps['automationName']='UiAutomator2'
    desired_caps['isHeadless']='true'
    desired_caps['app'] = apkpath
    desired_caps['unicodeKeyboard'] = 'true'
    desired_caps['resetKeyboard'] = 'true'
    
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    return driver