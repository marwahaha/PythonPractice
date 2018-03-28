import fleep
import os

file1 = open("D:\Documents\leep_res.txt", "w")
file1.close()

def walkdir(folder):
    #Walk through each files in a directory
    for dirpath, dirs, files in os.walk(folder):
        for filename in files:
            yield os.path.abspath(os.path.join(dirpath, filename))

input_dir = input("Give an input directory: ")

for filepath in walkdir(input_dir):
    with open(filepath, "rb") as fh:
        info = fleep.get(fh.read(128))
    extension = info.extension

    file_write = open("D:\Documents\leep_res.txt", "a")
    file_write.write("\n" + filepath + " >>>> " + str(extension))
    file_write.close()