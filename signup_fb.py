from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

path = r"C:\Users\umeri\OneDrive\Desktop\signup_bot\chromedriver.exe"
driver  = webdriver.Chrome(path)

driver.get("https://web.facebook.com/signup")

driver.find_element(By.NAME,"firstname").send_keys("fname")
sleep(3)
driver.find_element(By.NAME,"lastname").send_keys("lname")
sleep(3)
driver.find_element(By.NAME,"reg_email__").send_keys("fmename64@gmail.com")
sleep(3)
driver.find_element(By.NAME,"reg_email_confirmation__").send_keys("fmename64@gmail.com")
sleep(3)
driver.find_element(By.NAME,"reg_passwd__").send_keys("Random46@")
sleep(3)
driver.find_element(By.NAME,"birthday_day").send_keys("9")
sleep(2)
driver.find_element(By.NAME,"birthday_month").send_keys("Nov")
sleep(2)
driver.find_element(By.NAME,"birthday_year").send_keys("2000")
sleep(2)
driver.find_element(By.NAME,"sex").click()
sleep(1)
driver.find_element(By.NAME,"websubmit").click()
print("[+] Signup successful")