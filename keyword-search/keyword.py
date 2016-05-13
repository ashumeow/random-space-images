import urllib
import os

def meowFetchImages(start):
    urllib.urlretrieve("http://geekresearchlab.net/space/hubble/"+helloMeow+".jpg", +helloMeow+".jpg")
    print("Woo hoo! Finished")

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
    print("Capturing images...\n")
    meowPath()
    meowFetchImages(start)

meow()
