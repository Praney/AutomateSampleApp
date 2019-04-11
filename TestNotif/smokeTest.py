#!/usr/bin/python
# -*- coding: utf-8 -*-
# import unittest
from __future__ import absolute_import
import sys
import os
import pytest
from appium import webdriver
from AutomateSampleApp.startupfile import startup
from AutomateSampleApp.Pages import execution
from selenium import webdriver
import subprocess

driver = startup()

class TestWeather:

    def test_currentTemperatureinDublin(self):
        # Test Case to check current temperature of pre existing city 
        checkNotification= execution.Notif(driver)
        checkNotification.click_on_notif()
        driver.quit()