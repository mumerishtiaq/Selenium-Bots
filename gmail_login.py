from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

print('Enter the gmailid and password')
gmailId, passWord = map(str, input().split())
try:
	driver = webdriver.Chrome(ChromeDriverManager().install())
	driver.get(r'https://accounts.google.com/signin/v2/identifier?continue='+\
	'https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1'+\
	'&flowName=GlifWebSignIn&flowEntry = ServiceLogin')
	driver.implicitly_wait(15)

	loginBox = driver.find_element("xpath",'//*[@id ="identifierId"]')
	loginBox.send_keys(gmailId)

	nextButton = driver.find_element("xpath",'//*[@id ="identifierNext"]')
	nextButton.click()
	
	passWordBox = driver.find_element("xpath",'//*[@id ="password"]/div[1]/div / div[1]/input')
	passWordBox.send_keys(passWord)

	nextButton = driver.find_element("xpath",'//*[@id ="passwordNext"]')
	nextButton.click()

	print('Login Successful...!!')
except:
	print('Login Failed')


# "without try and except"
# from selenium import webdriver
# from time import sleep
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager 


# print('Enter the gmailid and password')
# gmailId, passWord = map(str, input().split())
# # driver = webdriver.Chrome(ChromeDriverManager().install())
# driver = webdriver.Chrome()
# driver.get("https://accounts.google.com/ServiceLogin?service=mail&continue=https://mail.google.com/mail/#identifier")
# sleep(5)
# driver.find_element(By.NAME,"identifier").send_keys(gmailId)
# sleep(3)
# driver.find_element(By.ID,"identifierNext").click()
# sleep(15)
# driver.find_element(By.NAME,"Passwd").send_keys(passWord)
# sleep(3)
# driver.find_element(By.NAME,"passwordNext").click()
# sleep(40)
# print("[+] Signin successful")
