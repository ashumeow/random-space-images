import urllib
import os

def meowFetchImages(start, stop):
    meowInit = 0
    helloMeow = start
    for i in range(start, start+stop+1):
        urllib.urlretrieve(""+str(helloMeow)+".jpg", str(helloMeow)+".jpg")
        print("Image# "+str(meowInit)+" of "+str(stop)+" fetched.")
        meowInit += 1
        helloMeow += 1
    print("Woo hoo! Finished")

def meowPath():
    meowCurrent = os.getcwd()
    if not os.path.exists(meowCurrent+"/space/planets/"):
         print("Wait.. Folder not found!\n")
         print("Creating a new folder...\n")
         os.makedirs(meowCurrent+"/space/planets/")
         os.chdir(meowCurrent+"/space/planets/")
    else:
         os.chdir(meowCurrent+"/space/planets/")

def meow():
    print("Random Images Capture from Space Planets\n")
    start = raw_input("Pick a random number?:\n")
    stop  = raw_input("How many images do you want to download?: ")
    print("Capturing images...\n")
    meowPath()
    meowFetchImages(int(start), int(stop))

meow()