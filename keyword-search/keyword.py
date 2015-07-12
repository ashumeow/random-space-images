import urllib
import os

def meowFetch():
    for start in helloMeow:
        # available keywords
        helloMeow = ['hubble','nebula','galaxy']
        # target url
        meow_url="http://geekresearchlab.net/space/keyword/"+str(helloMeow)+".jpg"
        # URL fetch/retrieve
        meowCatch=urllib.urlretrieve(meow_url)
        print ("Image fetched")

def meowPath():
    # path locator
    meowCurrent = os.getcwd()
    if not os.path.exists(meowCurrent+"/space/keyword/"):
         print("Wait.. Folder not found!\n")
         print("Creating a new folder...\n")
         os.makedirs(meowCurrent+"/space/keyword/")
         os.chdir(meowCurrent+"/space/keyword/")
    else:
         os.chdir(meowCurrent+"/space/keyword/")

def meow():
    # main execution area
    print("Keyword-based Images Capture\n")
    start = raw_input("Available keywords: 'hubble','nebula','galaxy'\n")
    print("Type any one of the available keywords: \n")
    print("Capturing images...\n")
    meowFetch()
    meowPath()
meow()