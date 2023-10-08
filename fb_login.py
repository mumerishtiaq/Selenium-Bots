import selenium
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

username = "username"
password = "password"

path = "C:\Users\Dell\Desktop\loginbot\chromedriver.exe"
# initialize the Chrome driver
driver = webdriver.Chrome(path)


driver.get("https://www.facebook.com/login")
driver.maximize_window()
driver.find_element(By.ID,"email").send_keys(username)
sleep(3)
driver.find_element(By.ID,"pass").send_keys(password)
sleep(2)
#driver.find_element(by=By.CSS_SELECTOR, value="1").click()
driver.find_element(By.ID,"loginbutton").click()
print("[+] Login successful")