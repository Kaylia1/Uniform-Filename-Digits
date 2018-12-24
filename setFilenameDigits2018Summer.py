#IMPORTANT: place this setFilenameDigits.py file to the folder directory your scanning, or the files you rename will move to wherever this file is
#need py2

import os, os.path
import sys

#HARDCODE this section
filenameDigits = 5 #num total digits in your file to change to
directory = "/Users/kaylee/Desktop/labellingtool_testpics"
ending = ".jpg" #files with this ending will change name

#PLEASE comment out 1 of the 2 following:

#IMPORTANT NOTE: works with string names too and w/ spaces, USE ONLY TO EXTEND NAME
#filenameDigits += len(ending)
#for i in os.listdir(directory):
#    if i.endswith(ending):
#        filename = i.zfill(filenameDigits)
#        print str(i)+ " "+ str(filename)
#        os.rename(directory+"/"+i, filename)

#IMPORTANT NOTE: DOES NOT work with string names too and w/ spaces (only int names), CAN shrink length if not cutting data (if would cut data, filename does not change)
for i in os.listdir(directory):
    if i.endswith(ending):
        filename = int(i.replace(ending,""))
        print(filename)
        filename = str(filename).zfill(filenameDigits)
        filename = filename + ending
        print str(i)+ " "+ str(filename)
        os.rename(directory+"/"+i, filename)
