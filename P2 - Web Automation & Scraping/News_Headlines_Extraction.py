#First of all we are going to create a driver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#Define the website and path we are using. 
website = "https://www.elfinancierocr.com/"
path = "C:\\Users\\Gino\\Downloads\\chromedriver.exe"

#Here we create the driver using the path we defined before. And create a service object to pass it to the driver.
service= Service(executable_path=path)
driver = webdriver.Chrome(service=service)


driver.get(website)
containers = driver.find_elements(by="xpath", value="//div[@class='promo-headline ']")

for container in containers:
    title = container.find_element(by="xpath", value="./h3/a")
    print(title.text)



#//div[@class='promo-headline ']/h3/a