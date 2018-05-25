from time import sleep
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from Shpock.Locators.elements import PageLocators
import logging
from appium.webdriver.common.touch_action import TouchAction
from selenium import webdriver
from appium import webdriver
import re
import os,sys
from Shpock.API import getWeather


class BasePage(object):

    # """Base class to initialize the base page that will be called from all pages"""

    def __init__(self,driver):
        self.driver = driver
        driver.implicitly_wait(5)
        
    
class CityTemp(BasePage):
    def testTemp(self):
        city = self.driver.find_element(*PageLocators.city)
        city.click()
        
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.ID,"com.daniloprado.weather:id/textview_temperature")))

        TempDublin = getWeather.weather(53.35014,-6.266155)
        nowTemp = self.driver.find_element(*PageLocators.temperature)
        logging.info(TempDublin)
        logging.info(nowTemp.text)
        assert TempDublin in nowTemp.text 

        back = self.driver.find_element(*PageLocators.navigate)
        back.click()

class CityAdd(BasePage):
    def addCity(self):
    
        city = self.driver.find_element(*PageLocators.add)
        city.click()
        
        searchCity = self.driver.find_element(*PageLocators.enterCityName)
        searchCity.send_keys("perth")
        selectCity = self.driver.find_element(*PageLocators.cityList)
        sleep(5)
        try :
            if selectCity.is_displayed()==True:
                selectCity.click()
        except NoSuchElementException:
            print("No Suggestion found")
        
        self.driver.background_app(10)
        
        added = self.driver.find_element(*PageLocators.verify)
        assert added.text == "Perth"
        added.click()
        currentTemperature = getWeather.weather(-31.950526900000003,115.86045719999998)
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.ID,"com.daniloprado.weather:id/textview_temperature")))
        nowTemp = self.driver.find_element(*PageLocators.temperature)
        logging.info(currentTemperature)
        logging.info(nowTemp.text)
        assert currentTemperature in nowTemp.text
        