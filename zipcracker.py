# Author PiereLucas

#
# Module
#
import zipfile, threading

def crack(zip, pwd):
    try:
        zip.extractall(pwd=pwd)
        print("Success: Password is " + pwd)
    except:
        pass

for i in range(3, 10):
