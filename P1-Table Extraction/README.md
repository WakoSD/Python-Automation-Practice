#Results:
## 1. Extract Tables from websites
<img width="1197" height="624" alt="imagen" src="https://github.com/user-attachments/assets/827b42c5-8ac2-4365-9f68-aee87c804736" />

# Lesson Learned
## Extract Tables from Websites

I encountered an issue to run the program. Seems like wikipedia is blocking access due to security.
We need to download the HTML first with requests and then pass it to pandas.read.html

With

```
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)
```

We are creating a header dictionary.
With out this, a lot of websites block the request because seems to be coming from a "bot".
I also learned that headers are like some additional information on request to web server.

It worked at certain point, but I did not like the result. Was not complete and not easy to read only using print.

<img width="942" height="235" alt="imagen" src="https://github.com/user-attachments/assets/940422a6-55b3-4c92-a854-a45730288078" />

Since we are focusing on the automation procedure instead of the UI. I got help for AI for that visual part.
We needed to use Tkinter and Treeview to show correctly.
