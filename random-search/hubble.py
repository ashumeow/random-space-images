import urllib
import os

def fetchImages(start, stop):
    counter = 0
    imgIndex = start
    for i in range(start, start+stop+1):
        urllib.urlretrieve(""+str(imgIndex)+".jpg", str(imgIndex)+".jpg")
        print("Image# "+str(counter)+" of "+str(stop)+" captured.")
        counter += 1
        imgIndex += 1
    print("Finished")

def pathFolder():
    cur_folder = os.getcwd()
    if not os.path.exists(cur_folder+"/space/hubble/"):
         print("Wait.. Folder not found!\n")
         print("Creating a new folder...\n")
         os.makedirs(cur_folder+"/space/hubble/")
         os.chdir(cur_folder+"/space/hubble/")
    else:
         os.chdir(cur_folder+"/space/hubble/")

def main():
    print("Random Images Capture from Hubble Telescope\n")
    start = raw_input("Pick a random number?:\n")
    stop  = raw_input("How many images do you want to download?: ")
    print("Capturing images...\n")
    pathFolder()
    fetchImages(int(start), int(stop))

main()
