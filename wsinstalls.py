from subprocess import call, DEVNULL
import subprocess
import time
import os
from sys import platform
if __name__ == "__main__":
    print("DO NOT RUN THIS SCRIPT! IT DOES NOTHING")
    time.sleep(10)
else:


    def installModule():
        def install(name):
            subprocess.call(['pip', 'install', name], stderr=DEVNULL, stdout=DEVNULL)
        if __name__ == "wsinstalls":
            print("Installing requests modules...")
            install('requests')
            time.sleep(.1)
            print("Installing beautifulsoup4 modules...")
            install("beautifulsoup4")
            time.sleep(.1)
            print("Installed all modules!")
            print("Importing modules...")

            time.sleep(.1)
            print("Imported all modules!")
        else:
            print("Installation process failed!")
            os.system('pause')
