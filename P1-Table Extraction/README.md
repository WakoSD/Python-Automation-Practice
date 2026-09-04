# Lesson Learned

## Extract Tables from Websites

I encountered an issue to run the program. Seems like wikipedia is blocking access due to security.
We need to download the HTML first with requests and then pass it to pandas.read.html
With

´´´
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)
´´´

We are creating a header dictionary.
With out this, a lot of websites block the request because seems to be coming from a "bot".
I also learned that headers are like some additional information on request to web server.

It worked at certain point, but I did not like the result. Was not complete and not easy to read only using print.

Web Scraping consists in extracting data from websites.
Instead of doing manually we can automate it.
We are extracting .csv files from URL using Pandas
