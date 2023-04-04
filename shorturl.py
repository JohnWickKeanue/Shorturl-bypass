import time
import cloudscraper
from bs4 import BeautifulSoup 
import requests

url = "https://urlsopen.com/ZuKH"  #@param {type:"string"}


# leech with credits broo
# ---------------------------------------------------------------------------------------------------------------------

def shourturl(url):
    
    client = cloudscraper.create_scraper(allow_brotli=False)
    
    
    DOMAIN = "https://blogpost.viewboonposts.com/ssssssagasdgeardggaegaqe"

    url = url[:-1] if url[-1] == '/' else url

    code = url.split("/")[-1]
    
    final_url = f"{DOMAIN}/{code}"
    
    ref = "https://blog.textpage.xyz/?safelink_redirect=eyJzZWNvbmRfc2FmZWxpbmtfdXJsIjoiIiwic2FmZWxpbmsiOiJodHRwczpcL1wvYmxvZy52aWV3Ym9vbnBvc3RzLmNvbVwvc2FmZS5waHA/bGluaz1cL3Nzc3Nzc2FnYXNkZ2VhcmRnZ2FlZ2FxZVwvZFNqUCJ9"
    
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
