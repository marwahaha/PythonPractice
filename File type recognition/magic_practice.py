import magic

f = magic.from_file(str(input("File: ")), mime=False)
print(f)