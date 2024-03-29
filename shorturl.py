import time
import cloudscraper
from bs4 import BeautifulSoup 
import requests

url = "https://urlsopen.com/ZuKH"  #@param {type:"string"}


# leech with credits broo
# ---------------------------------------------------------------------------------------------------------------------

def shourturl(url):
    
    client = cloudscraper.create_scraper(allow_brotli=False)
    
    
    DOMAIN = "https://blogpost.viewboonposts.com/e893f1f665f5e75f2d1ae009e0063ed66f89"

    url = url[:-1] if url[-1] == '/' else url

    code = url.split("/")[-1]
    
    final_url = f"{DOMAIN}/{code}"
    
    ref = "https://blog.textpage.xyz/"
    
    h = {"referer": ref}
  
    resp = client.get(final_url,headers=h).text
   
    soup = BeautifulSoup(resp, "html.parser")
    
    inputs = soup.find_all("input")
   
    data = { input.get('name'): input.get('value') for input in inputs }

    h = { "x-requested-with": "XMLHttpRequest" }
    time.sleep(2)
    r = client.post(f"{DOMAIN}/links/go", data=data, headers=h)
    try:
        c = r.json()['url']
        return c
    except: return "Something went wrong :("
    
# ---------------------------------------------------------------------------------------------------------------------
print(shourturl(url))
