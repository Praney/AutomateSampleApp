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

    def test_tempDublin(self):
        checkCity= execution.CityTemp(driver)
        checkCity.testTemp()
        # sleep(5)

    def test_addCity(self):
        addCity = execution.CityAdd(driver)
        addCity.addCity()
        driver.quit()