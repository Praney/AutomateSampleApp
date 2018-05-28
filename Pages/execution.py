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

    # Base class to initialize the base page that will be called from all pages

    def __init__(self,driver):
        self.driver = driver
        driver.implicitly_wait(5)
        
    
class CityTemp(BasePage):
    
    def reachtoTempPage(self):
        city = self.driver.find_element(*PageLocators.city)
        city.click()

    def testTemp(self,lat,longi,case):
            
        if case == 1 :
            CityTemp.allTempertures(self,lat,longi,1)
        elif case == 2 :
            CityTemp.allTempertures(self,lat,longi,2)
        else :
            CityTemp.allTempertures(self,lat,longi,3)

    def addCity(self):
    
        city = self.driver.find_element(*PageLocators.add)
        city.click()
        
        searchCity = self.driver.find_element(*PageLocators.enterCityName)
        searchCity.send_keys("new delhi")
        
        sleep(5)

        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID,"com.daniloprado.weather:id/textview_found_city_name")))
        selectCity = self.driver.find_element(*PageLocators.cityList)
        selectCity.click()

        added = self.driver.find_element(*PageLocators.verify)
        assert added.text == "New Delhi"

        self.driver.background_app(10)

        added = self.driver.find_element(*PageLocators.verify)
        added.click()
        
    def allTempertures(self,lat,longi,case):
        
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID,"com.daniloprado.weather:id/textview_temperature")))

        # Call API and get the minimum temperature of the city having lat long
        if case == 1 :
            TempDublinMin = getWeather.weather(lat,longi,1)

            for i in range(0,5):
                daysTempMin = self.driver.find_element(*PageLocators.temparrayMin[i])
                assert TempDublinMin[i] in daysTempMin.text

        # Call API and get the maximum temperature of the city having lat long
        elif case == 2 :
            TempDublinMax = getWeather.weather(lat,longi,2)

            for i in range(0,5):
                daysTempMax = self.driver.find_element(*PageLocators.temparrayMax[i])
                assert TempDublinMax[i] in daysTempMax.text
            back = self.driver.find_element(*PageLocators.navigate)
            back.click()  

        else :
        # Call API and get the current temperature of the city having lat long
            TempDublinNow = getWeather.weather(lat,longi,3)
            nowTemp = self.driver.find_element(*PageLocators.temperature)
            assert TempDublinNow in nowTemp.text 


    def tempNewCity(self,lat,longi,case):
               
        if case == 1 :
            CityTemp.allTempertures(self,lat,longi,1)
        elif case == 2 :
            CityTemp.allTempertures(self,lat,longi,2)
        else :
            CityTemp.allTempertures(self,lat,longi,3)
