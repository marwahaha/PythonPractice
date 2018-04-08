from datetime import datetime
import os

file = input("Give a file: ")
raw_time = os.path.getmtime(file)
readable_time = datetime.fromtimestamp(raw_time).strftime('%Y-%m-%d %H:%M:%S')
print(readable_time)