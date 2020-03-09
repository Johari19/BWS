from wsinstalls import *
installModule()
from wsfunc import *

# Text
print("----------------------------------------")
print("Basic Web Scraper (BWS) by Joseph Ambayec\n")
print("Script made by: https://github.com/Johari19\n")
print("This is a looping variant of the original scraper!")
print("Use this for things like stocks, time and etc.")
print("Sometimes this does not work as some websites have static values!\n")

# Variables
url = str(input("Enter url of the site you would like to scrape (USE: https://www.websitename.com): "))
if not url:
    log_error('Empty url/formatted incorrectly')
    time.sleep(10)
else:
    #nothing
    time.sleep(.2)
choice = input("\nWould you like to use 1)Class 2)ID: ")
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
f = open('value.csv', 'w')
writer = csv.writer(f)
writer.writerow(['Timestamp', 'Value'])
f.close()
print("I'm saving all the values in an easily formatable .csv file! Check value.csv")
print("\nI found:")
while True:
    timestamp = str(datetime.now().strftime('%H:%M:%S'))
    raw_html = get_URL(url)
    html = BeautifulSoup(raw_html, 'html.parser')
    for element in html.select(foo):
        eltext = element.get_text()
        f = open('value.csv', 'a')
        writer = csv.writer(f)
        writer.writerow([timestamp, eltext])
        f.close()
        print('[' + timestamp + '] ' + eltext, end="\r")
    time.sleep(1.25) # <---- DO NOT REMOVE! IF REMOVED, USER MAY RISK IP BAN FROM WEBSITE!
