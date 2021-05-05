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
    #Find images on the website with the attribute "data-image-title" and assign the title's value.
    images = page_content.find_all("img", attrs = {"data-attachment-id":True})#image-title":True})

    bias = images[0]
    bias_title = bias['data-image-title']

    factual_reporting = images[2]
    factual_reporting_title = factual_reporting['data-image-title']

    #return the title without the numbers at the end
    return bias_title[:-2], factual_reporting_title[4:]

print(getBias('hot-air'))

print("nwebscraper loaded")