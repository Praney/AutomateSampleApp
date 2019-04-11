import re
import os,sys
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from AutomateSampleApp.Locators.elements import PageLocators
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

class BasePage(object):

    # Base class to initialize the base page that will be called from all pages

    def __init__(self,driver):
        self.driver = driver
    
class Notif(BasePage):
    
    def click_on_notif(self):
        notification = self.driver.find_element(*PageLocators.notif)
        notification.click()
        self.driver.open_notifications()
        notificationTitles = self.driver.findElements(*PageLocators.title)
        notificationTitles.click();
        assert notificationTitles.text == "Notification Text"
