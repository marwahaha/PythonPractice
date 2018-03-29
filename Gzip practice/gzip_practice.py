import gzip

open_file = gzip.open(input("Specify file location: "), "r")
file_content = open_file.readlines()

for i in file_content:
    if "lokwoord" in str(i):
        print(i)

print(file_content)