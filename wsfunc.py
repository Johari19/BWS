from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
import time


if __name__ == "__main__":
    print("DO NOT RUN THIS SCRIPT! IT DOES NOTHING")
    time.sleep(10)
else:


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


    def log_error(e):
        print(e)
       
        
    def pause():
        programPause = input("Press the <ENTER> key to continue...")

        
