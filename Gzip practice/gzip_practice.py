import gzip

open_file = gzip.open(input("Specify file location: "), "r")
file_content = open_file.read()
print(file_content)