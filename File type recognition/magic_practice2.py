import os
import magic

def walkdir(folder):
    #Walk through each files in a directory
    for dirpath, dirs, files in os.walk(folder):
        for filename in files:
            yield os.path.abspath(os.path.join(dirpath, filename))


input_dir = input("Give an directory: ")
output_file = "/home/jasper/output2.txt"
file_create = open(output_file, "w")
file_create.write("Directory traversed: " + input_dir + "\ndic = {")
file_create.close()
output_dic = {}
counter = 0

for filepath in walkdir(input_dir):
    curr_magic = magic.from_file(filepath, mime=True)
    filename, file_extension = os.path.splitext(filepath)

    if not str(file_extension):
        continue

    try:
        if curr_magic not in output_dic[file_extension]:
            output_dic[file_extension].append(curr_magic)
            continue
    except KeyError:
        pass


    output_dic[file_extension] = [curr_magic]


file_write = open(output_file, "a")

for i in output_dic:
    file_write.write("\n    '" + i + "': [")
    for value in output_dic[i]:
        file_write.write("'" + value + "',")
    file_write.write("],")

file_write.close()

file_write2 = open(output_file, "a")
file_write2.write("\n}")
