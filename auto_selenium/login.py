from setup import get_driver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
from extract_text import get_temperature_value 

BASE_URL = "http://automated.pythonanywhere.com/"
LOGIN= BASE_URL + "login"

def login():
    driver = get_driver(LOGIN)
    driver.find_element(By.ID, "id_username").send_keys("automated")
    time.sleep(2)
    driver.find_element(By.ID, "id_password").send_keys("automatedautomated" + Keys.RETURN)
    get_temperature = get_temperature_value(BASE_URL)
    
    

