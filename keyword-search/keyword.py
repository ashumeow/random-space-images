import urllib
import os
import urlparse

def meowFetchImages(start, stop):
    meowInit = (
        'hubble',
        'nebula',
        'galaxy'
    )
    helloMeow = start
    for i in range(start, start+stop+1):
        urllib.urlretrieve("http://geekresearchlab.net/space/keyword/"+str(helloMeow)+".jpg", str(helloMeow)+".jpg")
        print("Image "+str(meowInit)+" fetched.")
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
    print("Keyword-based image capture\n")
    start = raw_input("Current available keywords are: 'hubble','galaxy','nebula'\n Enter a keyword for the right random image to be captured?:\n")
    stop = raw_input("Type 1 to begin: \n")
    print("Capturing images...\n")
    meowPath()
    meowFetchImages(int(start), int(stop))

meow()