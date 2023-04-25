import json
from time import sleep
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui

options = webdriver.ChromeOptions()
options.add_argument("--user-data-dir=C:\\Users\\jonet\\AppData\\Local\\Google\\Chrome\\User Data\\Default")


def message(command, talk, get_response):
    global message
    cmd = command.replace('message', '')
    cmd = cmd.strip()
    talk("Messaging " + cmd)
    with open('Data/contact.json') as f:
        data = json.load(f)
    try:
        link = data['Contacts'][cmd]['link']
        sleep(2)
        if link:
            driver = uc.Chrome(options=options)
            driver.get(link)
            pyautogui.press('enter')
            sleep(5)
            driver.find_element(By.XPATH, data["inputXPath"]).click()
            talk("What would you like to say?")
            message = get_response()
            talk("You would like me to send " + message)
            pyautogui.write(message)
            pyautogui.press('enter')
        else:
            talk("An Error Occurred.")

    except KeyError:
        talk("An Error Occurred.")
