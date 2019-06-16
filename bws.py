from wsinstalls import *
installModule()
from wsfunc import *

# Text
print("----------------------------------------")
print("Basic Web Scraper (BWS) by Johari19\n")
print("\nYou need to have a basic understanding of html elements and classes to use this properly!\n")
print("Script made by: https://github.com/Johari19\n")
print("This script only uses elements and classes. Using ids and javascript will not work!\n")
print("Some websites don't allow this script to work!\n")

# Variables
while True:
    url = str(input("\nEnter url of the site you would like to scrape (USE: https://websitename.com): "))
    print('Grabbing html file of {0}'.format(url))
    raw_html = get_URL(url)
    html = BeautifulSoup(raw_html, 'html.parser')
    element = str(input("Pick the element you want to find: "))
    classes = str(input("Pick the element's class: "))


    if not classes:
        foo = element;

    else:
        foo = element + '.' + classes;
        
    # Script
    print("\nI found:")
    for element in html.select(foo):
        print(element.get_text())
    pause()
