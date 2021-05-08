import requests

#Where are we getting this info?
bias_checking_website = "https://mediabiasfactcheck.com/"

def convert(argument):
    switcher = {
        "extremeright": "Extreme-Right",
        "right": "Right",
        "rightcenter" : "Right-Center",
        "leastbiased" : "Least-Biased",
        "extremeleft": "Extreme-Left",
        "left": "Left",
        "leftcenter" : "Left-Center",
        "VeryHigh" : "Very-High",
        "High" : "High",
        "MostlyFactual" : "Mostly-Factual",
        "Mixed" : "Mixed",
        "Low" : "Low",
        "VeryLow" : "Very-Low",
        "satirelabel" : "Satire"
    }
    return switcher.get(argument, "Not Classified/Found")

def get_bias(source_name):
    response = requests.get(bias_checking_website + source_name)
    if response.status_code != 200:
        return "Page not found", "Page not found"
    response = response.text

    parts = response.split('data-image-title')

    bias = parts[1]
    bias = bias[2:bias.find('"',2)-2]

    try:
        factual_reporting = parts[5]
        factual_reporting = factual_reporting[6:factual_reporting.find('"',6)]
    except:
        factual_reporting = "satirelabel"

    print(f"Bias: {bias}")
    print(f"Factual Reporting: {factual_reporting}")
    return convert(bias), convert(factual_reporting)

print("nwebscraper loaded")
