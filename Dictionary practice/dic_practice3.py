dict1 = {"Jan":{"Age":20, "Length":165}, "Piet":{"Age":35, "Length":185}}
jan = dict1["Jan"]
print(jan)

for man in dict1:
    print(dict1[man]["Age"])