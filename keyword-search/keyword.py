import urllib
import os

def meowFetch():
    helloMeow = ['hubble','nebula','galaxy']
    meow_url="http://geekresearchlab.net/space/keyword/"
    urllib.urlretrieve(meow_url+str(helloMeow)+".jpg")
    print ("Image fetched")

def meowPath():
    meowCurrent = os.getcwd()
    if not os.path.exists(meowCurrent+"/space/keyword/"):
         print("Wait.. Folder not found!\n")
         print("Creating a new folder...\n")
         os.makedirs(meowCurrent+"/space/keyword/")
         os.chdir(meowCurrent+"/space/keyword/")
    else:
         os.chdir(meowCurrent+"/space/keyword/")

def meow():
    print("Keyword-based Images Capture\n")
    start = raw_input("Available keywords: 'hubble','nebula','galaxy'\n")
    print("Type any one of the available keywords: \n")
    print("Capturing images...\n")
    meowFetch(int(helloMeow))
    meowPath()

meow()