#Does not work!
import binascii

file_path = 'D:\Documents\RZTP01.wbfs'

chunk_size = 1024
with open(file_path, 'rb') as f:
    while True:
        data = f.read(chunk_size)
        if not data:
            break
    hexa = binascii.hexlify(data)
    print(hexa)
    hexa_string = hexa.decode('ascii')
    print(hexa_string)