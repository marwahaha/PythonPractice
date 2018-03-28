from difflib import SequenceMatcher
import binascii
import hex_dictionary
import os

def walkdir(folder):
    #Walk through each files in a directory
    for dirpath, dirs, files in os.walk(folder):
        for filename in files:
            yield os.path.abspath(os.path.join(dirpath, filename))

def similar(stringa, stringb):
    s = SequenceMatcher(None, stringa, stringb)
    return s.get_matching_blocks()

dir_input = input("Give directory input: ")
file1 = open("D:\Documents\man_result.txt", "w")
file1.write("Directory traversed: " + dir_input)
file1.close()

for filepath in walkdir(dir_input):
    with open(filepath, 'rb') as f:
        content = f.read(1024)  # Reads only first 1024 bytes
    hex_string = str(binascii.hexlify(content))
    similarity = 0
    old_similarity = 0

    for key, value in hex_dictionary.dic.items():
        similarity = similar(hex_string[2:40], value)
        block_str = str(similarity[0])
        if block_str[8] == "0" and block_str[13] == "0":
            similarity2 = block_str[21]
            if similarity2 > str(old_similarity):
                old_similarity = similarity2
                extension = key


    print("File format recognized as: " + extension)
    file1 = open("D:\Documents\man_result.txt", "a")
    file1.write("\n" + filepath + " >>>>>> " + hex_string[2:40] + ">>>>>>" + extension)
    file1.close()




