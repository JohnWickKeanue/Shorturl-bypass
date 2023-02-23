
import time
import cloudscraper
from bs4 import BeautifulSoup 


url = "https://urlsopen.net/ZuKH"  #@param {type:"string"}


# leech with credits broo
# ---------------------------------------------------------------------------------------------------------------------

def shorturl(url):
    
    client = cloudscraper.create_scraper(allow_brotli=False)
    
    
    DOMAIN = "https://blogpost.viewboonposts.com/go"

    url = url[:-1] if url[-1] == '/' else url

    code = url.split("/")[-1]
    
    final_url = f"{DOMAIN}/{code}"
    
    ref = "https://blog.textpage.xyz/"
    
    h = {"referer": ref}
  
    resp = client.get(final_url,headers=h)
    
    soup = BeautifulSoup(resp.content, "html.parser")
    
    inputs = soup.find_all("input")
   
    data = { input.get('name'): input.get('value') for input in inputs }

    h = { "x-requested-with": "XMLHttpRequest" }
    
    time.sleep(2)
    r = client.post(f"{DOMAIN}/links/go", data=data, headers=h)
    try:
        return r.json()['url']
    except: return "Something went wrong :("
    
# ---------------------------------------------------------------------------------------------------------------------
print(shorturl(url))
