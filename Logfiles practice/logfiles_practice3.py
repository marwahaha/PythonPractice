import os
import magic
import gzip
import re
import datetime
from dateutil import parser

file_check = magic.Magic(mime=True)
gzip_types = [
    "application/x-gzip",
    "application/gzip"
]

def walkdir(folder):
    #Walk through each files in a directory
    for dirpath, dirs, files in os.walk(folder):
        for filename in files:
            yield os.path.abspath(os.path.join(dirpath, filename))

#Function that checks logfiles for content
def logfile_check(dir):
    failed_logins = []
    for filepath in walkdir(dir):
        absolute_path, extension = os.path.splitext(filepath)
        if "text" in file_check.from_file(filepath):
            failed_logins = textfile_checker(failed_logins, filepath)
        elif file_check.from_file(filepath) in gzip_types:
            failed_logins = gzip_checker(failed_logins, filepath)
        else:
            print("Not a log file found at: " + filepath)
            continue
    return failed_logins

def textfile_checker(failed_logins, filepath):
    open_file = open(filepath, "r")
    read_file = open_file.readlines()
    for line in read_file:
        if "auth" in filepath:
            if re.match("((.*)failed(.*)password(.*)|(.*)password(.*)failed(.*))", line, re.IGNORECASE):
                raw = os.path.getmtime(filepath)
                read_time = datetime.datetime.fromtimestamp(raw).strftime('%Y-%m-%d %H:%M:%S')
                currdate_time = parser.parse(line[:30], fuzzy=True, default=datetime.datetime(int(read_time[:4]), int(read_time[6:7]), int(read_time[9:10])))
                failed_logins.append([line, currdate_time])
        else:
            if re.match("((.*)fail(ed)?(.*)login(s)?(.*)|(.*)login(s)?(.*)fail(ed)?(.*))", line, re.IGNORECASE):
                raw = os.path.getmtime(filepath)
                read_time = datetime.datetime.fromtimestamp(raw).strftime('%Y-%m-%d %H:%M:%S')
                currdate_time = parser.parse(line[:30], fuzzy=True, default=datetime.datetime(int(read_time[:4]), int(read_time[6:7]), int(read_time[9:10])))
                failed_logins.append([line, currdate_time])
    return failed_logins

def gzip_checker(failed_logins, filepath):
    open_file = gzip.open(filepath, "r")
    read_file = open_file.readlines()
    for line in read_file:
        if "auth" in filepath:
            if re.match("((.*)failed(.*)password(.*)|(.*)password(.*)failed(.*))", str(line), re.IGNORECASE):
                raw = os.path.getmtime(filepath)
                read_time = datetime.datetime.fromtimestamp(raw).strftime('%Y-%m-%d %H:%M:%S')
                currdate_time = parser.parse(str(line)[:30], fuzzy=True, default=datetime.datetime(int(read_time[:4]), int(read_time[6:7]), int(read_time[9:10])))
                failed_logins.append([line, currdate_time])
        else:
            if re.match("((.*)fail(ed)?(.*)login(s)?(.*)|(.*)login(s)?(.*)fail(ed)?(.*))", str(line), re.IGNORECASE):
                raw = os.path.getmtime(filepath)
                read_time = datetime.datetime.fromtimestamp(raw).strftime('%Y-%m-%d %H:%M:%S')
                currdate_time = parser.parse(str(line)[:30], fuzzy=True, default=datetime.datetime(int(read_time[:4]), int(read_time[6:7]), int(read_time[9:10])))
                failed_logins.append([line, currdate_time])
    return failed_logins

input_dir = input("Give an directory: ")
print(logfile_check(input_dir))