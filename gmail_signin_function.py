from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager 
from time import sleep


def gmail_sign_in(email, password, url):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://accounts.google.com/ServiceLogin?service=mail&continue=https://mail.google.com/mail/#identifier")
    sleep(5)
    driver.find_element(By.NAME,"identifier").send_keys(email)
    sleep(3)
    driver.find_element(By.ID,"identifierNext").click()
    sleep(15)
    driver.find_element(By.NAME,"Passwd").send_keys(password)
    sleep(3)
    driver.find_element(By.ID,"passwordNext").click()
    sleep(40)
    print("[+] Signin successful")

email = "userbajwa64"
password = "Test0987@"
url = "https://mail.google.com"
 
gmail_sign_in(email, password, url)