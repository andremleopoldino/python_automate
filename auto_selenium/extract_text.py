import time
import os.path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from setup import get_driver



URL = "https://automated.pythonanywhere.com/"

def get_temperature_value(url):
    driver = get_driver(URL)
    time.sleep(2)
    element = driver.find_element(By.XPATH, "/html/body/div[1]/div/h1[2]")
    return element.text

