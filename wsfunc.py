from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
import time
from datetime import datetime
if __name__ == "__main__":
    print("DO NOT RUN THIS SCRIPT! IT DOES NOTHING")
    time.sleep(10)
else:
    def log_error(e):
        timestamp = datetime.now()
        print(e)
        f = open("error.txt","a+")
        f.write('[' + str(timestamp) + ']\n' + 'Error: ' + e + ' \n')
        f.close()
    def get_URL(url):

        try:
            with closing(get(url, stream=True, allow_redirects=False)) as resp:
                if responsetest(resp):
                    return resp.content
                else:
                    return None

        except requests.RequestException as e:
            log_error('Error during requests to {0} : {1}'.format(url, str(e)))
            return None


    def responsetest(resp):
        content_type = resp.headers['Content-Type'].lower()
        return (resp.status_code == 200
                and content_type is not None
                and content_type.find('html') > -1)





    def pause():
        programPause = input("Press the <ENTER> key to continue...")
