import os
import magic

def walkdir(folder):
    #Walk through each files in a directory
    for dirpath, dirs, files in os.walk(folder):
        for filename in files:
            yield os.path.abspath(os.path.join(dirpath, filename))


input_dir = input("Give an directory: ")
output_file = "/home/jasper/output1.txt"
file_create = open(output_file, "w")
file_create.write("Directory traversed: " + input_dir + "\ndic = {")
file_create.close()

for filepath in walkdir(input_dir):
    curr_magic = magic.from_file(filepath, mime=True)
    file_write = open(output_file, "a")
    file_write.write("\n    " + filepath + " >>>> " + curr_magic)
    file_write.close()

file_write2 = open(output_file, "a")
file_write2.write("\n}")