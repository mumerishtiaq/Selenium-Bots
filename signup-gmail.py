from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

path = r"C:\Users\umeri\OneDrive\Desktop\signup_bot\chromedriver.exe"
driver  = webdriver.Chrome(path)

driver.get("https://accounts.google.com/signup/v2/webcreateaccount?biz=false&cc=PK&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&dsh=S436504173%3A1668017119330516&emr=1&flowEntry=SignUp&flowName=GlifWebSignIn&followup=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&ifkv=ARgdvAsnmR40oM_WWPO57fg5nN6ZGyNrWcdhMz5WwNfQWm3C8_QstrNleF_Mr_6KMlSAZtVtRaHxag&osid=1&service=mail")

driver.find_element(By.NAME,"firstName").send_keys("fname")
sleep(3)
driver.find_element(By.NAME,"lastName").send_keys("lname")
sleep(3)
driver.find_element(By.NAME,"Username").send_keys("fmeename64")
sleep(3)
driver.find_element(By.NAME,"Passwd").send_keys("Random46@64")
sleep(3)
driver.find_element(By.NAME,"ConfirmPasswd").send_keys("Random46@64")
sleep(3)
driver.find_element(By.CLASS_NAME,"VfPpkd-RLmnJb").click()
sleep(10)
driver.find_element(By.NAME,"day").send_keys("10")
sleep(2)
driver.find_element(By.ID,"month").send_keys("Nov")
sleep(2)
driver.find_element(By.NAME,"year").send_keys("2000")
sleep(2)
driver.find_element(By.ID,"gender").send_keys("Male")
sleep(2)
driver.find_element(By.CLASS_NAME,"VfPpkd-RLmnJb").click()
sleep(5)
driver.find_element(By.CLASS_NAME,"VfPpkd-vQzf8d").click()
sleep(15)
print("[+] Signup successful")