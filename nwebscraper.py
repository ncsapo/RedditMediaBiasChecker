

import requests
from bs4 import BeautifulSoup

#Where are we getting this info?
bias_checking_website = "https://mediabiasfactcheck.com/"

#Takes in the name of the media you want to fact-check. Needs to be identical to the bias_checking_website url to the source
def getBias(sourceName):
    URL = bias_checking_website + sourceName
    #Load the webpage and get the content, call it page_content
    page = requests.get(URL)
    page_content = BeautifulSoup(page.content, 'html.parser')
    #Find images on the website with the attribute "data-image-title" and assign the title's value as extractedTitle. This is the unique title given to the image showing bias on each page. This title conviniently is short and is named after the bias it shows. E.g. left07
    img_details = pageContent.find("img", attrs={"data-image-title":True})
    extractedTitle = img_details['data-image-title']
    #return the title without the numbers at the end
    return extractedTitle[:-2]

print("nwebscraper loaded")