import binascii

hex_headers = {""}

file = input("Give file input: ")
with open(file, 'rb') as f:
    content = f.read()
var = str(binascii.hexlify(content))
print(var[2:40])