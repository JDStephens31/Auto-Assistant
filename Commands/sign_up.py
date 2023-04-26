import time
import json
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv

load_dotenv()

path = "C:\\Users\\jonet\\Downloads\\Installers\\chromedriver_win32\\chromedriver.exe"

params = {
    "email": os.getenv("EMAIL"),
    "password": os.getenv("password"),
    "first_name": os.getenv("FIRST_NAME"),
    "last_name": os.getenv("LAST_NAME"),
    "username": os.getenv("USERNAME"),
    "phone": os.getenv("PHONE")
}

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, executable_path=path)
assistance_required = False


def start(url):
    driver.get(url)
    time.sleep(3)
    driver.find_element(By.PARTIAL_LINK_TEXT, "up" or "register").click()
    return "Opened Page"


def get_entries(url):
    with open('C:\\Users\\jonet\\Documents\\GitHub\\BonzyBuddy-Assistant\\Data\\register.json') as f:
        data = json.load(f)
    for i in data:
        if i['url'] or i['url'] + '/' == url:
            print(i['url'] or i['url'] + '/')
            print("Found url")
            if i['params']['email']['required'] is True:
                emailXpath = i['params']['email']['xpath']
                email = driver.find_element(By.XPATH, emailXpath)
                print(params['email'])
                email.send_keys(params['email'])
            if i['params']['password']['required'] is True:
                passwordXpath = i['params']['password']['xpath']
                password = driver.find_element(By.XPATH, passwordXpath)
                password.send_keys(params['password'])
            if i['params']['first_name']['required'] is True:
                first_nameXpath = i['params']['first_name']['xpath']
                first_name = driver.find_element(By.XPATH, first_nameXpath)
                first_name.send_keys(params['first_name'])
            if i['params']['last_name']['required'] is True:
                last_nameXpath = i['params']['last_name']['xpath']
                last_name = driver.find_element(By.XPATH, last_nameXpath)
                last_name.send_keys(params['last_name'])
            if i['params']['phone']['required'] is True:
                phoneXpath = i['params']['phone']['xpath']
                phone = driver.find_element(By.XPATH, phoneXpath)
                phone.send_keys(params['phone'])
            if i['params']['username']['required'] is True:
                usernameXpath = i['params']['username']['xpath']
                username = driver.find_element(By.XPATH, usernameXpath)
                username.send_keys(params['username'])
            if i['params']['confirm_password']['required'] is True:
                confirm_passwordXpath = i['params']['confirm_password']['xpath']
                confirm_password = driver.find_element(By.XPATH, confirm_passwordXpath)
                confirm_password.send_keys(params['password'])
            if i['params']['confirm_email']['required'] is True:
                confirm_emailXpath = i['params']['confirm_email']['xpath']
                confirm_email = driver.find_element(By.XPATH, confirm_emailXpath)
                confirm_email.send_keys(params['email'])
            if i['params']['captcha']['required'] is True:
                assistance_required = True
            if i['params']['submit']['required'] is True:
                if assistance_required:
                    print("Assistance required")
                    return "Final Answer:"
                else:
                    submitXpath = i['params']['submit']['xpath']
                    driver.find_element(By.XPATH, submitXpath).click()
                    return "Successfully registered"
        return "Done"
