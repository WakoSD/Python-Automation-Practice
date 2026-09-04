#We import the library Pandas
import pandas as pd
import requests

#URL of the webpage
url = "https://en.wikipedia.org/wiki/Dark_(TV_series)"
#We make the request with a user-agent header to avoid being blocked by the website
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)
#This is a function that extracts tables from a website and returns them as a list of DataFrames
dark = pd.read_html(response.text)
#Printing amount of tables extracted from the website
print("Test. Printing length: " + str(len(dark)))
print(dark[1])
