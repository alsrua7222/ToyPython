import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import re

def alert(driver):
    tmp = driver.switch_to.alert
    tmp.accept()

