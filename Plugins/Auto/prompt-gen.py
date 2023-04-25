import os
import json
from time import sleep
import datetime
import random
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui
import openai
from dotenv import load_dotenv

options = webdriver.ChromeOptions()
options.add_argument("--user-data-dir=C:\\Users\\jonet\\AppData\\Local\\Google\\Chrome\\User Data\\Default")

# OpenAI Initialization
openai.organization = os.getenv("OPENAI_ORG")
openai.api_key = os.getenv("OPENAI_KEY")

def prompt_generator():
