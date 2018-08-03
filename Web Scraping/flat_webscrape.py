from bs4 import BeautifulSoup as soup 
import urllib.request

user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'

url = "https://www.makaan.com/kolkata-property/barrackpore-flats-for-sale-52043?beds=3plus&propertyType=apartment"
headers={'User-Agent':user_agent,} 

request= urllib.request.Request(url,None,headers) 
response = urllib.request.urlopen(request)
page_html = response.read() 
response.close()
page_soup = soup(page_html, "html.parser")

#Get All BHK Numbers
bhk_number_container = page_soup.findAll("div",{"class" : "title-line-wrap"})
#Get All Flat Names
flat_name_container = page_soup.findAll("div",{"class" : "title-line-wrap"})


for i in range(13):
    bhk_numbers = bhk_number_container[i].find("span",{"class" : "val"})
   
    
    print ("Apartment Number: " + str(i))
    print ("Apartment Detail: " + bhk_numbers.get_text() + " BHK Apartment")
    
    try:
        flat_names = flat_name_container[i].find("span",{"class" : "project-wrap"}).span
        flat_names = flat_name_container[i].find("span",{"class" : "project-wrap"}).span
        print ("Apartment Name: " + flat_names.get_text())
        print()
     
    except:
         print ("Apartment Name: None")
         print()










flat_name_container = page_soup.findAll("div",{"class" : "title-line-wrap"})

for i in range(13):
    try:
        flat_names = flat_name_container[i].find("span",{"class" : "project-wrap"}).span
        print (flat_names.get_text())
    
    except:
        print ("N/A")


    