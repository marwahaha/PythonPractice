import binascii

file = input("Give file input: ")
with open(file, 'rb') as f:
    content = f.read(1024) #Reads only first 1024 bytes
var = str(binascii.hexlify(content))
print(var[2:40])