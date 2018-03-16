import binascii

file = input("Give file input: ")
with open(file, 'rb') as f:
    content = f.read()
print(binascii.hexlify(content))