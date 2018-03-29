import magic

f = magic.from_file(str(input("File: ")), mime=True)
print(f)