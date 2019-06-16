from wsinstalls import *
installModule()
from wsfunc import *

# Text
print("----------------------------------------")
print("Basic Web Scraper (BWS) by Johari19\n")
print("Script made by: https://github.com/Johari19\n")
print("This script allows you to scrape info off the web using elements, classes and ids!")
print("Javascript is not working currently!\n")
print("Some websites don't allow this script to work!\n")

# Variables
while True:
    url = str(input("Enter url of the site you would like to scrape (USE: https://www.websitename.com): "))
    if not url:
        log_error('Empty url/formatted incorrectly')
        time.sleep(10)
    else:
        #nothing
        time.sleep(.2)
    print('\nGrabbing html file of {0}'.format(url))
    raw_html = get_URL(url)
    html = BeautifulSoup(raw_html, 'html.parser')
    choice = input("\nWould you like to use 1. Class 2. ID: ")
    sign = ''




    if choice == '1':
        sign = '.'
        element = str(input("\nPick the element you want to find: "))
        atr = str(input("\nPick the element's class: "))
    elif choice == '2':
        sign = '#'
        element = str(input("\nPick the element you want to find: "))
        atr = str(input("\nPick the element's id: "))
    elif not choice:
        log_error('Empty choice')
        time.sleep(10)
    else:
        log_error('Invalid choice')
        time.sleep(10)

    if not atr:
        foo = element;

    else:
        foo = element + sign + atr;

    # Script
    print("\nI found:")
    for element in html.select(foo):
        print(element.get_text())
    pause()
    print("----------------------------------------")
