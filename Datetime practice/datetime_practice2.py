import datetime
import os

def walkdir(folder):
    #Walk through each files in a directory
    for dirpath, dirs, files in os.walk(folder):
        for filename in files:
            yield os.path.abspath(os.path.join(dirpath, filename))


dir = input("Give a dir: ")
date_list = []
for filepath in walkdir(dir):
    raw_time = os.path.getmtime(filepath)
    readable_time = datetime.datetime.fromtimestamp(raw_time).strftime('%Y-%m-%d %H:%M:%S')
    date_list.append(readable_time)

date_list.sort()
print(date_list)