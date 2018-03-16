s = open("/home/jasper/Pictures/images.ico").read()
hex_list = ["{:02x}".format(ord(c)) for c in s]
print(hex_list)