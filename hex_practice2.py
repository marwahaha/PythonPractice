import binascii

file = input("Give file input: ")
with open(file, 'rb') as f:
    content = f.read()
var = binascii.hexlify(content)
print(var[0:40])