from difflib import SequenceMatcher
import binascii
import hex_dictionary

def similar(stringa, stringb):
    return SequenceMatcher(None, stringa, stringb).ratio()

file = input("Give file input: ")
with open(file, 'rb') as f:
    content = f.read(1024) #Reads only first 1024 bytes
hex_string = str(binascii.hexlify(content))
print(hex_string[2:40])
similarity = 0
old_similarity = 0
i = 0
alt = []

for key, value in hex_dictionary.dic.items():
    similarity = similar(hex_string[2:40], value)
    if similarity > old_similarity:
        old_similarity = similarity
        extension = key

print(old_similarity)
print("File format recognized as: " + extension)

#Works, but is not accurate
for key, value in hex_dictionary.dic.items():
    if similar(hex_dictionary.dic[extension], value) > 0.69:
        alt.append(key)
        i =+ 1

print("Alternatives found: " + str(alt))