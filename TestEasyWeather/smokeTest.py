#!/usr/bin/python
# -*- coding: utf-8 -*-
# import unittest
from __future__ import absolute_import
import sys
import os
import logging
from time import sleep
import pytest
from appium import webdriver
from Shpock.startupfile import startup
from Shpock.Pages import execution
from selenium import webdriver
import subprocess

driver = startup()

class TestWeather:

    def test_currentTempinDublin(self):
        # Test Case to check current temperature of pre existing city 
        checkCity= execution.CityTemp(driver)
        checkCity.reachtoTempPage()
        checkCity.testTemp(53.35014,-6.266155,3)

    def test_MinTempInDublinFiveDays(self):
        # Test Case to check mimimum temperature of pre existing city for next five days
        checkCity= execution.CityTemp(driver)
        checkCity.testTemp(53.35014,-6.266155,1)

    def test_MaxTempinDublinFiveDays(self):
        # Test Case to check Maximum Temperature of pre existing city for next five days
        checkCity= execution.CityTemp(driver)
        checkCity.testTemp(53.35014,-6.266155,2)

    def test_addCity(self):
        # Test Case to add new city
        addCity = execution.CityTemp(driver)
        addCity.addCity()
    
    def test_tempInNewCity(self):
        # Test Case to check all the temperatures of newly added city 
        temp  = execution.CityTemp(driver)
        temp.tempNewCity(28.6139391,77.2090212,1)
        temp.tempNewCity(28.6139391,77.2090212,3)
        temp.tempNewCity(28.6139391,77.2090212,2)
        driver.quit()