import bs4
import requests
from bs4 import BeautifulSoup as soup
import urllib

#we're gonna parse newegg for graphics cards
url = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20cards'

#open the connection, grab the page
neweggpage = urllib.request.urlopen(url)
neweggpage_html = neweggpage.read()
neweggpage.close()

#html parsing
page_soup = soup(neweggpage_html, "html.parser")

#this will search the 'div' for item-container, which in this case holds all the graphics card info
#there are typically 12 of these item-containers on the page, one for each card
page_container = page_soup.findAll("div", {"class":"item-container"})

#just taking the first item in the container as an example
#we could also do a for loop here to find all 12 cards
for product in page_container:
    #parse the product name
    product_name = product.img["title"]

    #create a container for the tag which contains the price
    product_price_container = product.findAll("li", {"class":"price-current"})

    #parse the product price
    product_price_1 = product_price_container[0]
    product_price = product_price_1.strong.text

    #this is the decimal price, which is a separate tag, bc it's a superscript
    product_decimal = product_price_1.sup.text
    print(f'The {product_name} is ${product_price}{product_decimal}.')