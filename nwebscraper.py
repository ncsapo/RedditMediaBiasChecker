import requests
from bs4 import BeautifulSoup

#Where are we getting this info?
bias_checking_website = "https://mediabiasfactcheck.com/"

#Takes in the name of the media you want to fact-check. Needs to be identical to the bias_checking_website url to the source
def getBias(sourceName):
    print("blah blah: ", sourceName)
    URL = sourceName
    #Load the webpage and get the content, call it page_content
    page = requests.get(URL)
    page_content = BeautifulSoup(page.content, 'html.parser')
    #Find images on the website with the attribute "data-image-title" and assign the title's value as extractedTitle. This is the unique title given to the image showing bias on each page. This title conviniently is short and is named after the bias it shows. E.g. left07
    images = page_content.find_all("img", attrs = {"data-attachment-id":True})#image-title":True})

    #print(f'images = {images}')
    bias = images[0]
    bias_title = bias['data-image-title']

    factual_reporting = images[2]
    factual_reporting_title = factual_reporting['data-image-title']
    #img_details = page_content.find("img", attrs={"data-image-title":True})
    #extractedTitle = img_details['data-image-title']
    #return the title without the numbers at the end
    return bias_title[:-2], factual_reporting_title[4:]

#print(getBias('hot-air'))

print("nwebscraper loaded")