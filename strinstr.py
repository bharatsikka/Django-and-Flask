
url = 'URL'
import requests
import browser_cookie3
cj = browser_cookie3.chrome()
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

d = requests.get(url, cookies = cj)
newfile = open('file.doc','wb')
newfile.write(d.content)
newfile.close()