import os
import time

def walkdir(folder):
    #Walk through each files in a directory
    for dirpath, dirs, files in os.walk(folder):
        for filename in files:
            print(filename)
            yield os.path.abspath(os.path.join(dirpath, filename))

dir = input("Give a testing directory: ")

for filepath in walkdir(dir):
    time.sleep(0.1)