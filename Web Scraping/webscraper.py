from bs4 import BeautifulSoup as soup 
import urllib.request

user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'

url = "https://amturing.acm.org/byyear.cfm"
headers={'User-Agent':user_agent,} 

request= urllib.request.Request(url,None,headers) 
response = urllib.request.urlopen(request)
page_html = response.read() 
response.close()
page_soup = soup(page_html, "html.parser")
containers = page_soup.findAll("ul",{"class" : "award-winners-list"}) 
container = containers[0]
chunk = container.findAll("a")

for links in chunk:
    print (links.get_text())
    