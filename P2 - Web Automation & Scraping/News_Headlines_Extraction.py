#First of all we are going to create a driver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#Define the website and path we are using. 
website = "https://www.lateja.cr/"
path = "C:\\Users\\Gino\\Downloads\\chromedriver.exe"

#Here we create the driver using the path we defined before. And create a service object to pass it to the driver.
service= Service(executable_path=path)
driver = webdriver.Chrome(service=service)

driver.get(website)
input("Press Enter to close the browser...")

