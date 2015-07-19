import urllib
import os
import urllib2
import json

def meowFetch():
    # available keywords
    helloMeow = {
    hubble: 'hubble',
    nebula: 'nebula',
    galaxy: 'galaxy'
    }
    # target url
    meow_url=("http://geekresearchlab.net/space/keyword/"+str(helloMeow)+".jpg".format(helloMeow))
    # URL fetch/retrieve
    meowCatch=urllib.urlretrieve(meow_url)
    # looping
    for meow_url in meowCatch.read():
        print("Image fetched")

def meowPath():
    # path locator
    meowCurrent = os.getcwd()
    # if path doesn't exists
    if not os.path.exists(meowCurrent+"/space/keyword/"):
         print("Wait.. Folder not found!\n")
         print("Creating a new folder...\n")
         os.makedirs(meowCurrent+"/space/keyword/")
         os.chdir(meowCurrent+"/space/keyword/")
    else:
        # if path exists
         os.chdir(meowCurrent+"/space/keyword/")

def meow():
    # main execution area
    print("Keyword-based Images Capture\n")
    helloMeow = raw_input("Available keywords: 'hubble','nebula','galaxy'\n")
    print("Type any one of the available keywords: \n")
    print("Capturing images...\n")
    meowPath()
    meowFetch(int(helloMeow))
meow()