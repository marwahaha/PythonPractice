#Dictionary practice 2 for advanced dictionary's

extension = "0"
counter = 0
pair = {}


while counter < 100:
    counter += 1
    extension = extension + str(counter)
    file_name = str(counter)
    pair[file_name] = extension

print(pair)