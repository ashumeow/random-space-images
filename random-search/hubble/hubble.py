import urllib
import os

def meowFetchImages(start, stop):
    meowInit = 0
    helloMeow = start
    for i in range(start, start+stop+1):
        urllib.urlretrieve("http://geekresearchlab.net/space/hubble/"+str(helloMeow)+".jpg", str(helloMeow)+".jpg")
        print("Image# "+str(meowInit)+" of "+str(stop)+" fetched.")
        meowInit += 1
        helloMeow += 1
    print("Woo hoo! Finished")

def meowPath():
    meowCurrent = os.getcwd()
    if not os.path.exists(meowCurrent+"/space/hubble/"):
         print("Wait.. Folder not found!\n")
         print("Creating a new folder...\n")
         os.makedirs(meowCurrent+"/space/hubble/")
         os.chdir(meowCurrent+"/space/hubble/")
    else:
         os.chdir(meowCurrent+"/space/hubble/")

def meow():
    print("Random Images Capture from Hubble Telescope\n")
    start = raw_input("Pick a random number?:\n")
    stop  = raw_input("How many images do you want to download?: ")
    print("Capturing images...\n")
    meowPath()
    meowFetchImages(int(start), int(stop))

meow()