import os
import re
import datetime
from dateutil import parser


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
        open_file = open(filepath, "r")
        try:
            read_file = open_file.readlines()
        except UnicodeDecodeError:
            continue
        for line in read_file:
            if "auth" in filepath:
                if re.match("((.*)failed(.*)password(.*)|(.*)password(.*)failed(.*))", line, re.IGNORECASE):
                    mtime = os.path.getmtime(filepath)
                    read_time = datetime.datetime.fromtimestamp(mtime).strftime('%Y-%m-%d %H:%M:%S')
                    currdate_time = parser.parse(line[:30], fuzzy=True, default=datetime.datetime(int(read_time[:4]), int(read_time[6:7]), int(read_time[9:10])))
                    print(currdate_time)
                    print(filepath)
                    failed_logins.append([line, currdate_time])
            else:
                if re.match("((.*)fail(ed)?(.*)login(s)?(.*)|(.*)login(s)?(.*)fail(ed)?(.*))", line, re.IGNORECASE):
                    mtime = os.path.getmtime(filepath)
                    read_time = datetime.datetime.fromtimestamp(mtime).strftime('%Y-%m-%d %H:%M:%S')
                    currdate_time = parser.parse(line[:30], fuzzy=True, default=datetime.datetime(int(read_time[:4]), int(read_time[6:7]), int(read_time[9:10])))
                    print(currdate_time)
                    print(filepath)
                    failed_logins.append([line, currdate_time])
    return failed_logins
input_dir = input("Give an directory: ")
print(logfile_check(input_dir))